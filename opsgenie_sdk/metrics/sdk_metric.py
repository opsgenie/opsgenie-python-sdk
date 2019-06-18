import logging
from collections import namedtuple

from .publisher import Publisher


class SdkMetric(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self.logger = logging.getLogger('opsgenie_sdk')
        self._data = None
        self._metric = namedtuple('SdkMetric',
                                  ['transactionId', 'duration', 'resourcePath', 'errorType', 'errorMessage',
                                   'sdkRequestDetails', 'sdkResultDetails'])

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name,
                                               self._data)

    @property
    def data(self):
        return self._data

    def build_metric(self, transaction_id, duration, resource_path, error_type, error_message, sdk_request_details,
                     sdk_result_details):
        try:
            self._data = self._metric(transaction_id, duration, resource_path, error_type, error_message,
                                      sdk_request_details,
                                      sdk_result_details)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()
            self.logger.debug('SDK Metrics Published')
