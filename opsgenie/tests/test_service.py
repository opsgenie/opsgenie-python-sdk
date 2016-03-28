import json

import httpretty
from requests import Response
from requests.exceptions import RetryError
from requests.packages.urllib3 import Retry

from opsgenie.alert.requests import GetAlertRequest
from opsgenie.config import ProxyConfiguration, HttpConfiguration
from opsgenie.errors import ServerError
from opsgenie.service import generate_params, generate_proxy, generate_timeout_and_retry, execute_http_call, \
    handle_error
from opsgenie.tests import OpsGenieTestCase


class TestService(OpsGenieTestCase):
    def test_generating_params(self):
        request = GetAlertRequest(alias="Alias")
        params = generate_params("API_KEY", request)

        self.assertIsNone(params['id'], 'Id should be none')
        self.assertIsNone(params['tinyId'], 'tiny_id should be none')
        self.assertEqual('Alias', params['alias'])
        self.assertEqual('API_KEY', params['apiKey'])

    def test_generating_proxy(self):
        proxy_config = ProxyConfiguration("_HOST", 8080, protocol="HTTP")
        proxy = generate_proxy(proxy_config)

        self.assertEqual("http://_HOST:8080", proxy['http'])

        proxy_config = ProxyConfiguration("_HOST", 8080, "_USERNAME", "_PASSWORD", "HTTPS")
        proxy = generate_proxy(proxy_config)

        self.assertEqual("https://_USERNAME:_PASSWORD@_HOST:8080", proxy['https'])

    def test_generating_timeout_and_retry(self):
        http_config = HttpConfiguration(connect_timeout=10, read_timeout=20, max_retry=5)
        timeout, retry = generate_timeout_and_retry(http_config)

        self.assertEqual(10, timeout[0])
        self.assertEqual(20, timeout[1])
        self.assertEqual(5, retry.total)

    @httpretty.activate
    def test_executing_over_proxy(self):
        request_count = {'total': 0}

        def request_callback(request, uri, headers):
            request_count['total'] += 1
            return 200, headers, "Established"

        httpretty.register_uri(httpretty.GET, "http://proxy-test.com", body=request_callback)

        retry = Retry(total=7, status_forcelist=[500])
        timeout = (10, 10)
        proxy = {'http': 'http://proxy-test.com:80'}
        execute_http_call('GET', 'http://opsgenie.com', {}, retry, timeout, proxy)
        self.assertEqual(1, request_count['total'])

    @httpretty.activate
    def test_retrying_errors(self):
        request_count = {'total': 0}

        def request_callback(request, uri, headers):
            request_count['total'] += 1
            return 500, headers, "error-message"

        httpretty.register_uri(httpretty.GET, "http://opsgenie.com", body=request_callback)

        retry = Retry(total=7, status_forcelist=[500])
        timeout = (10, 10)
        with self.assertRaisesRegexp(RetryError, "Max retries exceeded"):
            execute_http_call('GET', 'http://opsgenie.com', {}, retry, timeout, None)
            self.assertEqual(8, request_count['total'])

    def test_handle_error(self):
        class TestResponse(Response):
            @property
            def text(self):
                return json.dumps({'code': 101, 'error': 'error-message'})

        resp = TestResponse()
        resp.status_code = 200

        handle_error(resp)

        resp.status_code = 201
        with self.assertRaisesRegexp(ServerError, "error-message"):
            handle_error(resp)
