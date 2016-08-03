from .errors import ApiKeyMissingError, EndpointMissingError, InvalidConfigurationError


class Configuration:
    DEFAULT_ENDPOINT = 'https://api.opsgenie.com/v1/json'

    def __init__(self, apikey=None, endpoint=DEFAULT_ENDPOINT, http_config=None, proxy_config=None):
        """
        Configuration for OpsGenie client
        Parameters
        ----------
        apikey : str
            OpsGenie API KEY
        endpoint : str, optional
            OpsGenie WebApi url to use with OpsGenie client. (Default: http://api.opsgenie.com/v1/json)
        http_config : HttpConfiguration or dict
        proxy_config : ProxyConfiguration or dict
        """
        self.apikey = apikey
        self.endpoint = endpoint

        if http_config:
            if isinstance(http_config, HttpConfiguration):
                self.http_config = http_config
            else:
                self.http_config = HttpConfiguration(**http_config)
        else:
            self.http_config = HttpConfiguration()

        if proxy_config:
            if isinstance(proxy_config, ProxyConfiguration):
                self.proxy_config = proxy_config
            else:
                self.proxy_config = ProxyConfiguration(**proxy_config)
        else:
            self.proxy_config = None

    def validate(self):
        if not self.apikey:
            raise ApiKeyMissingError()

        if not self.endpoint:
            raise EndpointMissingError()

        if self.proxy_config:
            self.proxy_config.validate()

        self.http_config.validate()


class HttpConfiguration:
    DEFAULT_TIMEOUT = 30
    DEFAULT_MAX_RETRY = 5

    def __init__(self, connect_timeout=DEFAULT_TIMEOUT, read_timeout=DEFAULT_TIMEOUT, max_retry=DEFAULT_MAX_RETRY):
        """
        Http Configuration to use with OpsGenie client
        Parameters
        ----------
        connect_timeout : int, optional
            Connection timeout (Default: 30)
        read_timeout : int, optional
            Read timeout (Default: 30)
        max_retry : int, optional
            Retry count of the failed requests (excluding first request). (Default:5)
        """
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.max_retry = max_retry

    def validate(self):
        pass


class ProxyConfiguration:
    def __init__(self, host=None, port=None, username=None, password=None, protocol=None):
        """
        Proxy configuration to use with OpsGenie client
        Parameters
        ----------
        host : str
            IP or the domain name of the proxy server ("10.10.0.1")
        port : int
            Port number of the proxy server ( 5432 )
        username : str, optional
        password : str, optional
        protocol : {'http', 'https'}
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.protocol = protocol.lower() if protocol is not None else None

    def validate(self):
        if not self.host or not self.port:
            raise InvalidConfigurationError("Host and Port Should be given")
        if self.protocol is None or not (self.protocol == "http" or self.protocol == "https"):
            raise InvalidConfigurationError(
                "Proxy Protocol must be one of ['http', 'https']. Current: {}".format(self.protocol))
