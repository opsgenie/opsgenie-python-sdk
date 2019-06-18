# opsgenie_sdk.IncidentApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_incident**](IncidentApi.md#close_incident) | **POST** /v1/incidents/{identifier}/close | Close Incident
[**create_incident**](IncidentApi.md#create_incident) | **POST** /v1/incidents/create | Create Incident
[**delete_incident**](IncidentApi.md#delete_incident) | **DELETE** /v1/incidents/{identifier} | Delete Incident
[**get_incident**](IncidentApi.md#get_incident) | **GET** /v1/incidents/{identifier} | Get Incident
[**get_incident_request_status**](IncidentApi.md#get_incident_request_status) | **GET** /v1/incidents/requests/{requestId} | Get Request Status of Incident
[**list_incidents**](IncidentApi.md#list_incidents) | **GET** /v1/incidents/ | List incidents


# **close_incident**
> SuccessResponse close_incident(identifier, identifier_type=identifier_type, close_incident_payload=close_incident_payload)

Close Incident

Closes incident with given identifier

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
api_instance = opsgenie_sdk.IncidentApi(opsgenie_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of incident which could be incident id or tiny id
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'tiny. Default is id' (optional) (default to 'id')
close_incident_payload = opsgenie_sdk.CloseIncidentPayload() # CloseIncidentPayload | Request payload of closing incident action (optional)

try:
    # Close Incident
    api_response = api_instance.close_incident(identifier, identifier_type=identifier_type, close_incident_payload=close_incident_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentApi->close_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of incident which could be incident id or tiny id | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;tiny. Default is id&#39; | [optional] [default to &#39;id&#39;]
 **close_incident_payload** | [**CloseIncidentPayload**](CloseIncidentPayload.md)| Request payload of closing incident action | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_incident**
> SuccessResponse create_incident(create_incident_payload)

Create Incident

Creates a new incident

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
api_instance = opsgenie_sdk.IncidentApi(opsgenie_sdk.ApiClient(configuration))
create_incident_payload = opsgenie_sdk.CreateIncidentPayload() # CreateIncidentPayload | Request payload of created incident

try:
    # Create Incident
    api_response = api_instance.create_incident(create_incident_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentApi->create_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_incident_payload** | [**CreateIncidentPayload**](CreateIncidentPayload.md)| Request payload of created incident | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_incident**
> SuccessResponse delete_incident(identifier, identifier_type=identifier_type)

Delete Incident

Deletes an incident using incident id or the tiny id

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
api_instance = opsgenie_sdk.IncidentApi(opsgenie_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of incident which could be incident id or tiny id
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'tiny. Default is id' (optional) (default to 'id')

try:
    # Delete Incident
    api_response = api_instance.delete_incident(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentApi->delete_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of incident which could be incident id or tiny id | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;tiny. Default is id&#39; | [optional] [default to &#39;id&#39;]

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incident**
> GetIncidentResponse get_incident(identifier, identifier_type=identifier_type)

Get Incident

Returns incident with given id, tiny id or alias

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
api_instance = opsgenie_sdk.IncidentApi(opsgenie_sdk.ApiClient(configuration))
identifier = 'identifier_example' # str | Identifier of incident which could be incident id or tiny id
identifier_type = 'id' # str | Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'tiny. Default is id' (optional) (default to 'id')

try:
    # Get Incident
    api_response = api_instance.get_incident(identifier, identifier_type=identifier_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentApi->get_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier of incident which could be incident id or tiny id | 
 **identifier_type** | **str**| Type of the identifier that is provided as an in-line parameter. Possible values are &#39;id&#39; or &#39;tiny. Default is id&#39; | [optional] [default to &#39;id&#39;]

### Return type

[**GetIncidentResponse**](GetIncidentResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incident_request_status**
> GetIncidentRequestStatusResponse get_incident_request_status(request_id)

Get Request Status of Incident

Used to track the status and incident details (if any) of the request whose identifier is given

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
api_instance = opsgenie_sdk.IncidentApi(opsgenie_sdk.ApiClient(configuration))
request_id = 'request_id_example' # str | Universally unique identifier of the questioned request

try:
    # Get Request Status of Incident
    api_response = api_instance.get_incident_request_status(request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentApi->get_incident_request_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Universally unique identifier of the questioned request | 

### Return type

[**GetIncidentRequestStatusResponse**](GetIncidentRequestStatusResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_incidents**
> ListIncidentsResponse list_incidents(query, offset=offset, limit=limit, sort=sort, order=order)

List incidents

Return list of incidents

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
api_instance = opsgenie_sdk.IncidentApi(opsgenie_sdk.ApiClient(configuration))
query = 'query_example' # str | Search query to apply while filtering the incidents.
offset = 56 # int | Start index of the result set (to apply pagination). Minimum value (and also default value) is 0. (optional)
limit = 56 # int | Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 (optional)
sort = 'createdAt' # str | Name of the field that result set will be sorted by (optional) (default to 'createdAt')
order = 'desc' # str | Sorting order of the result set (optional) (default to 'desc')

try:
    # List incidents
    api_response = api_instance.list_incidents(query, offset=offset, limit=limit, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentApi->list_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query to apply while filtering the incidents. | 
 **offset** | **int**| Start index of the result set (to apply pagination). Minimum value (and also default value) is 0. | [optional] 
 **limit** | **int**| Maximum number of items to provide in the result. Must be a positive integer value. Default value is 20 and maximum value is 100 | [optional] 
 **sort** | **str**| Name of the field that result set will be sorted by | [optional] [default to &#39;createdAt&#39;]
 **order** | **str**| Sorting order of the result set | [optional] [default to &#39;desc&#39;]

### Return type

[**ListIncidentsResponse**](ListIncidentsResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

