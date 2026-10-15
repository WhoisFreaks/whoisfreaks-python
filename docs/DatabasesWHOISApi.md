# whoisfreaks.DatabasesWHOISApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_whois_daily**](DatabasesWHOISApi.md#db_whois_daily) | **GET** /v3.3/download/dbupdate/daily/domains/whois | WHOIS Database Daily
[**db_whois_monthly**](DatabasesWHOISApi.md#db_whois_monthly) | **GET** /v3.3/download/dbupdate/monthly/domains/whois | WHOIS Database Monthly
[**db_whois_weekly**](DatabasesWHOISApi.md#db_whois_weekly) | **GET** /v3.3/download/dbupdate/weekly/domains/whois | WHOIS Database Weekly


# **db_whois_daily**
> bytearray db_whois_daily(var_date=var_date)

WHOIS Database Daily

WHOIS Database Daily. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesWHOISApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # WHOIS Database Daily
        api_response = api_instance.db_whois_daily(var_date=var_date)
        print("The response of DatabasesWHOISApi->db_whois_daily:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesWHOISApi->db_whois_daily: %s\n" % e)
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

# **db_whois_monthly**
> bytearray db_whois_monthly(var_date=var_date)

WHOIS Database Monthly

WHOIS Database Monthly. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesWHOISApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # WHOIS Database Monthly
        api_response = api_instance.db_whois_monthly(var_date=var_date)
        print("The response of DatabasesWHOISApi->db_whois_monthly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesWHOISApi->db_whois_monthly: %s\n" % e)
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

# **db_whois_weekly**
> bytearray db_whois_weekly(var_date=var_date)

WHOIS Database Weekly

WHOIS Database Weekly. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesWHOISApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # WHOIS Database Weekly
        api_response = api_instance.db_whois_weekly(var_date=var_date)
        print("The response of DatabasesWHOISApi->db_whois_weekly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesWHOISApi->db_whois_weekly: %s\n" % e)
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

