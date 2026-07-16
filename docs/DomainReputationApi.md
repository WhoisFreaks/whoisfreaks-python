# whoisfreaks.DomainReputationApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_reputation**](DomainReputationApi.md#domain_reputation) | **GET** /v1/domain/security | Domain Reputation Lookup


# **domain_reputation**
> DomainReputationResponse domain_reputation(domain_name, format=format)

Domain Reputation Lookup

Real-time domain threat assessment. Returns risk verdict, trust score, DGA analysis, threat intelligence matches, and security signals. 1 credit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.domain_reputation_response import DomainReputationResponse
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
    api_instance = whoisfreaks.DomainReputationApi(api_client)
    domain_name = 'amazon.com' # str | The domain name to assess
    format = json # str |  (optional) (default to json)

    try:
        # Domain Reputation Lookup
        api_response = api_instance.domain_reputation(domain_name, format=format)
        print("The response of DomainReputationApi->domain_reputation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainReputationApi->domain_reputation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**| The domain name to assess | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**DomainReputationResponse**](DomainReputationResponse.md)

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
**404** | Not found |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

