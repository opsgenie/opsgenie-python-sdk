# opsgenie_sdk.HeartbeatApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_heartbeat**](HeartbeatApi.md#create_heartbeat) | **POST** /v2/heartbeats | Create Heartbeat
[**delete_heartbeat**](HeartbeatApi.md#delete_heartbeat) | **DELETE** /v2/heartbeats/{name} | Delete Heartbeat
[**disable_heartbeat**](HeartbeatApi.md#disable_heartbeat) | **POST** /v2/heartbeats/{name}/disable | Disable Heartbeat
[**enable_heartbeat**](HeartbeatApi.md#enable_heartbeat) | **POST** /v2/heartbeats/{name}/enable | Enable Heartbeat
[**get_heartbeat**](HeartbeatApi.md#get_heartbeat) | **GET** /v2/heartbeats/{name} | Get Heartbeat
[**list_heart_beats**](HeartbeatApi.md#list_heart_beats) | **GET** /v2/heartbeats | List Heartbeats
[**ping**](HeartbeatApi.md#ping) | **GET** /v2/heartbeats/{name}/ping | Ping Heartbeat
[**update_heartbeat**](HeartbeatApi.md#update_heartbeat) | **PATCH** /v2/heartbeats/{name} | Update Heartbeat (Partial)


# **create_heartbeat**
> CreateHeartbeatResponse create_heartbeat(create_heartbeat_payload)

Create Heartbeat

Create a new heartbeat

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))
create_heartbeat_payload = opsgenie_sdk.CreateHeartbeatPayload() # CreateHeartbeatPayload | Request payload of created heartbeat

try:
    # Create Heartbeat
    api_response = api_instance.create_heartbeat(create_heartbeat_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->create_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_heartbeat_payload** | [**CreateHeartbeatPayload**](CreateHeartbeatPayload.md)| Request payload of created heartbeat | 

### Return type

[**CreateHeartbeatResponse**](CreateHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_heartbeat**
> SuccessResponse delete_heartbeat(name)

Delete Heartbeat

Delete heartbeat with given name

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Delete Heartbeat
    api_response = api_instance.delete_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->delete_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_heartbeat**
> DisableHeartbeatResponse disable_heartbeat(name)

Disable Heartbeat

Disable heartbeat request with given name

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Disable Heartbeat
    api_response = api_instance.disable_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->disable_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**DisableHeartbeatResponse**](DisableHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_heartbeat**
> EnableHeartbeatResponse enable_heartbeat(name)

Enable Heartbeat

Enable heartbeat request with given name

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Enable Heartbeat
    api_response = api_instance.enable_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->enable_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**EnableHeartbeatResponse**](EnableHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heartbeat**
> GetHeartbeatResponse get_heartbeat(name)

Get Heartbeat

Returns heartbeat with given name

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Get Heartbeat
    api_response = api_instance.get_heartbeat(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->get_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**GetHeartbeatResponse**](GetHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_heart_beats**
> ListHeartbeatResponse list_heart_beats()

List Heartbeats

Returns list of Heartbeats

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))

try:
    # List Heartbeats
    api_response = api_instance.list_heart_beats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->list_heart_beats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListHeartbeatResponse**](ListHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> SuccessResponse ping(name)

Ping Heartbeat

Ping Heartbeat for given heartbeat name

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat

try:
    # Ping Heartbeat
    api_response = api_instance.ping(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_heartbeat**
> UpdateHeartbeatResponse update_heartbeat(name, update_heartbeat_payload=update_heartbeat_payload)

Update Heartbeat (Partial)

Update Heartbeatwith given name

### Example

* Api Key Authentication (GenieKey):
```python
from __future__ import print_function
import time
import opsgenie_sdk
from opsgenie_sdk.rest import ApiException
from pprint import pprint
configuration = opsgenie_sdk.Configuration()
# Configure API key authorization: GenieKey
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# create an instance of the API class
api_instance = opsgenie_sdk.HeartbeatApi(opsgenie_sdk.ApiClient(configuration))
name = 'name_example' # str | Name of the heartbeat
update_heartbeat_payload = opsgenie_sdk.UpdateHeartbeatPayload() # UpdateHeartbeatPayload | Request payload of update heartbeat action (optional)

try:
    # Update Heartbeat (Partial)
    api_response = api_instance.update_heartbeat(name, update_heartbeat_payload=update_heartbeat_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->update_heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the heartbeat | 
 **update_heartbeat_payload** | [**UpdateHeartbeatPayload**](UpdateHeartbeatPayload.md)| Request payload of update heartbeat action | [optional] 

### Return type

[**UpdateHeartbeatResponse**](UpdateHeartbeatResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

