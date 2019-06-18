# CreateHeartbeatPayloadAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the heartbeat | 
**description** | **str** | An optional description of the heartbeat | [optional] 
**interval** | **int** | Specifies how often a heartbeat message should be expected | 
**interval_unit** | **str** | Interval specified as &#39;minutes&#39;, &#39;hours&#39; or &#39;days&#39; | 
**enabled** | **bool** | Enable/disable heartbeat monitoring | 
**owner_team** | [**CreateHeartbeatPayloadAllOfOwnerTeam**](CreateHeartbeatPayloadAllOfOwnerTeam.md) |  | [optional] 
**alert_message** | **str** | Specifies the alert message for heartbeat expiration alert. If this is not provided, default alert message is &#39;HeartbeatName is expired&#39; | [optional] 
**alert_tags** | **list[str]** | Specifies the alert tags for heartbeat expiration alert | [optional] 
**alert_priority** | **str** | Specifies the alert priority for heartbeat expiration alert. If this is not provided, default priority is P3 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


