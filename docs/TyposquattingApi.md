# whoisfreaks.TyposquattingApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**typosquatting**](TyposquattingApi.md#typosquatting) | **GET** /v3.0/domain/typos | Typosquatting Lookup


# **typosquatting**
> TyposquattingResponse typosquatting(keyword=keyword, pattern=pattern, page_token=page_token)

Typosquatting Lookup

Find typo variants of a brand. 5 credits per page.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.typosquatting_response import TyposquattingResponse
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
    api_instance = whoisfreaks.TyposquattingApi(api_client)
    keyword = 'whoisfreaks' # str |  (optional)
    pattern = 'whois*' # str |  (optional)
    page_token = 'page_token_example' # str |  (optional)

    try:
        # Typosquatting Lookup
        api_response = api_instance.typosquatting(keyword=keyword, pattern=pattern, page_token=page_token)
        print("The response of TyposquattingApi->typosquatting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TyposquattingApi->typosquatting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**|  | [optional] 
 **pattern** | **str**|  | [optional] 
 **page_token** | **str**|  | [optional] 

### Return type

[**TyposquattingResponse**](TyposquattingResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Invalid API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

