from opsgenie.service import BaseService, execute
from .responses import *


class AlertService(BaseService):
    @execute("GET", url_suffix="/alert", response_cls=GetAlertResponse)
    def get_alert(self, request):
        """
        OpsGenie Get Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#getAlertRequest

        Parameters
        ----------
        request : GetAlertRequest

        Returns
        --------
        GetAlertResponse
        """
        pass

    @execute("GET", url_suffix="/alert", response_cls=ListAlertsResponse)
    def list_alerts(self, request):
        """
        OpsGenie Lis Alerts API call
        https://www.opsgenie.com/docs/web-api/alert-api#listAlertRequest

        Parameters
        ----------
        request : ListAlertsRequest

        Returns
        --------
        ListAlertsResponse
        """
        pass

    @execute("GET", url_suffix="/alert/log", response_cls=ListAlertLogsResponse)
    def list_alert_logs(self, request):
        """
        OpsGenie List Alert Logs API call
        https://www.opsgenie.com/docs/web-api/alert-api#listLogs

        Parameters
        ----------
        request : ListAlertLogsRequest

        Returns
        --------
        ListAlertLogsResponse
        """
        pass

    @execute("GET", url_suffix="/alert/note", response_cls=ListAlertNotesResponse)
    def list_alert_notes(self, request):
        """
        OpsGenie List Alert Notes API call
        https://www.opsgenie.com/docs/web-api/alert-api#listNotes

        Parameters
        ----------
        request : ListAlertNotesRequest

        Returns
        --------
        ListAlertNotesResponse
        """
        pass

    @execute("GET", url_suffix="/alert/recipient", response_cls=ListAlertRecipientsResponse)
    def list_alert_recipients(self, request):
        """
        OpsGenie List Alert Recipients API call
        https://www.opsgenie.com/docs/web-api/alert-api#listRecipients

        Parameters
        ----------
        request : ListAlertRecipientsRequest

        Returns
        --------
        ListAlertsRecipientsResponse
        """
        pass

    @execute("POST", url_suffix="/alert", response_cls=CreateAlertResponse)
    def create_alert(self, request):
        """
        OpsGenie Create Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#createAlertRequest

        Parameters
        ----------
        request : CreateAlertRequest

        Returns
        --------
        CreateAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/close", response_cls=CloseAlertResponse)
    def close_alert(self, request):
        """
        OpsGenie Close Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#closeAlertRequest

        Parameters
        ----------
        request : CloseAlertRequest

        Returns
        --------
        CloseAlertResponse
        """
        pass

    @execute("DELETE", url_suffix="/alert", response_cls=DeleteAlertResponse)
    def delete_alert(self, request):
        """
        OpsGenie Delete Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#deleteAlertRequest

        Parameters
        ----------
        request : DeleteAlertRequest

        Returns
        --------
        DeleteAlertResponse
        """
        pass

    @execute("GET", url_suffix="/alert/count", response_cls=CountAlertsResponse)
    def count_alerts(self, request):
        """
        OpsGenie Count Alerts API call
        https://www.opsgenie.com/docs/web-api/alert-api#countAlertRequest

        Parameters
        ----------
        request : CountAlertsRequest

        Returns
        --------
        CountAlertsResponse
        """
        pass

    @execute("POST", url_suffix="/alert/acknowledge", response_cls=AcknowledgeAlertResponse)
    def acknowledge_alert(self, request):
        """
        OpsGenie Acknowledge Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#acknowledgeRequest

        Parameters
        ----------
        request : AcknowledgeAlertRequest

        Returns
        --------
        AcknowledgeAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/snooze", response_cls=SnoozeAlertResponse)
    def snooze_alert(self, request):
        """
        OpsGenie Snooze Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#snoozeRequest

        Parameters
        ----------
        request : SnoozeAlertRequest

        Returns
        --------
        SnoozeAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/renotify", response_cls=RenotifyAlertResponse)
    def renotify_alert(self, request):
        """
        OpsGenie Renotify Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#renotifyRequest

        Parameters
        ----------
        request : RenotifyAlertRequest

        Returns
        --------
        RenotifyAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/takeOwnership", response_cls=TakeOwnershipOfAlertResponse)
    def take_ownership_of_alert(self, request):
        """
        OpsGenie Take Ownership of Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#takeOwnershipRequest

        Parameters
        ----------
        request : TakeOwnershipOfAlertRequest

        Returns
        --------
        TakeOwnershipOfAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/assign", response_cls=AssignOwnerToAlertResponse)
    def assign_owner_to_alert(self, request):
        """
        OpsGenie Assign Owner to Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#assignRequest

        Parameters
        ----------
        request : AssignOwnerToAlertRequest

        Returns
        --------
        AssignOwnerToAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/team", response_cls=AddTeamToAlertResponse)
    def add_team_to_alert(self, request):
        """
        OpsGenie Add Team to Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#addTeamRequest

        Parameters
        ----------
        request : AddTeamToAlertRequest

        Returns
        --------
        AddTeamToAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/recipient", response_cls=AddRecipientToAlertResponse)
    def add_recipient_to_alert(self, request):
        """
        OpsGenie Add Recipient to Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#addRecipientRequest

        Parameters
        ----------
        request : AddRecipientToAlertRequest

        Returns
        --------
        AddRecipientToAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/note", response_cls=AddNoteToAlertResponse)
    def add_note_to_alert(self, request):
        """
        OpsGenie Add Note to Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#addNoteRequest

        Parameters
        ----------
        request : AddNoteToAlertRequest

        Returns
        --------
        AddNoteToAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/tags", response_cls=AddTagsToAlertResponse)
    def add_tags_to_alert(self, request):
        """
        OpsGenie Add Tags to Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#addTagsRequest

        Parameters
        ----------
        request : AddTagsToAlertRequest

        Returns
        --------
        AddTagsToAlertResponse
        """
        pass

    @execute("DELETE", url_suffix="/alert/tags", response_cls=RemoveTagsFromAlertResponse)
    def remove_tags_from_alert(self, request):
        """
        OpsGenie Remove Tags from Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#removeTagsRequest

        Parameters
        ----------
        request : RemoveTagsFromAlertRequest

        Returns
        --------
        RemoveTagsFromAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/details", response_cls=AddDetailsToAlertResponse)
    def add_details_to_alert(self, request):
        """
        OpsGenie Add Details to Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#addDetailsRequest

        Parameters
        ----------
        request : AddDetailsToAlertRequest

        Returns
        --------
        AddDetailsToAlertResponse
        """
        pass

    @execute("DELETE", url_suffix="/alert/details", response_cls=RemoveDetailsFromAlertResponse)
    def remove_details_to_alert(self, request):
        """
        OpsGenie Remove Details from Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#removeDetailsRequest

        Parameters
        ----------
        request : RemoveDetailsFromAlertRequest

        Returns
        --------
        RemoveDetailsFromAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/executeAction", response_cls=ExecuteActionOfAlertResponse)
    def execute_action_of_alert(self, request):
        """
        OpsGenie Execute Action of Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#executeActionRequest

        Parameters
        ----------
        request : ExecuteActionOfAlertRequest

        Returns
        --------
        ExecuteActionOfAlertResponse
        """
        pass

    @execute("POST", url_suffix="/alert/attach", response_cls=AttachFileToAlertResponse, attachment=True)
    def attach_file_to_alert(self, request):
        """
        OpsGenie Attach File to Alert API call
        https://www.opsgenie.com/docs/web-api/alert-api#attachmentRequest

        Parameters
        ----------
        request : AttachFileToAlertRequest

        Returns
        --------
        AttachFileToAlertResponse
        """
        pass
