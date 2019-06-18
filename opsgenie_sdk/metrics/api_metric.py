import logging
from collections import namedtuple

from .publisher import Publisher


class ApiMetric(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self.logger = logging.getLogger('opsgenie_sdk')
        self._data = None
        self._metric = namedtuple('ApiMetric', ['transactionId', 'duration', 'resourcePath', 'resultMetadata',
                                                'httpResponse'])

        self._result_metadata = namedtuple('ResultMetadata',
                                           ['RequestId', 'ResponseTime', 'RateLimitState', 'RateLimitReason',
                                            'RateLimitPeriod', 'RetryCount'])

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name,
                                               self._data)

    @property
    def data(self):
        return self._data

    def build_metric(self, transaction_id, duration, resource_path, response_data, http_response, retry_count):
        try:
            self._data = self._metric(transaction_id, duration, resource_path,
                                      self._get_result_metadata(response_data, retry_count),
                                      http_response)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()
            self.logger.debug('API Metrics Published')

    def _get_result_metadata(self, response_data, retry_count):
        request_id = response_data.getheader(name='X-Request-ID')
        response_time = response_data.getheader(name='X-Response-Time')
        rate_limit_state = response_data.getheader(name='X-RateLimit-State')
        rate_limit_reason = response_data.getheader(name='X-RateLimit-Reason')
        rate_limit_period = response_data.getheader(name='X-RateLimit-Period-In-Sec')

        return self._result_metadata(RequestId=request_id,
                                     ResponseTime=response_time,
                                     RateLimitState=rate_limit_state,
                                     RateLimitReason=rate_limit_reason,
                                     RateLimitPeriod=rate_limit_period,
                                     RetryCount=retry_count)
