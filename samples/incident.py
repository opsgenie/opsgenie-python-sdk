import getopt
import sys

import opsgenie_sdk
from opsgenie_sdk.metrics.observer import Observer
from opsgenie_sdk.rest import ApiException

class MetricObserver(Observer):
    def notify(self, publisher):
        print("{}: '{}' has now metric data = {}".format(type(self).__name__,
                                                         publisher.name, publisher.data))


class Incident:
    def __init__(self, opsgenie_api_key, opsgenie_service_id):
        self.conf = self.conf = opsgenie_sdk.configuration.Configuration()
        self.conf.api_key['Authorization'] = opsgenie_api_key

        self.conf.debug = False
        # self.conf.logger_file = 'incident_debug.log'
        # self.conf.retry_http_response = ['4xx', '5xx']

        self.api_client = opsgenie_sdk.api_client.ApiClient(configuration=self.conf)
        self.incident_api = opsgenie_sdk.IncidentApi(api_client=self.api_client)

        self.serviceId = opsgenie_service_id

    def create_incident(self):
        body = opsgenie_sdk.CreateIncidentPayload(
            message="Example Incident",
            description="Creating example incident",
            service_id=self.serviceId,
            priority='P5')

        try:
            create_response = self.incident_api.create_incident(create_incident_payload=body)
            print(create_response)
            return create_response
        except ApiException as err:
            print("Exception when calling IncidentApi->create_incident: %s\n" % err)

    def check_request_status(self, request_id):
        try:
            request_response = self.incident_api.get_incident_request_status(request_id)
            print(request_response)
            return request_response
        except ApiException as err:
            print("Exception when calling IncidentApi->get_incident_request_status: %s\n" % err)

    def get_incident(self, incident_id):
        try:
            get_response = self.incident_api.get_incident(incident_id)
            print(get_response)
        except ApiException as err:
            print("Exception when calling IncidentApi->get_incident: %s\n" % err)

    def delete_incident(self, incident_id):
        try:
            delete_response = self.incident_api.delete_incident(incident_id)
            print(delete_response)
        except ApiException as err:
            print("Exception when calling IncidentApi->delete_incident: %s\n" % err)

    def list_incidents(self):
        query = 'status=open'

        try:
            list_response = self.incident_api.list_incidents(query, limit=5)
            print(list_response)
        except ApiException as err:
            print("Exception when calling IncidentApi->list_incidents: %s\n" % err)

    def close_incident(self, incident_id):
        body = opsgenie_sdk.CloseIncidentPayload(note='Example closed')
        try:
            close_response = self.incident_api.close_incident(incident_id, close_incident_payload=body)
            print(close_response)
        except ApiException as err:
            print("Exception when calling IncidentApi->close_incident: %s\n" % err)


def main(argv):
    opsgenie_api_key = ''
    opsgenie_service_id = ''
    try:
        opts, args = getopt.getopt(argv, "ha:s:")
    except getopt.GetoptError:
        print('incident.py -a <apikey> -s <serviceid>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('incident.py -a <apikey> -s <serviceid>')
            sys.exit()
        elif opt == '-a':
            opsgenie_api_key = arg
        elif opt == '-s':
            opsgenie_service_id = arg
    if not opsgenie_api_key:
        print('incident.py -a <apikey> -s <serviceid>')
        sys.exit(2)

    incident = Incident(opsgenie_api_key, opsgenie_service_id)

    metric_observer = MetricObserver()

    api_metric_publisher = incident.api_client.api_metric_publisher
    api_metric_publisher.subscribe(metric_observer)

    http_metric_publisher = incident.api_client.http_metric_publisher
    http_metric_publisher.subscribe(metric_observer)

    sdk_metric_publisher = incident.api_client.sdk_metric_publisher
    sdk_metric_publisher.subscribe(metric_observer)

    print()
    print('Create Incident:')
    response = incident.create_incident()
    request_id = response.request_id

    print()
    print('Retrieve Result:')
    result = response.retrieve_result()
    print(result)

    print()
    print('Retrieve Resulting Action:')
    incident1 = response.retrieve_resulting_action()
    print(incident1)

    incident_id = response.id

    print()
    print('Get Request Status:')
    incident.check_request_status(request_id)

    print()
    print('Get Incident:')
    incident.get_incident(incident_id)

    print()
    print('List Incidents:')
    incident.list_incidents()

    print()
    print('Close Incident:')
    incident.close_incident(incident_id)

    print()
    print('Delete Incident:')
    incident.delete_incident(incident_id)


if __name__ == '__main__':
    main(sys.argv[1:])
