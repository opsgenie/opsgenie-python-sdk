import logging
from collections import namedtuple

from .publisher import Publisher


class HttpMetric(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self.logger = logging.getLogger('opsgenie_sdk')
        self._data = None
        self.metric = namedtuple('HttpMetric', ['transactionId', 'duration', 'resourcePath', 'retryCount', 'error',
                                                'status', 'statusCode', 'request'])

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name,
                                               self._data)

    @property
    def data(self):
        return self._data

    def build_metric(self, transaction_id, duration, resource_path, retry_count, error, status,
                     status_code, request):
        try:
            self._data = self.metric(transaction_id, duration, resource_path, retry_count, error, status, status_code,
                                     request)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()
            self.logger.debug('HTTP Metrics Published')
