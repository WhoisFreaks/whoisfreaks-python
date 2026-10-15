# whoisfreaks.DatabasesExpiringDroppedApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_dropped**](DatabasesExpiringDroppedApi.md#db_dropped) | **GET** /v3.1/download/domainer/dropped | Dropped Domains
[**db_dropped_backlinks**](DatabasesExpiringDroppedApi.md#db_dropped_backlinks) | **GET** /v3.3/download/domainer/dropped/backlinks | Dropped With Backlinks
[**db_dropped_json**](DatabasesExpiringDroppedApi.md#db_dropped_json) | **GET** /v3.1/domains/dropped | Dropped Domains (JSON)
[**db_expired**](DatabasesExpiringDroppedApi.md#db_expired) | **GET** /v3.1/download/domainer/expired | Expiring Domains
[**db_expired_cleaned**](DatabasesExpiringDroppedApi.md#db_expired_cleaned) | **GET** /v3.1/download/domainer/expired/cleaned | Expiring Cleaned WHOIS


# **db_dropped**
> bytearray db_dropped(whois, var_date=var_date)

Dropped Domains

Dropped Domains. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesExpiringDroppedApi(api_client)
    whois = true # bool | 
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Dropped Domains
        api_response = api_instance.db_dropped(whois, var_date=var_date)
        print("The response of DatabasesExpiringDroppedApi->db_dropped:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesExpiringDroppedApi->db_dropped: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois** | **bool**|  | 
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

# **db_dropped_backlinks**
> bytearray db_dropped_backlinks(whois=whois, var_date=var_date)

Dropped With Backlinks

Dropped With Backlinks. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesExpiringDroppedApi(api_client)
    whois = true # bool |  (optional)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Dropped With Backlinks
        api_response = api_instance.db_dropped_backlinks(whois=whois, var_date=var_date)
        print("The response of DatabasesExpiringDroppedApi->db_dropped_backlinks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesExpiringDroppedApi->db_dropped_backlinks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois** | **bool**|  | [optional] 
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

# **db_dropped_json**
> List[str] db_dropped_json(var_date=var_date, tlds=tlds)

Dropped Domains (JSON)

Dropped Domains (JSON). Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesExpiringDroppedApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)
    tlds = 'com,net' # str |  (optional)

    try:
        # Dropped Domains (JSON)
        api_response = api_instance.db_dropped_json(var_date=var_date, tlds=tlds)
        print("The response of DatabasesExpiringDroppedApi->db_dropped_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesExpiringDroppedApi->db_dropped_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| yyyy-MM-dd; omit for latest | [optional] 
 **tlds** | **str**|  | [optional] 

### Return type

**List[str]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON array of domains |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_expired**
> bytearray db_expired(whois, var_date=var_date)

Expiring Domains

Expiring Domains. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesExpiringDroppedApi(api_client)
    whois = true # bool | 
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Expiring Domains
        api_response = api_instance.db_expired(whois, var_date=var_date)
        print("The response of DatabasesExpiringDroppedApi->db_expired:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesExpiringDroppedApi->db_expired: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois** | **bool**|  | 
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

# **db_expired_cleaned**
> bytearray db_expired_cleaned(var_date=var_date)

Expiring Cleaned WHOIS

Expiring Cleaned WHOIS. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesExpiringDroppedApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Expiring Cleaned WHOIS
        api_response = api_instance.db_expired_cleaned(var_date=var_date)
        print("The response of DatabasesExpiringDroppedApi->db_expired_cleaned:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesExpiringDroppedApi->db_expired_cleaned: %s\n" % e)
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

