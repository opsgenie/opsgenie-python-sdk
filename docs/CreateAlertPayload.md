# CreateAlertPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | Display name of the request owner | [optional] 
**note** | **str** | Additional note that will be added while creating the alert | [optional] 
**source** | **str** | Source field of the alert. Default value is IP address of the incoming request | [optional] 
**message** | **str** | Message of the alert | 
**alias** | **str** | Client-defined identifier of the alert, that is also the key element of alert deduplication. | [optional] 
**description** | **str** | Description field of the alert that is generally used to provide a detailed information about the alert. | [optional] 
**responders** | [**list[Recipient]**](Recipient.md) | Responders that the alert will be routed to send notifications | [optional] 
**visible_to** | [**list[Recipient]**](Recipient.md) | Teams and users that the alert will become visible to without sending any notification | [optional] 
**actions** | **list[str]** | Custom actions that will be available for the alert | [optional] 
**tags** | **list[str]** | Tags of the alert | [optional] 
**details** | **dict(str, str)** | Map of key-value pairs to use as custom properties of the alert | [optional] 
**entity** | **str** | Entity field of the alert that is generally used to specify which domain alert is related to | [optional] 
**priority** | **str** | Priority level of the alert | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


