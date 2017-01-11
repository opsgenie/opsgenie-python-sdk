from __future__ import print_function
from opsgenie import OpsGenie
from opsgenie.alert.requests import *
from opsgenie.config import Configuration
from opsgenie.errors import OpsGenieError
from samples import random_str

API_KEY = "YOUR_API_KEY"
TEAM_NAME = "YOUR_TEAM_NAME"
OWNER = "YOUR_USERNAME"
ESCALATION_NAME = "YOUR_ESCALATION_NAME"
FILE_PATH = "FILE_PATH_TO_SEND"
SOURCE = "PYTHON API"
ACTIONS = ["ACTION1", "ACTION2"]
ACTION_TO_EXECUTE = ACTIONS[0]


def setup_opsgenie_client():
    config = Configuration(apikey=API_KEY)
    return OpsGenie(config)


def create_alert(client):
    # Create Alert
    response = client.alert.create_alert(CreateAlertRequest(message=random_str(8, 'Test')))
    print("message: ", (response.message))
    print("alert id: ", (response.alert_id))
    print("status: ", (response.status))
    print("code: ", (response.code))

    return response


def alert_create_acknowledge():
    print("\n alert_create_acknowledge")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Acknowledge Alert
        ack_response = client.alert.acknowledge_alert(AcknowledgeAlertRequest(id=response.alert_id))
        print("status: ", (ack_response.status))
        print("code: ", (ack_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_unacknowledge():
    print("\n alert_create_unacknowledge")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Acknowledge Alert
        ack_response = client.alert.acknowledge_alert(AcknowledgeAlertRequest(id=response.alert_id))
        print("Acknowledge status: ", (ack_response.status))
        print("Acknowledge code: ", (ack_response.code))

        # UnAcknowledge Alert
        unack_response = client.alert.unacknowledge_alert(UnAcknowledgeAlertRequest(id=response.alert_id))
        print("status: ", (unack_response.status))
        print("code: ", (unack_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_addnote_listnotes():
    print("\n alert_create_addnote_listnotes")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Add 10 Note to Alert
        for i in range(10):
            request = AddNoteToAlertRequest(response.alert_id, note=random_str(45))
            add_note_response = client.alert.add_note_to_alert(request)
            print("[Add note] ", (add_note_response.status), (add_note_response.code))

        # List Notes of Alert
        list_notes_response = client.alert.list_alert_notes(ListAlertNotesRequest(response.alert_id))
        print("Last Key: ", (list_notes_response.last_key))
        print("Notes: \n --------")

        for note in list_notes_response.notes:
            print("Note: ", (note.note))
            print("Owner: ", (note.owner))
            print("Created At: ", (note.created_at))
            print("------------------")

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_addrecipient():
    print("\n alert_create_addrecipient")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Add Recipient
        add_recipient_response = client.alert.add_recipient_to_alert(
            AddRecipientToAlertRequest(id=response.alert_id, recipient="recipient"))
        print("status: ", (add_recipient_response.status))
        print("code: ", (add_recipient_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_addtags():
    print("\n alert_create_addtags")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Add Tags
        add_tags_response = client.alert.add_tags_to_alert(
            AddTagsToAlertRequest(id=response.alert_id, tags=["tag1", "tag2"]))
        print("status: ", (add_tags_response.status))
        print("code: ", (add_tags_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_addteam():
    print("\n alert_create_addteam")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Add Team
        add_team_response = client.alert.add_team_to_alert(
            AddTeamToAlertRequest(id=response.alert_id, team=TEAM_NAME))
        print("status: ", (add_team_response.status))
        print("code: ", (add_team_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_assignowner():
    print("\n alert_create_assignowner")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Assign Owner
        assign_owner_response = client.alert.assign_owner_to_alert(
            AssignOwnerToAlertRequest(id=response.alert_id, owner=OWNER))
        print("status: ", (assign_owner_response.status))
        print("code: ", (assign_owner_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_attachfile():
    print("\n alert_create_attachfile")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Attach File
        attach_file_response = client.alert.attach_file_to_alert(
            AttachFileToAlertRequest(id=response.alert_id, attachment=FILE_PATH))
        print("status: ", (attach_file_response.status))
        print("code: ", (attach_file_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_close():
    print("\n alert_create_close")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Close Alert
        close_alert_response = client.alert.close_alert(CloseAlertRequest(id=response.alert_id))
        print("status: ", (close_alert_response.status))
        print("code: ", (close_alert_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_delete():
    print("\n alert_create_delete")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Delete Alert
        delete_alert_response = client.alert.delete_alert(DeleteAlertRequest(id=response.alert_id, source=SOURCE))
        print("status: ", (delete_alert_response.status))
        print("code: ", (delete_alert_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_executeaction():
    print("\n alert_create_executeaction")
    client = setup_opsgenie_client()

    try:
        response = client.alert.create_alert(CreateAlertRequest(message=random_str(10, "Test"), actions=ACTIONS))

        # Execute Action
        execute_action_response = client.alert.execute_action_of_alert(
            ExecuteActionOfAlertRequest(id=response.alert_id, action=ACTION_TO_EXECUTE,
                                        note="Action {} executed by Python API".format(ACTION_TO_EXECUTE)))
        print("status: ", (execute_action_response.status))
        print("code: ", (execute_action_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_get():
    print("\n alert_create_get")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Get Alert
        get_alert_response = client.alert.get_alert(GetAlertRequest(id=response.alert_id))
        print("tags: ", (list_to_str(get_alert_response.tags)))
        print("count: ", (get_alert_response.count))
        print("teams: ", (list_to_str(get_alert_response.teams)))
        print("recipients: ", (list_to_str(get_alert_response.recipients)))
        print("tiny id: ", (get_alert_response.tiny_id))
        print("alias: ", (get_alert_response.alias))
        print("entity: ", (get_alert_response.entity))
        print("id: ", (get_alert_response.id))
        print("updated at: ", (get_alert_response.updated_at))
        print("message: ", (get_alert_response.message))
        print("details: ", (get_alert_response.details))
        print("source: ", (get_alert_response.source))
        print("description: ", (get_alert_response.description))
        print("created at: ", (get_alert_response.created_at))
        print("is seen: ", (get_alert_response.is_seen))
        print("acknowledged: ", (get_alert_response.acknowledged))
        print("owner: ", (get_alert_response.owner))
        print("system data: ", (get_alert_response.system_data))
        print("actions: ", (list_to_str(get_alert_response.actions)))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_listlogs():
    print("\n alert_create_listlogs")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # List Logs of Alert
        list_logs_response = client.alert.list_alert_logs(ListAlertLogsRequest(response.alert_id))

        for log in list_logs_response.logs:
            print("Owner: ", (log.owner))
            print("Log: ", (log.log))
            print("Log Type: ", (log.log_type))
            print("Created At: ", (log.created_at))
            print("------------------")

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_listrecipients():
    print("\n alert_create_listrecipients")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # List Recipients of Alert
        list_recipients_response = client.alert.list_alert_recipients(ListAlertRecipientsRequest(response.alert_id))

        print("Users: ", (list_to_str([u.username for u in list_recipients_response.users])))
        print("Groups: ", (list_to_str([u.username for u in list_recipients_response.groups])))
    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_renotify():
    print("\n alert_create_renotify")
    client = setup_opsgenie_client()

    try:
        response = client.alert.create_alert(CreateAlertRequest(message=random_str(10, "Test"), actions=ACTIONS))

        # Renotify Alert
        renotify_response = client.alert.renotify_alert(RenotifyAlertRequest(id=response.alert_id))
        print("status: ", (renotify_response.status))
        print("code: ", (renotify_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_takeownership():
    print("\n alert_create_takeownership")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Take ownership of Alert
        renotify_response = client.alert.take_ownership_of_alert(TakeOwnershipOfAlertRequest(id=response.alert_id))
        print("status: ", (renotify_response.status))
        print("code: ", (renotify_response.code))

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_listalerts():
    print("\n alert_create_listalerts")
    client = setup_opsgenie_client()

    try:
        # List Alerts
        list_alerts_response = client.alert.list_alerts(ListAlertsRequest())

        for alert in list_alerts_response.alerts:
            print("Id: ", alert.id)
            print("Alias: ", alert.alias)
            print("Message: ", alert.message)
            print("Status: ", alert.status)
            print("IsSeen: ", alert.is_seen)
            print("Acknowledged: ", alert.acknowledged)
            print("Created at: ", alert.created_at)
            print("Updated at: ", alert.updated_at)
            print("Tiny id: ", alert.tiny_id)
            print("Owner: ", alert.owner)
            print("------------------")

    except OpsGenieError as err:
        print("[ERROR]", err.message)


def alert_create_escalatetonext():
    print("\n alert_create_escalatetonext")
    client = setup_opsgenie_client()

    try:
        response = create_alert(client)

        # Add Recipient To Alert
        add_recipient_response = client.alert.add_recipient_to_alert(
            AddRecipientToAlertRequest(id=response.alert_id, recipient="recipient"))
        print("Recipient status: ", (add_recipient_response.status))
        print("Recipient code: ", (add_recipient_response.code))

        # Escalate To Next
        escalate_to_next_response = client.alert.escalate_to_next(EscalateToNextAlertRequest(id=response.alert_id, escalation_name=ESCALATION_NAME))

        print("status: ", escalate_to_next_response.status)
        print("code: ", escalate_to_next_response.code)

    except OpsGenieError as err:
        print("[ERROR]", err.message)


#alert_create_escalatetonext()
#alert_create_unacknowledge()
# alert_create_addnote_listnotes()
# alert_create_addrecipient()
# alert_create_addtags()
# alert_create_addteam()
# alert_create_assignowner()
# alert_create_attachfile()
# alert_create_close()
# alert_create_delete()
# alert_create_executeaction()
# alert_create_get()
# alert_create_listalerts()
# alert_create_listlogs()
# alert_create_listrecipients()
# alert_create_renotify()
# alert_create_takeownership()
