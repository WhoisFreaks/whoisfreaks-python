# whoisfreaks.DatabasesNewlyRegisteredApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_newly_cctld**](DatabasesNewlyRegisteredApi.md#db_newly_cctld) | **GET** /v3.1/download/domainer/cctld | Newly Registered ccTLD (CSV)
[**db_newly_cctld_cleaned**](DatabasesNewlyRegisteredApi.md#db_newly_cctld_cleaned) | **GET** /v3.1/download/domainer/cctld/cleaned | Newly Registered ccTLD Cleaned WHOIS (CSV)
[**db_newly_cctld_json**](DatabasesNewlyRegisteredApi.md#db_newly_cctld_json) | **GET** /v3.1/domains/newly/cctld | Newly Registered ccTLD (JSON)
[**db_newly_dns**](DatabasesNewlyRegisteredApi.md#db_newly_dns) | **GET** /v3.1/download/domainer/newly/dns | Newly Registered With DNS
[**db_newly_gtld**](DatabasesNewlyRegisteredApi.md#db_newly_gtld) | **GET** /v3.1/download/domainer/gtld | Newly Registered gTLD (CSV)
[**db_newly_gtld_cleaned**](DatabasesNewlyRegisteredApi.md#db_newly_gtld_cleaned) | **GET** /v3.1/download/domainer/gtld/cleaned | Newly Registered gTLD Cleaned WHOIS (CSV)
[**db_newly_gtld_json**](DatabasesNewlyRegisteredApi.md#db_newly_gtld_json) | **GET** /v3.1/domains/newly/gtld | Newly Registered gTLD (JSON)


# **db_newly_cctld**
> bytearray db_newly_cctld(whois, var_date=var_date, tlds=tlds)

Newly Registered ccTLD (CSV)

Newly Registered ccTLD (CSV). Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesNewlyRegisteredApi(api_client)
    whois = true # bool | 
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)
    tlds = 'com,net' # str |  (optional)

    try:
        # Newly Registered ccTLD (CSV)
        api_response = api_instance.db_newly_cctld(whois, var_date=var_date, tlds=tlds)
        print("The response of DatabasesNewlyRegisteredApi->db_newly_cctld:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesNewlyRegisteredApi->db_newly_cctld: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois** | **bool**|  | 
 **var_date** | **date**| yyyy-MM-dd; omit for latest | [optional] 
 **tlds** | **str**|  | [optional] 

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

# **db_newly_cctld_cleaned**
> bytearray db_newly_cctld_cleaned(var_date=var_date)

Newly Registered ccTLD Cleaned WHOIS (CSV)

Newly Registered ccTLD Cleaned WHOIS (CSV). Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesNewlyRegisteredApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Newly Registered ccTLD Cleaned WHOIS (CSV)
        api_response = api_instance.db_newly_cctld_cleaned(var_date=var_date)
        print("The response of DatabasesNewlyRegisteredApi->db_newly_cctld_cleaned:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesNewlyRegisteredApi->db_newly_cctld_cleaned: %s\n" % e)
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

# **db_newly_cctld_json**
> List[str] db_newly_cctld_json(var_date=var_date, tlds=tlds)

Newly Registered ccTLD (JSON)

Newly Registered ccTLD (JSON). Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesNewlyRegisteredApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)
    tlds = 'com,net' # str |  (optional)

    try:
        # Newly Registered ccTLD (JSON)
        api_response = api_instance.db_newly_cctld_json(var_date=var_date, tlds=tlds)
        print("The response of DatabasesNewlyRegisteredApi->db_newly_cctld_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesNewlyRegisteredApi->db_newly_cctld_json: %s\n" % e)
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

# **db_newly_dns**
> bytearray db_newly_dns(var_date=var_date)

Newly Registered With DNS

Newly Registered With DNS. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesNewlyRegisteredApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Newly Registered With DNS
        api_response = api_instance.db_newly_dns(var_date=var_date)
        print("The response of DatabasesNewlyRegisteredApi->db_newly_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesNewlyRegisteredApi->db_newly_dns: %s\n" % e)
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
**200** | JSON array of domains with DNS |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_newly_gtld**
> bytearray db_newly_gtld(whois, var_date=var_date, tlds=tlds)

Newly Registered gTLD (CSV)

Newly Registered gTLD (CSV). Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesNewlyRegisteredApi(api_client)
    whois = true # bool | 
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)
    tlds = 'com,net' # str |  (optional)

    try:
        # Newly Registered gTLD (CSV)
        api_response = api_instance.db_newly_gtld(whois, var_date=var_date, tlds=tlds)
        print("The response of DatabasesNewlyRegisteredApi->db_newly_gtld:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesNewlyRegisteredApi->db_newly_gtld: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois** | **bool**|  | 
 **var_date** | **date**| yyyy-MM-dd; omit for latest | [optional] 
 **tlds** | **str**|  | [optional] 

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

# **db_newly_gtld_cleaned**
> bytearray db_newly_gtld_cleaned(var_date=var_date)

Newly Registered gTLD Cleaned WHOIS (CSV)

Newly Registered gTLD Cleaned WHOIS (CSV). Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesNewlyRegisteredApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)

    try:
        # Newly Registered gTLD Cleaned WHOIS (CSV)
        api_response = api_instance.db_newly_gtld_cleaned(var_date=var_date)
        print("The response of DatabasesNewlyRegisteredApi->db_newly_gtld_cleaned:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesNewlyRegisteredApi->db_newly_gtld_cleaned: %s\n" % e)
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

# **db_newly_gtld_json**
> List[str] db_newly_gtld_json(var_date=var_date, tlds=tlds)

Newly Registered gTLD (JSON)

Newly Registered gTLD (JSON). Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesNewlyRegisteredApi(api_client)
    var_date = '2026-10-01' # date | yyyy-MM-dd; omit for latest (optional)
    tlds = 'com,net' # str |  (optional)

    try:
        # Newly Registered gTLD (JSON)
        api_response = api_instance.db_newly_gtld_json(var_date=var_date, tlds=tlds)
        print("The response of DatabasesNewlyRegisteredApi->db_newly_gtld_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesNewlyRegisteredApi->db_newly_gtld_json: %s\n" % e)
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

