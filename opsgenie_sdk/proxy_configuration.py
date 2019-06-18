from opsgenie_sdk.errors import InvalidConfigurationError


class ProxyConfiguration:
    def __init__(self, host=None, port=None, username=None, password=None, protocol=None):
        """
        Proxy configuration to use with opsgenie_sdk
        ----------
        Example Usage:
            conf = opsgenie_sdk.configuration.Configuration()
            proxy_url = opsgenie_sdk.proxy_configuration.ProxyConfiguration().get_proxy_url()
            conf.proxy = proxy_url
        ----------
        Parameters:
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

    def get_proxy_url(self):
        self.validate()

        if self.username:
            return self.protocol + '://' + self.username + ':' + self.password + '@' + self.host + ':' + self.port
        else:
            return self.protocol + '://' + self.host + ':' + self.port
