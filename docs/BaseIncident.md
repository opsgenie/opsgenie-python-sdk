# BaseIncident

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tiny_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**is_seen** | **bool** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**source** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**responders** | [**list[Responder]**](Responder.md) |  | [optional] 
**owner_team** | **str** |  | [optional] 
**extra_properties** | **dict(str, str)** | Map of key-value pairs to use as custom properties of the incident | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


