# whoisfreaks.WHOISApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_whois**](WHOISApi.md#bulk_whois) | **POST** /v2.0/bulkwhois/live | Bulk WHOIS Lookup
[**whois_history**](WHOISApi.md#whois_history) | **GET** /v2.0/whois/history | Historical WHOIS records for a domain
[**whois_live**](WHOISApi.md#whois_live) | **GET** /v2.0/whois/live | Live WHOIS Lookup
[**whois_reverse**](WHOISApi.md#whois_reverse) | **GET** /v2.0/whois/reverse | Reverse WHOIS lookup by keyword


# **bulk_whois**
> BulkWhoisResponse bulk_whois(bulk_whois_request, format=format)

Bulk WHOIS Lookup

Up to 100 domains in one request. 1 credit per successful domain.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.bulk_whois_request import BulkWhoisRequest
from whoisfreaks.models.bulk_whois_response import BulkWhoisResponse
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
    api_instance = whoisfreaks.WHOISApi(api_client)
    bulk_whois_request = whoisfreaks.BulkWhoisRequest() # BulkWhoisRequest | 
    format = json # str |  (optional) (default to json)

    try:
        # Bulk WHOIS Lookup
        api_response = api_instance.bulk_whois(bulk_whois_request, format=format)
        print("The response of WHOISApi->bulk_whois:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WHOISApi->bulk_whois: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_whois_request** | [**BulkWhoisRequest**](BulkWhoisRequest.md)|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**BulkWhoisResponse**](BulkWhoisResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**4XX** | Error response (4XX) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whois_history**
> WhoisHistoricalResponse whois_history(domain_name, format=format)

Historical WHOIS records for a domain

Every WHOIS record captured for the domain since 1986, in one response (no pagination). Cost 2 credits.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.whois_historical_response import WhoisHistoricalResponse
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
    api_instance = whoisfreaks.WHOISApi(api_client)
    domain_name = 'whoisfreaks.com' # str | Domain to fetch historical WHOIS records for
    format = 'format_example' # str |  (optional)

    try:
        # Historical WHOIS records for a domain
        api_response = api_instance.whois_history(domain_name, format=format)
        print("The response of WHOISApi->whois_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WHOISApi->whois_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| Domain to fetch historical WHOIS records for | 
 **format** | **str**|  | [optional] 

### Return type

[**WhoisHistoricalResponse**](WhoisHistoricalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Historical WHOIS records |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whois_live**
> WhoisResponse whois_live(domain_name, format=format)

Live WHOIS Lookup

Real-time WHOIS lookup from authoritative servers. Cost 1 credit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.whois_response import WhoisResponse
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
    api_instance = whoisfreaks.WHOISApi(api_client)
    domain_name = 'whoisfreaks.com' # str | 
    format = json # str |  (optional) (default to json)

    try:
        # Live WHOIS Lookup
        api_response = api_instance.whois_live(domain_name, format=format)
        print("The response of WHOISApi->whois_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WHOISApi->whois_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**WhoisResponse**](WhoisResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Invalid API key |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whois_reverse**
> ReverseWhoisResponse whois_reverse(keyword, page=page, format=format)

Reverse WHOIS lookup by keyword

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.reverse_whois_response import ReverseWhoisResponse
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
    api_instance = whoisfreaks.WHOISApi(api_client)
    keyword = 'whoisfreaks' # str | Keyword to search across WHOIS records
    page = 1 # int | Page number (optional)
    format = 'format_example' # str |  (optional)

    try:
        # Reverse WHOIS lookup by keyword
        api_response = api_instance.whois_reverse(keyword, page=page, format=format)
        print("The response of WHOISApi->whois_reverse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WHOISApi->whois_reverse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| Keyword to search across WHOIS records | 
 **page** | **int**| Page number | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**ReverseWhoisResponse**](ReverseWhoisResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reverse WHOIS results (paginated) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

