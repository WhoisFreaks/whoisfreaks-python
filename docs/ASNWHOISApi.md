# whoisfreaks.ASNWHOISApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asn_whois**](ASNWHOISApi.md#asn_whois) | **GET** /v2.0/asn-whois | ASN WHOIS Lookup


# **asn_whois**
> AsnWhoisResponse asn_whois(asn, format=format)

ASN WHOIS Lookup

WHOIS for an ASN. 1 credit.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.asn_whois_response import AsnWhoisResponse
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
    api_instance = whoisfreaks.ASNWHOISApi(api_client)
    asn = 'as15169' # str | 
    format = json # str |  (optional) (default to json)

    try:
        # ASN WHOIS Lookup
        api_response = api_instance.asn_whois(asn, format=format)
        print("The response of ASNWHOISApi->asn_whois:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ASNWHOISApi->asn_whois: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asn** | **str**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**AsnWhoisResponse**](AsnWhoisResponse.md)

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

