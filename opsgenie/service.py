import platform

import pkg_resources
import requests
from requests import Response
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

from .config import ProxyConfiguration, HttpConfiguration
from .errors import ServerError
from .request import BaseRequest


def generate_params(api_key, request):
    """
    Used to generate params from request
    Parameters
    ----------
    api_key : str
    request : BaseRequest

    Returns
    -------

    """
    params = request.decode()
    params['apiKey'] = api_key
    return params


def generate_proxy(proxy_config):
    """
    Generate requests specific proxy configuration
    Parameters
    ----------
    proxy_config : ProxyConfiguration

    Returns
    -------
    proxy config for requests
    """
    proxy = None
    if proxy_config:
        if proxy_config.username:
            proxy = {proxy_config.protocol: '{0}://{1}:{2}@{3}:{4}'.format(proxy_config.protocol,
                                                                           proxy_config.username,
                                                                           proxy_config.password,
                                                                           proxy_config.host,
                                                                           proxy_config.port)}
        else:
            proxy = {proxy_config.protocol: '{0}://{1}:{2}'.format(proxy_config.protocol,
                                                                   proxy_config.host,
                                                                   proxy_config.port)}

    return proxy


def generate_timeout_and_retry(http_config):
    """
    Generate timeout and retry mechanism for requests to use
    Parameters
    ----------
    http_config : HttpConfiguration

    Returns
    -------
    tuple (tuple, Retry)
    """
    timeout = (http_config.connect_timeout, http_config.read_timeout)

    retry = Retry(total=http_config.max_retry, status_forcelist=[500, 501, 502, 503])

    return timeout, retry


def generate_user_agent():
    version = pkg_resources.require("opsgenie-sdk")[0].version
    return "opsgenie-python-sdk/{0}; {1}/{2}; {3}".format(version,
                                                          platform.system(), platform.release(),
                                                          platform.python_version())


def execute_http_call(method, url, params, retry, timeout, proxy, attachment=None):
    """
    Executes http call using requests library
    Parameters
    ----------
    method : str
    url : str
    params : dict
    retry : Retry
    timeout : tuple
    proxy : object
    attachment : str

    Returns
    -------
    Response
    """
    session = requests.session()
    session.mount('http://', HTTPAdapter(max_retries=retry))  # Documented in HTTPAdapter
    session.mount('https://', HTTPAdapter(max_retries=retry))  # Documented in HTTPAdapter
    session.headers = {'User-Agent': generate_user_agent()}
    if method is "GET":
        response = session.get(url, params=params, proxies=proxy, timeout=timeout)
    elif method is "DELETE":
        response = session.delete(url, params=params, proxies=proxy, timeout=timeout)
    elif method is "POST":
        if attachment is None:
            response = session.post(url, json=params, proxies=proxy, timeout=timeout)
        else:
            response = session.post(url, data=params, proxies=proxy, timeout=timeout,
                                    files={'attachment': open(attachment, 'rb')})
    else:
        raise NotImplementedError()

    return response


def execute(method, url_suffix, response_cls, attachment=False):
    """
    Executes http call with given parameters
    Parameters
    ----------
    method : {'GET', 'POST', 'DELETE'}
    url_suffix : str
    response_cls : class
        Class of response type
    attachment : bool
    """

    def request_wrapper(__):
        def request_call(self, request):
            """

            Parameters
            ----------
            self : BaseService
            request : instance of BaseRequest subclass

            Returns
            -------
            Instance of response_cls
            """
            request.validate()

            url = self.configuration.endpoint + url_suffix
            params = generate_params(self.configuration.apikey, request)
            proxy = generate_proxy(self.configuration.proxy_config)
            timeout, retry = generate_timeout_and_retry(self.configuration.http_config)

            response = execute_http_call(method, url, params, retry, timeout, proxy,
                                         None if attachment is False else request.attachment)

            handle_error(response)
            return response_cls(response.text)

        return request_call

    return request_wrapper


def handle_error(response):
    if response.status_code is not 200:
        raise ServerError(response.text)


class BaseService:
    def __init__(self, configuration):
        """

        Parameters
        ----------
        configuration : Configuration
        """
        self.configuration = configuration
