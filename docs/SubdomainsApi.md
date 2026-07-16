# whoisfreaks.SubdomainsApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subdomains**](SubdomainsApi.md#subdomains) | **GET** /v1.0/subdomains | Subdomains Lookup


# **subdomains**
> SubdomainsResponse subdomains(domain, after=after, before=before, status=status, page=page, format=format)

Subdomains Lookup

All subdomains including nested. 2 credits per query.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.subdomains_response import SubdomainsResponse
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
    api_instance = whoisfreaks.SubdomainsApi(api_client)
    domain = 'domain_example' # str | 
    after = '2013-10-20' # date |  (optional)
    before = '2013-10-20' # date |  (optional)
    status = 'status_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    format = json # str |  (optional) (default to json)

    try:
        # Subdomains Lookup
        api_response = api_instance.subdomains(domain, after=after, before=before, status=status, page=page, format=format)
        print("The response of SubdomainsApi->subdomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubdomainsApi->subdomains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 
 **after** | **date**|  | [optional] 
 **before** | **date**|  | [optional] 
 **status** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **format** | **str**|  | [optional] [default to json]

### Return type

[**SubdomainsResponse**](SubdomainsResponse.md)

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

