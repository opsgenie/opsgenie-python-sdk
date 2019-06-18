# CreateIncidentPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message of the incident | [optional] 
**description** | **str** | Description field of the incident that is generally used to provide a detailed information about the incident. | [optional] 
**responders** | [**list[Recipient]**](Recipient.md) | Responders that the incident will be routed to send notifications | [optional] 
**tags** | **list[str]** | Tags of the incident. | [optional] 
**details** | **dict(str, str)** | Map of key-value pairs to use as custom properties of the incident | [optional] 
**priority** | **str** | Priority level of the incident | [optional] 
**note** | **str** | Additional note that will be added while creating the incident | [optional] 
**service_id** | **str** | Service on which incident will be created. | [optional] 
**status_page_entry** | [**dict(str, StatusPageEntry)**](StatusPageEntry.md) | Status page entry fields. If this field is leaved blank, message and description of incident will be used for title and detail respectively. | [optional] 
**notify_stakeholders** | **bool** | Indicate whether stakeholders are notified or not. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


