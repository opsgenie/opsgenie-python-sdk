import getopt
import sys

import opsgenie_sdk
from opsgenie_sdk.metrics.observer import Observer
from opsgenie_sdk.rest import ApiException


class MetricObserver(Observer):
    def notify(self, publisher):
        print("{}: '{}' has now metric data = {}".format(type(self).__name__,
                                                         publisher.name, publisher.data))


class Alert:
    def __init__(self, opsgenie_api_key):
        self.conf = self.conf = opsgenie_sdk.configuration.Configuration()
        self.conf.api_key['Authorization'] = opsgenie_api_key

        self.conf.debug = False

        self.conf.retry_count = 5
        self.conf.retry_http_response = ['4xx', '5xx']
        self.conf.retry_delay = 2
        self.conf.retry_enabled = True

        self.api_client = opsgenie_sdk.api_client.ApiClient(configuration=self.conf)
        self.alert_api = opsgenie_sdk.AlertApi(api_client=self.api_client)

    def create_alert(self):
        body = opsgenie_sdk.CreateAlertPayload(
            message="Example Closed",
            description="Creating example alert",
            priority='P5',
        )

        try:
            create_response = self.alert_api.create_alert(create_alert_payload=body)
            print(create_response)
            return create_response
        except ApiException as err:
            print("Exception when calling AlertApi->create_alert: %s\n" % err)

    def check_request_status(self, request_id):
        try:
            request_response = self.alert_api.get_request_status(request_id)
            print(request_response)
            return request_response
        except ApiException as err:
            print("Exception when calling AlertApi->get__request_status: %s\n" % err)

    def get_alert(self, alert_id):

        try:
            alert_response = self.alert_api.get_alert(identifier=alert_id, identifier_type='id')
            print(alert_response)
            return alert_response
        except ApiException as err:
            print("Exception when calling AlertApi->get_alert: %s\n" % err)

    def count_alerts(self):
        try:
            count_response = self.alert_api.count_alerts()
            print(count_response)
            return count_response
        except ApiException as err:
            print("Exception when calling AlertApi->count__alerts: %s\n" % err)

    def list_alerts(self):
        query = 'status=open'
        try:
            list_response = self.alert_api.list_alerts(query=query)
            print(list_response)
            return list_response
        except ApiException as err:
            print("Exception when calling AlertApi->list_alerts: %s\n" % err)

    def acknowledge_alert(self, alert_id):
        body = opsgenie_sdk.AcknowledgeAlertPayload(note='Example Acknowledged')
        try:
            acknowledge_response = self.alert_api.acknowledge_alert(identifier=alert_id, acknowledge_alert_payload=body)
            print(acknowledge_response)
            return acknowledge_response
        except ApiException as err:
            print("Exception when calling AlertApi->acknowledge_alerts: %s\n" % err)

    def snooze_alert(self, alert_id):
        body = opsgenie_sdk.SnoozeAlertPayload(end_time="2030-04-03T20:05:50.894Z")
        try:
            snooze_response = self.alert_api.snooze_alert(identifier=alert_id, snooze_alert_payload=body)
            print(snooze_response)
            return snooze_response
        except ApiException as err:
            print("Exception when calling AlertApi->snooze_alerts: %s\n" % err)

    def escalate_alert(self, alert_id):
        body = opsgenie_sdk.EscalateAlertToNextPayload()

    def close_alert(self, alert_id):
        body = opsgenie_sdk.CloseAlertPayload(note='Example Closed')
        try:
            close_response = self.alert_api.close_alert(identifier=alert_id, close_alert_payload=body)
            print(close_response)
            return close_response
        except ApiException as err:
            print("Exception when calling AlertApi->close_alerts: %s\n" % err)

    def delete_alert(self, alert_id):
        try:
            delete_response = self.alert_api.delete_alert(identifier=alert_id, identifier_type='id')
            print(delete_response)
            return delete_response
        except ApiException as err:
            print("Exception when calling AlertApi->delete_response: %s\n" % err)



def main(argv):
    opsgenie_api_key = ''
    try:
        opts, args = getopt.getopt(argv, "ha:s:")
    except getopt.GetoptError:
        print('alert.py -a <apikey>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('alert.py -a <apikey>')
            sys.exit()
        elif opt == '-a':
            opsgenie_api_key = arg
    if not opsgenie_api_key:
        print('alert.py -a <apikey>')
        sys.exit(2)

    alert = Alert(opsgenie_api_key)

    metric_observer = MetricObserver()

    api_metric_publisher = alert.api_client.api_metric_publisher
    api_metric_publisher.subscribe(metric_observer)

    http_metric_publisher = alert.api_client.http_metric_publisher
    http_metric_publisher.subscribe(metric_observer)

    sdk_metric_publisher = alert.api_client.sdk_metric_publisher
    sdk_metric_publisher.subscribe(metric_observer)

    print()
    print('Create Alert:')
    response = alert.create_alert()

    alert_id = response.id

    print()
    print('Retrieve Result:')
    result = response.retrieve_result()
    print(result)

    print()
    print('Retrieve Resulting Action:')
    alert1 = response.retrieve_resulting_action()
    print(alert1)

    print()
    print('Get Alert:')
    alert.get_alert(alert_id)

    print()
    print('Count Alerts:')
    alert.count_alerts()

    print()
    print('List Alerts:')
    alert.list_alerts()

    print()
    print('Snooze Alert:')
    alert.snooze_alert(alert_id)

    # print()
    # print('Acknowledge Alert')
    # alert.acknowledge_alert(alert)

    print()
    print('Close Alert:')
    alert.close_alert(alert_id)

    print()
    print('Delete Alert')
    alert.delete_alert(alert_id)


if __name__ == '__main__':
    main(sys.argv[1:])
