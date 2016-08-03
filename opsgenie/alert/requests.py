from opsgenie.request import BaseRequest, required_one_of, should_be_one_of, max_value, required
from opsgenie.utility import list_to_str, format_date, convert_from_date


class GetAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, tiny_id=None):
        """
        Used to hold required parameters of Get Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#getAlertRequest

        One of the [id, alias, tinyId] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        tiny_id : int, optional
            Short id assigned to the alert. All requests supports tinyId but using this field is not recommended.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.tiny_id = tiny_id

    @required_one_of(["id", "alias", "tiny_id"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'tinyId': self.tiny_id
        }


class ListAlertsRequest(BaseRequest):
    def __init__(self, created_after=None, created_before=None, updated_after=None, updated_before=None, limit=None,
                 status=None, sort_by=None, order=None, tags=None, tags_operator=None):
        """
        Used to hold required parameters of List Alerts Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#listAlertRequest

        Parameters
        ----------
        created_after : datetime, optional
            UTC datetime. Filter alerts created after specified time.
        created_before : datetime, optional
            UTC datetime. Filter alerts created before specified time.
        updated_after : datetime, optional
            UTC datetime. Filter alerts updated after specified time.
        updated_before : datetime, optional
            UTC datetime. Filter alerts updated before specified time.
        limit : int, optional
            Page size. (Default is 20, Max is 100)
        status : {'open', 'acked', 'unacked', 'seen', 'notseen', 'closed'}
            Unix timestamp in nanoseconds. Filter alerts with status.
        sort_by : {'createdAt', 'updatedAt'}, optional
            Sort result set using specified parameter. Default is 'createdAt'
        order : {'asc', 'desc'}, optional
            Sort order of the result set. Default is 'desc'
        tags : list of str, optional
            List of tags to be used to filter alerts.
        tags_operator : {'and', 'or'}, optional
            Operator of filtering alerts using tags. Default is and
        """
        BaseRequest.__init__(self)
        self.created_after = created_after
        self.created_before = created_before
        self.updated_after = updated_after
        self.updated_before = updated_before
        self.limit = limit
        self.status = status
        self.sort_by = sort_by
        self.order = order
        self.tags = tags
        self.tags_operator = tags_operator

    @max_value("limit", 100)
    @should_be_one_of("status", ["open", "acked", "unacked", "seen", "notseen", "closed"])
    @should_be_one_of("sort_by", ["createdAt", "updatedAt"])
    @should_be_one_of("order", ["asc", "desc"])
    @should_be_one_of("tags_operator", ["and", "or"])
    def validate(self):
        pass

    def decode(self):
        return {
            'createdAfter': convert_from_date(self.created_after),
            'createdBefore': convert_from_date(self.created_before),
            'updatedAfter': convert_from_date(self.updated_after),
            'updatedBefore': convert_from_date(self.updated_before),
            'limit': self.limit,
            'status': self.status,
            'sortBy': self.sort_by,
            'order': self.order,
            'tags': list_to_str(self.tags),
            'tagsOperator': self.tags_operator
        }


class ListAlertLogsRequest(BaseRequest):
    def __init__(self, id=None, alias=None, limit=None, order=None, last_key=None):
        """
        Used to hold required parameters of List Alert Logs Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#listLogs

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        limit : int, optional
            Page size. (Default is 20, Max is 100)
        order : {'asc', 'desc'}, optional
            Sort order of the result set. Default is 'desc'
        last_key : str, optional
            Key which will be used in pagination.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.limit = limit
        self.order = order
        self.last_key = last_key

    @required_one_of(["id", "alias"])
    @should_be_one_of("order", ["asc", "desc"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'limit': self.limit,
            'order': self.order,
            'lastKey': self.last_key
        }


class ListAlertNotesRequest(BaseRequest):
    def __init__(self, id=None, alias=None, limit=None, order=None, last_key=None):
        """
        Used to hold required parameters of List Alert Notes Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#listNotes

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        limit : int, optional
            Page size. (Default is 20, Max is 100)
        order : {'asc', 'desc'}, optional
            Sort order of the result set. Default is 'desc'
        last_key : str, optional
            Key which will be used in pagination.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.limit = limit
        self.order = order
        self.last_key = last_key

    @required_one_of(["id", "alias"])
    @should_be_one_of("order", ["asc", "desc"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'limit': self.limit,
            'order': self.order,
            'lastKey': self.last_key
        }


class ListAlertRecipientsRequest(BaseRequest):
    def __init__(self, id=None, alias=None):
        """
        Used to hold required parameters of List Alert Recipients Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#listRecipients

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias

    @required_one_of(["id", "alias"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias
        }


class CreateAlertRequest(BaseRequest):
    def __init__(self, message=None, teams=None, alias=None, description=None, recipients=None, actions=None,
                 source=None, tags=None, details=None, entity=None, user=None, note=None):
        """
        Used to hold required parameters of Create Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#createAlertRequest

        Parameters
        ----------
        message : str, required
            Alert message limited to 130 characters.
        teams : list of str, optional
            List of team names which will be responsible for the alert.
        alias : str, optional
            A user defined identifier for the alert.
        description : str, optional
            Field for details of an alert.
        recipients : list of str, optional
            User, group, schedule or escalation names defines which users will receive the notifications of the alert.
        actions : list of str, optional
            Custom actions which can be executed for the alert.
        source : str, optional
            Field to specify source of alert. Default is IP address of incoming request
        tags : list of str, optional
            A comma separated list of labels attached to the alert.
        details : dict, optional
            User defined properties.
        entity : str, optional
            The entity the alert is related to.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        """
        BaseRequest.__init__(self)
        self.message = message
        self.teams = teams
        self.alias = alias
        self.description = description
        self.recipients = recipients
        self.actions = actions
        self.source = source
        self.tags = tags
        self.details = details
        self.entity = entity
        self.user = user
        self.note = note

    @required("message")
    @max_value("message", 130)
    def validate(self):
        pass

    def decode(self):
        return {
            'message': self.message,
            'teams': list_to_str(self.teams),
            'alias': self.alias,
            'description': self.description,
            'recipients': list_to_str(self.recipients),
            'actions': list_to_str(self.actions),
            'source': self.source,
            'tags': list_to_str(self.tags),
            'details': self.details,
            'entity': self.entity,
            'user': self.user,
            'note': self.note
        }


class CloseAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Close Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#closeAlertRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class DeleteAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, user=None, source=None):
        """
        Used to hold required parameters of Delete Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#deleteAlertRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.user = user
        self.source = source

    @required_one_of(["id", "alias"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'user': self.user,
            'source': self.source
        }


class CountAlertsRequest(BaseRequest):
    def __init__(self, created_after=None, created_before=None, updated_after=None, updated_before=None, limit=None,
                 status=None, tags=None, tags_operator=None):
        """
        Used to hold required parameters of Count Alerts Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#countAlertRequest

        Parameters
        ----------
        created_after : datetime, optional
            UTC datetime. Filter alerts created after specified time.
        created_before : datetime, optional
            UTC datetime. Filter alerts created before specified time.
        updated_after : datetime, optional
            UTC datetime. Filter alerts updated after specified time.
        updated_before : datetime, optional
            UTC datetime. Filter alerts updated before specified time.
        limit : int, optional
            Page size. (Default is 20, Max is 100)
        status : {'open', 'acked', 'unacked', 'seen', 'notseen', 'closed'}
            Unix timestamp in nanoseconds. Filter alerts with status.
        tags : list of str, optional
            List of tags to be used to filter alerts.
        tags_operator : {'and', 'or'}, optional
            Operator of filtering alerts using tags. Default is and
        """
        BaseRequest.__init__(self)
        self.created_after = created_after
        self.created_before = created_before
        self.updated_after = updated_after
        self.updated_before = updated_before
        self.limit = limit
        self.status = status
        self.tags = tags
        self.tags_operator = tags_operator

    @max_value("limit", 100)
    @should_be_one_of("status", ["open", "acked", "unacked", "seen", "notseen", "closed"])
    def validate(self):
        pass

    def decode(self):
        return {
            'createdAfter': convert_from_date(self.created_after),
            'createdBefore': convert_from_date(self.created_before),
            'updatedAfter': convert_from_date(self.updated_after),
            'updatedBefore': convert_from_date(self.updated_before),
            'limit': self.limit,
            'status': self.status,
            'tags': list_to_str(self.tags),
            'tagsOperator': self.tags_operator
        }


class AcknowledgeAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Acknowledge Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#acknowledgeRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class SnoozeAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, end_date=None, time_zone=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Snooze Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#snoozeRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        end_date : datetime.datetime, required
            The date and time snooze will end in.
        time_zone : str, optional
            Time zone of the date to be converted
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.end_date = end_date
        self.time_zone = time_zone
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    @required("endDate")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'endDate': format_date(self.end_date),
            'timeZone': self.time_zone,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class RenotifyAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, recipients=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Renotify Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#renotifyRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        recipients : list of str, optional
            The user names of individual users or groups. If not specified alert recipients will be renotified.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.recipients = recipients
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'recipients': list_to_str(self.recipients),
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class TakeOwnershipOfAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Take Ownership of Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#takeOwnershipRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class AssignOwnerToAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, owner=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Assign Owner to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#assignRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        owner : str, required
            The user who will be the owner of the alert after the execution.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.owner = owner
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    @required("owner")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'owner': self.owner,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class AddTeamToAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, team=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Add Team to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#addTeamRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        team : str, required
            The new team name that will be added.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.team = team
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    @required("team")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'team': self.team,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class AddRecipientToAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, recipient=None, user=None, note=None, source=None):
        """
        Used to hold required parameters of Add Recipient to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#addRecipientRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        recipient : str, required
            The new recipient that will be added.
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        note : str, optional
            Additional alert note
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.recipient = recipient
        self.user = user
        self.note = note
        self.source = source

    @required_one_of(["id", "alias"])
    @required("recipient")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'recipient': self.recipient,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class AddNoteToAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, note=None, user=None, source=None):
        """
        Used to hold required parameters of Add Note to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#addNoteRequest

        One of the [id, alias] parameters must be given, can not be given together.

       Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        note : str, required
            Note text that will be added
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.note = note
        self.user = user
        self.source = source

    @required_one_of(["id", "alias"])
    @required("note")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'note': self.note,
            'user': self.user,
            'source': self.source
        }


class AddTagsToAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, tags=None, user=None, source=None, note=None):
        """
        Used to hold required parameters of Add Tags to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#addTagsRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        tags : list of str, required
            List of tags that will be added.
        note : str, required
            Note text that will be added
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.tags = tags
        self.user = user
        self.source = source
        self.note = note

    @required_one_of(["id", "alias"])
    @required("tags")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'tags': list_to_str(self.tags),
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class RemoveTagsFromAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, tags=None, user=None, source=None, note=None):
        """
        Used to hold required parameters of Remove Tags to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#removeTagsRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        tags : list of str, required
            List of tags that will be removed.
        note : str, required
            Note text that will be added
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.tags = tags
        self.user = user
        self.source = source
        self.note = note

    @required_one_of(["id", "alias"])
    @required("tags")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'tags': list_to_str(self.tags),
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class AddDetailsToAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, details=None, user=None, source=None, note=None):
        """
        Used to hold required parameters of Add Details to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#addDetailsRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        details : dict, required
            Set of properties to be added to alert details.
        note : str, required
            Note text that will be added
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.details = details
        self.user = user
        self.source = source
        self.note = note

    @required_one_of(["id", "alias"])
    @required("details")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'details': self.details,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class RemoveDetailsFromAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, keys=None, user=None, source=None, note=None):
        """
        Used to hold required parameters of Remove Details From Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#removeDetailsRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        keys : list of str, required
            List of keys to be removed from alert details.
        note : str, required
            Note text that will be added
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.keys = keys
        self.user = user
        self.source = source
        self.note = note

    @required_one_of(["id", "alias"])
    @required("keys")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'keys': list_to_str(self.keys),
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class ExecuteActionOfAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, action=None, user=None, source=None, note=None):
        """
        Used to hold required parameters of Execute Action of Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#executeActionRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        action : str, required
            Action to execute.
        note : str, required
            Note text that will be added
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.action = action
        self.user = user
        self.source = source
        self.note = note

    @required_one_of(["id", "alias"])
    @required("action")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'action': self.action,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }


class AttachFileToAlertRequest(BaseRequest):
    def __init__(self, id=None, alias=None, attachment=None, user=None, source=None, index_file=None, note=None):
        """
        Used to hold required parameters of Attach File to Alert Request call.
        https://www.opsgenie.com/docs/web-api/alert-api#attachmentRequest

        One of the [id, alias] parameters must be given, can not be given together.

        Parameters
        ----------
        id : str, optional
            Id of the alert to be retrieved.
        alias : str, optional
            Alias of the alert to be retrieved. Using alias will only retrieve an open alert with that alias.
        attachment : str, required
            Path of the file to be attached.
        index_file : str, optional
            Name of html file which will be shown when attachment clicked on UI. See doc for more.
        note : str, required
            Note text that will be added
        user : str, optional
            Sets default owner of the execution. Default is owner of account.
        source : str, optional
            User defined field to specify source of close action.
        """
        BaseRequest.__init__(self)
        self.id = id
        self.alias = alias
        self.attachment = attachment
        self.user = user
        self.source = source
        self.index_file = index_file
        self.note = note

    @required_one_of(["id", "alias"])
    @required("attachment")
    def validate(self):
        pass

    def decode(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'user': self.user,
            'note': self.note,
            'source': self.source
        }
