# whoisfreaks.DatabasesSubdomainsApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_subdomains_daily**](DatabasesSubdomainsApi.md#db_subdomains_daily) | **GET** /v3.2/download/dbupdate/daily/subdomains | Subdomains Daily
[**db_subdomains_monthly**](DatabasesSubdomainsApi.md#db_subdomains_monthly) | **GET** /v3.2/download/dbupdate/monthly/subdomains | Subdomains Monthly
[**db_subdomains_weekly**](DatabasesSubdomainsApi.md#db_subdomains_weekly) | **GET** /v3.2/download/dbupdate/weekly/subdomains | Subdomains Weekly


# **db_subdomains_daily**
> bytearray db_subdomains_daily(var_date=var_date)

Subdomains Daily

Subdomains Daily. Returns the file/snapshot described by this operation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.whoisfreaks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whoisfreaks.Configuration(
    host = "https://api.whoisfreaks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whoisfreaks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whoisfreaks.DatabasesSubdomainsApi(api_client)
    var_date = '2013-10-20' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Subdomains Daily
        api_response = api_instance.db_subdomains_daily(var_date=var_date)
        print("The response of DatabasesSubdomainsApi->db_subdomains_daily:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesSubdomainsApi->db_subdomains_daily: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| yyyy-MM-dd; omit for latest | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_subdomains_monthly**
> bytearray db_subdomains_monthly(var_date=var_date)

Subdomains Monthly

Subdomains Monthly. Returns the file/snapshot described by this operation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.whoisfreaks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whoisfreaks.Configuration(
    host = "https://api.whoisfreaks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whoisfreaks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whoisfreaks.DatabasesSubdomainsApi(api_client)
    var_date = '2013-10-20' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Subdomains Monthly
        api_response = api_instance.db_subdomains_monthly(var_date=var_date)
        print("The response of DatabasesSubdomainsApi->db_subdomains_monthly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesSubdomainsApi->db_subdomains_monthly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| yyyy-MM-dd; omit for latest | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_subdomains_weekly**
> bytearray db_subdomains_weekly(var_date=var_date)

Subdomains Weekly

Subdomains Weekly. Returns the file/snapshot described by this operation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.whoisfreaks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = whoisfreaks.Configuration(
    host = "https://api.whoisfreaks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with whoisfreaks.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = whoisfreaks.DatabasesSubdomainsApi(api_client)
    var_date = '2013-10-20' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Subdomains Weekly
        api_response = api_instance.db_subdomains_weekly(var_date=var_date)
        print("The response of DatabasesSubdomainsApi->db_subdomains_weekly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesSubdomainsApi->db_subdomains_weekly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| yyyy-MM-dd; omit for latest | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

