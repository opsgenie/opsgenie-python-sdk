from __future__ import print_function

from pprint import pprint

from opsgenie.swagger_client import AlertApi
from opsgenie.swagger_client import configuration
from opsgenie.swagger_client.models import *
from opsgenie.swagger_client.rest import ApiException

REQUEST_ID = "YOUR_REQUEST_ID"
API_KEY = "YOUR_API_KEY"
IDENTIFIER = "YOUR_ALERT_IDENTIFIER"
IDENTIFIER_TYPE = "YOUR_ALERT_IDENTIFIER_TYPE"


def setup_opsgenie_client():
    configuration.api_key['Authorization'] = API_KEY
    configuration.api_key_prefix['Authorization'] = 'GenieKey'
    # Provides more detailed request
    # configuration.debug = True


def get_request_status():
    setup_opsgenie_client()

    try:
        response = AlertApi().get_request_status(request_id=REQUEST_ID)

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        # Refer to GetRequestStatusResponse for more detailed data
        print('data.alert_id: {}'.format(response.data.alert_id))
        print('data.alias: {}'.format(response.data.alias))
        print('data.integration_id: {}'.format(response.data.integration_id))
        print('data.is_success: {}'.format(response.data.is_success))
        print('data.processed_at: {}'.format(response.data.processed_at))
        print('data.action: {}'.format(response.data.action))
        print('data.status: {}'.format(response.data.status))
    except ApiException as err:
        print("Exception when calling AlertApi->get_request_status: %s\n" % err)


def create_alert():
    setup_opsgenie_client()

    body = CreateAlertRequest(
        message='AppServer1 is down!',
        alias='Tron',
        description='CPU usage is over 87%',
        teams=[TeamRecipient(name='OperationTeam'), TeamRecipient(name="NetworkTeam")],
        visible_to=[TeamRecipient(name='NetworkTeam', type='team')],
        actions=['ping', 'restart'],
        tags=['network', 'operations', 'gomtan'],
        entity='ApppServer1',
        priority='P4',
        user='user@opsgenie.com',
        note='Alert created')

    try:
        response = AlertApi().create_alert(body=body)

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('result: {}'.format(response.result))
    except ApiException as err:
        print("Exception when calling AlertApi->create_alert: %s\n" % err)


