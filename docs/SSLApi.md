# whoisfreaks.SSLApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssl_lookup**](SSLApi.md#ssl_lookup) | **GET** /v1.0/ssl/live | SSL Certificate Lookup


# **ssl_lookup**
> SslResponse ssl_lookup(domain_name, chain=chain, ssl_raw=ssl_raw, format=format)

SSL Certificate Lookup

Real-time SSL cert with optional chain.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.ssl_response import SslResponse
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
    api_instance = whoisfreaks.SSLApi(api_client)
    domain_name = 'domain_name_example' # str | 
    chain = False # bool |  (optional) (default to False)
    ssl_raw = False # bool |  (optional) (default to False)
    format = json # str |  (optional) (default to json)

    try:
        # SSL Certificate Lookup
        api_response = api_instance.ssl_lookup(domain_name, chain=chain, ssl_raw=ssl_raw, format=format)
        print("The response of SSLApi->ssl_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSLApi->ssl_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **chain** | **bool**|  | [optional] [default to False]
 **ssl_raw** | **bool**|  | [optional] [default to False]
 **format** | **str**|  | [optional] [default to json]

### Return type

[**SslResponse**](SslResponse.md)

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

