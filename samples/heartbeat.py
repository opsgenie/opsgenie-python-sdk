import getopt
import sys

import opsgenie_sdk
from opsgenie_sdk.api.heartbeat.create_heartbeat_payload_all_of_owner_team import CreateHeartbeatPayloadAllOfOwnerTeam
from opsgenie_sdk.metrics.observer import Observer
from opsgenie_sdk.rest import ApiException


class MetricObserver(Observer):
    def notify(self, publisher):
        print("{}: '{}' has now metric data = {}".format(type(self).__name__,
                                                         publisher.name, publisher.data))


class HeartBeat:
    heartbeat_name = 'PythonSDK'

    def __init__(self, opsgenie_api_key):
        self.conf = opsgenie_sdk.configuration.Configuration()
        self.conf.api_key['Authorization'] = opsgenie_api_key

        self.conf.debug = False
        # self.conf.logger_file = 'heartbeat_debug.log'

        self.api_client = opsgenie_sdk.api_client.ApiClient(configuration=self.conf)
        self.heartbeat_api = opsgenie_sdk.HeartbeatApi(api_client=self.api_client)

    def ping(self):
        try:
            response = self.heartbeat_api.ping(self.heartbeat_name)
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->ping: %s\n" % err)

    def get(self):
        try:
            response = self.heartbeat_api.get_heartbeat(self.heartbeat_name)
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->get: %s\n" % err)

    def add(self):
        owner_team = CreateHeartbeatPayloadAllOfOwnerTeam(name='tardis_team')
        body = opsgenie_sdk.CreateHeartbeatPayload(name=self.heartbeat_name,
                                                   description='Created via the python sdk',
                                                   interval=5,
                                                   owner_team=owner_team,
                                                   interval_unit='minutes',
                                                   enabled=True,
                                                   alert_message='testingPythonSDK',
                                                   alert_tags=['tag1'],
                                                   alert_priority='P2')
        try:
            response = self.heartbeat_api.create_heartbeat(create_heartbeat_payload=body)
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->add: %s\n" % err)

    def delete(self):
        try:
            response = self.heartbeat_api.delete_heartbeat(self.heartbeat_name)
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->delete: %s\n" % err)

    def update(self):
        body = opsgenie_sdk.UpdateHeartbeatPayload(description='Updated' + self.heartbeat_name)
        try:
            response = self.heartbeat_api.update_heartbeat(name=self.heartbeat_name, update_heartbeat_payload=body)
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->update: %s\n" % err)

    def disable(self):
        try:
            response = self.heartbeat_api.disable_heartbeat(self.heartbeat_name)
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->disable: %s\n" % err)

    def enable(self):
        try:
            response = self.heartbeat_api.enable_heartbeat(self.heartbeat_name)
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->enable: %s\n" % err)

    def list(self):
        try:
            response = self.heartbeat_api.list_heart_beats()
            print(response)
        except ApiException as err:
            print("Exception when calling HeartBeatApi->list: %s\n" % err)


def main(argv):
    opsgenie_api_key = ''
    try:
        opts, args = getopt.getopt(argv, "ha:")
    except getopt.GetoptError:
        print('heartbeat.py -a <apikey>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('heartbeat.py -a <apikey>')
            sys.exit()
        elif opt == '-a':
            opsgenie_api_key = arg
    if not opsgenie_api_key:
        print('heartbeat.py -a <apikey>')
        sys.exit(2)

    heartbeat = HeartBeat(opsgenie_api_key)

    metric_observer = MetricObserver()

    api_metric_publisher = heartbeat.api_client.api_metric_publisher
    api_metric_publisher.subscribe(metric_observer)

    http_metric_publisher = heartbeat.api_client.http_metric_publisher
    http_metric_publisher.subscribe(metric_observer)

    sdk_metric_publisher = heartbeat.api_client.sdk_metric_publisher
    sdk_metric_publisher.subscribe(metric_observer)

    print('Add HeartBeat:')
    heartbeat.add()

    print()

    print('Ping HeartBeat:')
    heartbeat.ping()

    print()

    print('Get HeartBeat:')
    heartbeat.get()

    print()

    print('Update HeartBeat')
    heartbeat.update()

    print()

    print('Disable HeartBeat')
    heartbeat.disable()

    print()

    print('Enable HeartBeat')
    heartbeat.enable()

    print()

    print('List HeartBeat')
    heartbeat.list()

    print()

    print('Delete HeartBeat')
    heartbeat.delete()


if __name__ == '__main__':
    main(sys.argv[1:])
