# opsgenie_sdk.AccountApi

All URIs are relative to *https://api.opsgenie.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_info**](AccountApi.md#get_info) | **GET** /v2/account | Get Account Info


# **get_info**
> GetAccountInfoResponse get_info()

Get Account Info

Used to search and retrieve account information in OpsGenie

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
api_instance = opsgenie_sdk.AccountApi(opsgenie_sdk.ApiClient(configuration))

try:
    # Get Account Info
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAccountInfoResponse**](GetAccountInfoResponse.md)

### Authorization

[GenieKey](../README.md#GenieKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

