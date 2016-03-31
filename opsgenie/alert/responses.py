from opsgenie.response import BaseResponse
from opsgenie.utility import convert_to_date


class GetAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.tags = self.pop('tags')
        self.count = self.pop('count')
        self.status = self.pop('status')
        self.teams = self.pop('teams')
        self.recipients = self.pop('recipients')
        self.tiny_id = self.pop('tinyId')
        self.alias = self.pop('alias')
        self.entity = self.pop('entity')
        self.id = self.pop('id')
        self.updated_at = convert_to_date(self.pop('updatedAt'))
        self.message = self.pop('message')
        self.details = self.pop('details')
        self.source = self.pop('source')
        self.description = self.pop('description')
        self.created_at = convert_to_date(self.pop('createdAt'))
        self.is_seen = self.pop('isSeen')
        self.acknowledged = self.pop('acknowledged')
        self.owner = self.pop('owner')
        self.actions = self.pop('actions')
        self.system_data = self.pop('systemData')

        self.decode()


class ListAlertsResponse(BaseResponse):
    class AlertResponse:
        def __init__(self, **kwargs):
            self.id = kwargs.get('id')
            self.alias = kwargs.get('alias')
            self.message = kwargs.get('message')
            self.status = kwargs.get('status')
            self.is_seen = kwargs.get('isSeen')
            self.acknowledged = kwargs.get('acknowledged')
            self.created_at = convert_to_date(kwargs.get('createdAt'))
            self.updated_at = convert_to_date(kwargs.get('updatedAt'))
            self.tiny_id = kwargs.get('tinyId')
            self.owner = kwargs.get('owner')

    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.alerts = []
        for alert in self.pop('alerts', []):
            self.alerts.append(ListAlertsResponse.AlertResponse(**alert))

        self.decode()


class ListAlertLogsResponse(BaseResponse):
    class AlertLogResponse:
        def __init__(self, **kwargs):
            self.log = kwargs.get('log')
            self.log_type = kwargs.get('logType')
            self.owner = kwargs.get('owner')
            self.created_at = convert_to_date(kwargs.get('createdAt'))

    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.logs = []
        for log in self.pop('logs', []):
            self.logs.append(ListAlertLogsResponse.AlertLogResponse(**log))

        self.lastKey = self.pop('lastKey')

        self.decode()


class ListAlertNotesResponse(BaseResponse):
    class AlertNoteResponse:
        def __init__(self, **kwargs):
            self.note = kwargs.get('note')
            self.owner = kwargs.get('owner')
            self.created_at = convert_to_date(kwargs.get('createdAt'))

    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.took = self.pop('took')
        self.last_key = self.pop('lastKey')
        self.notes = []
        for note in self.pop('notes', []):
            self.notes.append(ListAlertNotesResponse.AlertNoteResponse(**note))

        self.decode()


class ListAlertRecipientsResponse(BaseResponse):
    class UserResponse:
        def __init__(self, **kwargs):
            self.username = kwargs.get('username')
            self.state = kwargs.get('state')
            self.method = kwargs.get('method')
            self.state_changed_at = convert_to_date(kwargs.get('stateChangedAt'))

    class GroupResponse:
        def __init__(self, **kwargs):
            self.username = kwargs.get('username')
            self.state = kwargs.get('state')
            self.method = kwargs.get('method')
            self.state_changed_at = convert_to_date(kwargs.get('stateChangedAt'))

    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.users = []
        for user in self.pop('users', []):
            self.users.append(ListAlertRecipientsResponse.UserResponse(**user))

        self.groups = []
        for group in self.pop('groups', []):
            self.groups.append(ListAlertRecipientsResponse.GroupResponse(**group))

        self.decode()


class CreateAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.message = self.pop('message')
        self.alert_id = self.pop('alertId')
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class CloseAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class DeleteAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class CountAlertsResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.count = self.pop('count')

        self.decode()


class AcknowledgeAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class SnoozeAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class RenotifyAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class TakeOwnershipOfAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class AssignOwnerToAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class AddTeamToAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class AddRecipientToAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class AddNoteToAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class AddTagsToAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class RemoveTagsFromAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class AddDetailsToAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class RemoveDetailsFromAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class ExecuteActionOfAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()


class AttachFileToAlertResponse(BaseResponse):
    def __init__(self, json_str):
        BaseResponse.__init__(self, json_str)
        self.status = self.pop('status')
        self.code = self.pop('code')

        self.decode()
