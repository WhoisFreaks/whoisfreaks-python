# whoisfreaks.DomainAvailabilityApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_domain_availability_v2**](DomainAvailabilityApi.md#bulk_domain_availability_v2) | **POST** /v2.0/domain/availability | Bulk Domain Availability Check
[**domain_availability_v2**](DomainAvailabilityApi.md#domain_availability_v2) | **GET** /v2.0/domain/availability | Domain Availability Check with Suggestions


# **bulk_domain_availability_v2**
> BulkDomainAvailabilityResponse bulk_domain_availability_v2(bulk_domain_availability_request, domain=domain, format=format)

Bulk Domain Availability Check

Two bulk modes. Mode 1: POST domainNames array. Mode 2: POST tld array plus domain query param. Max 100 domains per request. 1 credit per domain checked.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.bulk_domain_availability_request import BulkDomainAvailabilityRequest
from whoisfreaks.models.bulk_domain_availability_response import BulkDomainAvailabilityResponse
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
    api_instance = whoisfreaks.DomainAvailabilityApi(api_client)
    bulk_domain_availability_request = whoisfreaks.BulkDomainAvailabilityRequest() # BulkDomainAvailabilityRequest | 
    domain = 'google.com' # str | Required for TLD-mode bulk check (base domain). (optional)
    format = json # str |  (optional) (default to json)

    try:
        # Bulk Domain Availability Check
        api_response = api_instance.bulk_domain_availability_v2(bulk_domain_availability_request, domain=domain, format=format)
        print("The response of DomainAvailabilityApi->bulk_domain_availability_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAvailabilityApi->bulk_domain_availability_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_domain_availability_request** | [**BulkDomainAvailabilityRequest**](BulkDomainAvailabilityRequest.md)|  | 
 **domain** | **str**| Required for TLD-mode bulk check (base domain). | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**BulkDomainAvailabilityResponse**](BulkDomainAvailabilityResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Invalid API key |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_availability_v2**
> DomainAvailabilityResponse domain_availability_v2(domain, sug=sug, count=count, format=format)

Domain Availability Check with Suggestions

Check availability of a single domain and optionally get suggestions across multiple TLDs. 1 credit per domain checked. sug=false checks only the queried domain; sug=true returns up to `count` (max 100) TLD suggestions.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.domain_availability_response import DomainAvailabilityResponse
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
    api_instance = whoisfreaks.DomainAvailabilityApi(api_client)
    domain = 'google.com' # str | The domain name to check
    sug = False # bool | Whether to return TLD suggestions alongside the queried domain. (optional) (default to False)
    count = 5 # int | Number of TLD suggestions to return when sug=true. Maximum is 100. (optional) (default to 5)
    format = json # str |  (optional) (default to json)

    try:
        # Domain Availability Check with Suggestions
        api_response = api_instance.domain_availability_v2(domain, sug=sug, count=count, format=format)
        print("The response of DomainAvailabilityApi->domain_availability_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAvailabilityApi->domain_availability_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain name to check | 
 **sug** | **bool**| Whether to return TLD suggestions alongside the queried domain. | [optional] [default to False]
 **count** | **int**| Number of TLD suggestions to return when sug&#x3D;true. Maximum is 100. | [optional] [default to 5]
 **format** | **str**|  | [optional] [default to json]

### Return type

[**DomainAvailabilityResponse**](DomainAvailabilityResponse.md)

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
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

