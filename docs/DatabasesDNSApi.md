# whoisfreaks.DatabasesDNSApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_dns_daily**](DatabasesDNSApi.md#db_dns_daily) | **GET** /v3.2/download/dbupdate/daily/dns | DNS Database Daily
[**db_dns_monthly**](DatabasesDNSApi.md#db_dns_monthly) | **GET** /v3.2/download/dbupdate/monthly/dns | DNS Database Monthly
[**db_dns_weekly**](DatabasesDNSApi.md#db_dns_weekly) | **GET** /v3.2/download/dbupdate/weekly/dns | DNS Database Weekly


# **db_dns_daily**
> bytearray db_dns_daily(var_date=var_date)

DNS Database Daily

DNS Database Daily. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesDNSApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # DNS Database Daily
        api_response = api_instance.db_dns_daily(var_date=var_date)
        print("The response of DatabasesDNSApi->db_dns_daily:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesDNSApi->db_dns_daily: %s\n" % e)
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

# **db_dns_monthly**
> bytearray db_dns_monthly(var_date=var_date)

DNS Database Monthly

DNS Database Monthly. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesDNSApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # DNS Database Monthly
        api_response = api_instance.db_dns_monthly(var_date=var_date)
        print("The response of DatabasesDNSApi->db_dns_monthly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesDNSApi->db_dns_monthly: %s\n" % e)
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

# **db_dns_weekly**
> bytearray db_dns_weekly(var_date=var_date)

DNS Database Weekly

DNS Database Weekly. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesDNSApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # DNS Database Weekly
        api_response = api_instance.db_dns_weekly(var_date=var_date)
        print("The response of DatabasesDNSApi->db_dns_weekly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesDNSApi->db_dns_weekly: %s\n" % e)
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

