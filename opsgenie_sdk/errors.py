import json


class OpsGenieError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)


class InvalidRequestError(OpsGenieError):
    pass


class ApiKeyMissingError(OpsGenieError):
    def __init__(self):
        super(ApiKeyMissingError, self).__init__('Api Key is not configured!')


class EndpointMissingError(OpsGenieError):
    def __init__(self):
        super(EndpointMissingError, self).__init__('OpsGenie end-point is not configured!')


class InvalidConfigurationError(OpsGenieError):
    def __init__(self, message):
        super(InvalidConfigurationError, self).__init__(message)


class ServerError(OpsGenieError):
    def __init__(self, json_str):
        try:
            self.json_obj = json.loads(json_str)
            self.message = self.json_obj.get('error', None)
            self.code = self.json_obj.get('code', None)
        except ValueError:
            self.message = json_str
        super(ServerError, self).__init__(self.message)
        self.code = -1


class HTTPException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" \
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
