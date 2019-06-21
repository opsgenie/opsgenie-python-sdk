import getopt
import sys

import opsgenie_sdk
from opsgenie_sdk.metrics.observer import Observer
from opsgenie_sdk.rest import ApiException


class MetricObserver(Observer):
    def notify(self, publisher):
        print("{}: '{}' has now metric data = {}".format(type(self).__name__,
                                                         publisher.name, publisher.data))


class Account:
    def __init__(self, opsgenie_api_key):
        self.conf = self.conf = opsgenie_sdk.configuration.Configuration()
        self.conf.api_key['Authorization'] = opsgenie_api_key

        self.conf.debug = False

        self.conf.retry_count = 5
        self.conf.retry_http_response = ['4xx', '5xx']
        self.conf.retry_delay = 2
        self.conf.retry_enabled = True

        self.api_client = opsgenie_sdk.api_client.ApiClient(configuration=self.conf)
        self.account_api = opsgenie_sdk.AccountApi(api_client=self.api_client)

    def get_info(self):
        try:
            info_response = self.account_api.get_info()
            print(info_response)
            return info_response
        except ApiException as err:
            print("Exception when calling AccountApi->get_info: %s\n" % err)


def main(argv):
    opsgenie_api_key = ''
    try:
        opts, args = getopt.getopt(argv, "ha:s:")
    except getopt.GetoptError:
        print('account.py -a <apikey>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('account.py -a <apikey>')
            sys.exit()
        elif opt == '-a':
            opsgenie_api_key = arg
    if not opsgenie_api_key:
        print('account.py -a <apikey>')
        sys.exit(2)

    account = Account(opsgenie_api_key)

    metric_observer = MetricObserver()

    api_metric_publisher = account.api_client.api_metric_publisher
    api_metric_publisher.subscribe(metric_observer)

    http_metric_publisher = account.api_client.http_metric_publisher
    http_metric_publisher.subscribe(metric_observer)

    sdk_metric_publisher = account.api_client.sdk_metric_publisher
    sdk_metric_publisher.subscribe(metric_observer)

    print()
    print('Get Account Info:')
    account.get_info()


if __name__ == '__main__':
    main(sys.argv[1:])