def close_alert():
    setup_opsgenie_client()

    body = CloseAlertRequest(
        source='System',
        user='user@opsgenie.com',
        note='Alert was unnecessary, closed by System')

    try:
        response = AlertApi().close_alert(identifier=IDENTIFIER, identifier_type=IDENTIFIER_TYPE, body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->close_alert: %s\n" % err)


def delete_alert():
    setup_opsgenie_client()

    try:
        response = AlertApi().delete_alert(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            source='System',
            user='user@opsgenie.com')

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('result: {}'.format(response.result))
    except ApiException as err:
        print("Exception when calling AlertApi->delete_alert: %s\n" % err)


def get_alert():
    setup_opsgenie_client()

    try:
        # Default identifier_type is id
        response = AlertApi().get_alert(identifier=IDENTIFIER, identifier_type=IDENTIFIER_TYPE)

        # Refer to GetAlertResponse for more detailed data
        print(response)
        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('data.acknowledged: {}'.format(response.data.acknowledged))
        print('data.actions: {}'.format(response.data.actions))
        print('data.alias: {}'.format(response.data.alias))
        print('data.count: {}'.format(response.data.count))
        print('data.created_at: {}'.format(response.data.created_at))
        print('data.description: {}'.format(response.data.description))
        print('data.details: {}'.format(response.data.details))
        print('data.entity: {}'.format(response.data.entity))
        print('data.id: {}'.format(response.data.id))
        print('data.integration: {}'.format(response.data.integration))
        print('data.is_seen: {}'.format(response.data.is_seen))
        print('data.last_occurred_at: {}'.format(response.data.last_occurred_at))
        print('data.message: {}'.format(response.data.message))
        print('data.owner: {}'.format(response.data.owner))
        print('data.priority: {}'.format(response.data.priority))
        print('data.report: {}'.format(response.data.report))
        print('data.snoozed: {}'.format(response.data.snoozed))
        print('data.snoozed_until: {}'.format(response.data.snoozed_until))
        print('data.source: {}'.format(response.data.source))
        print('data.status: {}'.format(response.data.status))
        print('data.tags: {}'.format(response.data.tags))
        print('data.teams: {}'.format(response.data.teams))
        print('data.tiny_id: {}'.format(response.data.tiny_id))
        print('data.updated_at: {}'.format(response.data.updated_at))
    except ApiException as err:
        print("Exception when calling AlertApi->get_alert: %s\n" % err)


def list_alerts():
    setup_opsgenie_client()

    try:
        # Default identifier_type is id
        response = AlertApi().list_alerts(
            limit=25,
            query='status: open',
            order='desc',
            sort='createdAt')

        # Refer to ListAlertsResponse for more detailed data
        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        for alert_response in response.data:
            print('alert_response.id: {}'.format(alert_response.id))
            print('alert_response.tiny_id: {}'.format(alert_response.tiny_id))
            print('alert_response.alias: {}'.format(alert_response.alias))
            print('alert_response.message: {}'.format(alert_response.message))
            print('alert_response.status: {}'.format(alert_response.status))
            print('alert_response.acknowledged: {}'.format(alert_response.acknowledged))
            print('alert_response.is_seen: {}'.format(alert_response.is_seen))
            print('alert_response.tags: {}'.format(alert_response.tags))
            print('alert_response.snoozed: {}'.format(alert_response.snoozed))
            print('alert_response.snoozed_until: {}'.format(alert_response.snoozed_until))
            print('alert_response.count: {}'.format(alert_response.count))
            print('alert_response.last_occurred_at: {}'.format(alert_response.last_occurred_at))
            print('alert_response.created_at: {}'.format(alert_response.created_at))
            print('alert_response.updated_at: {}'.format(alert_response.updated_at))
            print('alert_response.source: {}'.format(alert_response.source))
            print('alert_response.owner: {}'.format(alert_response.owner))
            print('alert_response.priority: {}'.format(alert_response.priority))
            print('alert_response.teams: {}'.format(alert_response.teams))
            print('alert_response.integration: {}'.format(alert_response.integration))
            print('alert_response.report: {}'.format(alert_response.report))
    except ApiException as err:
        print("Exception when calling AlertApi->list_alerts: %s\n" % err)


def acknowledge_alert():
    setup_opsgenie_client()

    body = AcknowledgeAlertRequest(
        source='System',
        user='user@opsgenie.com',
        note='Alert was unnecessary, acknowledged by System')

    try:
        response = AlertApi().acknowledge_alert(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('result: {}'.format(response.result))
    except ApiException as err:
        print("Exception when calling AlertApi->acknowledge_alert: %s\n" % err)


def unacknowledge_alert():
    setup_opsgenie_client()

    body = UnAcknowledgeAlertRequest(
        source='System',
        user='user@opsgenie.com',
        note='Alert was necessary, unacknowledged by System')

    try:
        response = AlertApi().un_acknowledge_alert(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->unacknowledge_alert: %s\n" % err)


def snooze_alert():
    setup_opsgenie_client()

    body = SnoozeAlertRequest(
        source='System',
        user='user@opsgenie.com',
        note='Snoozed because of vacation by System',
        end_time='2017-02-06T05:00:00Z')

    try:
        response = AlertApi().snooze_alert(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->snooze_alert: %s\n" % err)


def escalate_alert_to_next():
    setup_opsgenie_client()

    body = EscalateAlertToNextRequest(
        source='System',
        user='user@opsgenie.com',
        note='Escalated',
        escalation=EscalationRecipient(id='39d50168-24b3-4355-b285-b91060823dee'))

    try:
        response = AlertApi().escalate_alert(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->escalate_alert_to_next: %s\n" % err)


def assign_alert():
    setup_opsgenie_client()

    body = AssignAlertRequest(
        source='System',
        user='user@opsgenie.com',
        note='Assigned',
        owner=UserRecipient(username='user@opsgenie.com'))

    try:
        response = AlertApi().assign_alert(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->assign_alert: %s\n" % err)


def add_alert_note():
    setup_opsgenie_client()

    body = AddAlertNoteRequest(
        source='HR',
        user='user@opsgenie.com',
        note='We should find another solution.')

    try:
        response = AlertApi().add_note(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->add_alert_note: %s\n" % err)


def add_alert_tags():
    setup_opsgenie_client()

    body = AddAlertTagsRequest(
        source='Server',
        user='user@opsgenie.com',
        note='We should find another tag.',
        tags=['support', 'network'])

    try:
        response = AlertApi().add_tags(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->add_alert_tags: %s\n" % err)


def remove_alert_tags():
    setup_opsgenie_client()

    try:
        response = AlertApi().delete_tags(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            user='user@opsgenie.com',
            tags=['support', 'network'],
            note='Unnecessary tags are removed.',
            source='Server')

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->remove_alert_tags: %s\n" % err)


def add_alert_team():
    setup_opsgenie_client()

    body = AddAlertTeamRequest(
        team=TeamRecipient(name='OperationTeam'),
        source='System',
        note='Team is added',
        user='user@opsgenie.com')

    try:
        response = AlertApi().add_team(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->add_alert_team: %s\n" % err)


def add_alert_details():
    setup_opsgenie_client()

    body = AddAlertDetailsRequest(
        user='user@opsgenie.com',
        note='Add these details to document',
        source='HR',
        details={'prop1': 'val1', 'prop2': 'val2'})

    try:
        response = AlertApi().add_details(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->add_alert_details: %s\n" % err)


def remove_alert_details():
    setup_opsgenie_client()

    try:
        response = AlertApi().delete_details(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            user='user@opsgenie.com',
            note='Remove unrelated details.',
            source='System',
            keys=['prop1', 'prop2'])

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->remove_alert_details: %s\n" % err)


def execute_custom_alert_action():
    setup_opsgenie_client()

    body = ExecuteCustomAlertActionRequest(
        user='user@opsgenie.com',
        note='"Executing rebase action"',
        source='Automation',
    )

    try:
        response = AlertApi().execute_custom_action(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            action_name='rebase',
            body=body)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->execute_custom_alert_action: %s\n" % err)


def list_alert_recipients():
    setup_opsgenie_client()

    try:
        response = AlertApi().list_recipients(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE)

        # Refer to ListAlertRecipientsResponse for more detailed data
        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        for alert_response in response.data:
            print('alert_response.created_at: {}'.format(alert_response.created_at))
            print('alert_response.method: {}'.format(alert_response.method))
            print('alert_response.state: {}'.format(alert_response.state))
            print('alert_response.updated_at: {}'.format(alert_response.updated_at))
            print('alert_response.user: {}'.format(alert_response.user))
    except ApiException as err:
        print("Exception when calling AlertApi->list_recipients: %s\n" % err)


def list_alert_logs():
    setup_opsgenie_client()

    try:
        response = AlertApi().list_logs(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            limit=50,
            order='asc',
            direction='next')

        # Refer to ListAlertLogsResponse for more detailed data
        print('request id: {}'.format(response.request_id))
        print('paging: {}'.format(response.paging))
        print('took: {}'.format(response.took))
        for alert_log_response in response.data:
            print('alert_log_response.log: {}'.format(alert_log_response.log))
            print('alert_log_response.type: {}'.format(alert_log_response.type))
            print('alert_log_response.owner: {}'.format(alert_log_response.owner))
            print('alert_log_response.created_at: {}'.format(alert_log_response.created_at))
            print('alert_log_response.offset: {}'.format(alert_log_response.offset))
    except ApiException as err:
        print("Exception when calling AlertApi->list_alert_logs: %s\n" % err)


def list_alert_notes():
    setup_opsgenie_client()

    try:
        response = AlertApi().list_notes(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE,
            limit=50,
            order='asc',
            direction='next')

        # Refer to ListAlertNotesResponse for more detailed data
        print('request id: {}'.format(response.request_id))
        print('paging: {}'.format(response.paging))
        print('took: {}'.format(response.took))
        for alert_notes_response in response.data:
            print('alert_notes_response.note: {}'.format(alert_notes_response.note))
            print('alert_notes_response.owner: {}'.format(alert_notes_response.owner))
            print('alert_notes_response.created_at: {}'.format(alert_notes_response.created_at))
            print('alert_notes_response.offset: {}'.format(alert_notes_response.offset))
    except ApiException as err:
        print("Exception when calling AlertApi->list_alert_notes: %s\n" % err)


def add_saved_search():
    setup_opsgenie_client()

    body = AddSavedSearchRequest(
        name='My Saved Search',
        description='Saved search for open alerts',
        query='status: open',
        owner=UserRecipient(username='user@opsgenie.com'))

    try:
        response = AlertApi().add_saved_searches(body)

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('data.id: {}'.format(response.data.id))
        print('data.name: {}'.format(response.data.name))
    except ApiException as err:
        print("Exception when calling AlertApi->add_saved_search: %s\n" % err)


def get_saved_search():
    setup_opsgenie_client()

    try:
        response = AlertApi().get_saved_search(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE)

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('data.id: {}'.format(response.data.id))
        print('data.name: {}'.format(response.data.name))
        print('data.created_at: {}'.format(response.data.created_at))
        print('data.updated_at: {}'.format(response.data.updated_at))
        print('data.owner: {}'.format(response.data.owner))
        print('data.teams: {}'.format(response.data.teams))
        print('data.description: {}'.format(response.data.description))
        print('data.query: {}'.format(response.data.query))
    except ApiException as err:
        print("Exception when calling AlertApi->get_saved_search: %s\n" % err)


def delete_saved_search():
    setup_opsgenie_client()

    try:
        response = AlertApi().delete_saved_search(
            identifier=IDENTIFIER,
            identifier_type=IDENTIFIER_TYPE)

        pprint(response)
    except ApiException as err:
        print("Exception when calling AlertApi->delete_saved_search: %s\n" % err)


def list_saved_search():
    setup_opsgenie_client()

    try:
        response = AlertApi().list_saved_searches()

        # Refer to ListSavedSearchResponse for more detailed data
        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        for saved_search_response in response.data:
            print('saved_search_response.id: {}'.format(saved_search_response.id))
            print('saved_search_response.name: {}'.format(saved_search_response.name))

    except ApiException as err:
        print("Exception when calling AlertApi->list_saved_search: %s\n" % err)
