# whoisfreaks.DatabasesIPGeolocationApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**db_ip_city**](DatabasesIPGeolocationApi.md#db_ip_city) | **GET** /v3.3/download/snapshot/ip/city | IP to City Snapshot
[**db_ip_city_status**](DatabasesIPGeolocationApi.md#db_ip_city_status) | **GET** /v3.3/status/snapshot/ip/city | IP to City Snapshot Status
[**db_ip_country**](DatabasesIPGeolocationApi.md#db_ip_country) | **GET** /v3.3/download/snapshot/ip/country | IP to Country Snapshot
[**db_ip_country_status**](DatabasesIPGeolocationApi.md#db_ip_country_status) | **GET** /v3.3/status/snapshot/ip/country | IP to Country Snapshot Status


# **db_ip_city**
> bytearray db_ip_city(var_date)

IP to City Snapshot

IP to City Snapshot. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesIPGeolocationApi(api_client)
    var_date = '2026-10-01' # date | 

    try:
        # IP to City Snapshot
        api_response = api_instance.db_ip_city(var_date)
        print("The response of DatabasesIPGeolocationApi->db_ip_city:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesIPGeolocationApi->db_ip_city: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

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
**200** | ZIP archive |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_ip_city_status**
> SnapshotStatus db_ip_city_status()

IP to City Snapshot Status

IP to City Snapshot Status. Returns the file/snapshot described by this operation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.snapshot_status import SnapshotStatus
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
    api_instance = whoisfreaks.DatabasesIPGeolocationApi(api_client)

    try:
        # IP to City Snapshot Status
        api_response = api_instance.db_ip_city_status()
        print("The response of DatabasesIPGeolocationApi->db_ip_city_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesIPGeolocationApi->db_ip_city_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SnapshotStatus**](SnapshotStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_ip_country**
> bytearray db_ip_country(var_date)

IP to Country Snapshot

IP to Country Snapshot. Returns the file/snapshot described by this operation.

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
    api_instance = whoisfreaks.DatabasesIPGeolocationApi(api_client)
    var_date = '2026-10-01' # date | 

    try:
        # IP to Country Snapshot
        api_response = api_instance.db_ip_country(var_date)
        print("The response of DatabasesIPGeolocationApi->db_ip_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesIPGeolocationApi->db_ip_country: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

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
**200** | ZIP archive |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **db_ip_country_status**
> SnapshotStatus db_ip_country_status()

IP to Country Snapshot Status

IP to Country Snapshot Status. Returns the file/snapshot described by this operation.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.snapshot_status import SnapshotStatus
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
    api_instance = whoisfreaks.DatabasesIPGeolocationApi(api_client)

    try:
        # IP to Country Snapshot Status
        api_response = api_instance.db_ip_country_status()
        print("The response of DatabasesIPGeolocationApi->db_ip_country_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesIPGeolocationApi->db_ip_country_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SnapshotStatus**](SnapshotStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

