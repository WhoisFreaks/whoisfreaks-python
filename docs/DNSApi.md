# whoisfreaks.DNSApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_bulk**](DNSApi.md#dns_bulk) | **POST** /v2.0/dns/bulk/live | Bulk DNS Lookup
[**dns_historical**](DNSApi.md#dns_historical) | **GET** /v2.0/dns/historical | Historical DNS Lookup
[**dns_live**](DNSApi.md#dns_live) | **GET** /v2.0/dns/live | Live DNS Lookup
[**dns_reverse**](DNSApi.md#dns_reverse) | **GET** /v2.1/dns/reverse | Reverse DNS Lookup


# **dns_bulk**
> BulkDnsResponse dns_bulk(type, dns_bulk_request, format=format)

Bulk DNS Lookup

Up to 100 domains + 100 IPs in one request.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.bulk_dns_response import BulkDnsResponse
from whoisfreaks.models.dns_bulk_request import DnsBulkRequest
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
    api_instance = whoisfreaks.DNSApi(api_client)
    type = 'all' # str |  (default to 'all')
    dns_bulk_request = whoisfreaks.DnsBulkRequest() # DnsBulkRequest | 
    format = json # str |  (optional) (default to json)

    try:
        # Bulk DNS Lookup
        api_response = api_instance.dns_bulk(type, dns_bulk_request, format=format)
        print("The response of DNSApi->dns_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [default to &#39;all&#39;]
 **dns_bulk_request** | [**DnsBulkRequest**](DnsBulkRequest.md)|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**BulkDnsResponse**](BulkDnsResponse.md)

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

# **dns_historical**
> HistoricalDnsResponse dns_historical(domain_name, type, page=page, format=format)

Historical DNS Lookup

All historical DNS records. 2 credits per page (100 records/page).

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.historical_dns_response import HistoricalDnsResponse
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
    api_instance = whoisfreaks.DNSApi(api_client)
    domain_name = 'domain_name_example' # str | 
    type = 'all' # str |  (default to 'all')
    page = 1 # int |  (optional) (default to 1)
    format = json # str |  (optional) (default to json)

    try:
        # Historical DNS Lookup
        api_response = api_instance.dns_historical(domain_name, type, page=page, format=format)
        print("The response of DNSApi->dns_historical:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_historical: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_name** | **str**|  | 
 **type** | **str**|  | [default to &#39;all&#39;]
 **page** | **int**|  | [optional] [default to 1]
 **format** | **str**|  | [optional] [default to json]

### Return type

[**HistoricalDnsResponse**](HistoricalDnsResponse.md)

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

# **dns_live**
> DnsResponse dns_live(type, domain_name=domain_name, ip_address=ip_address, format=format)

Live DNS Lookup

Real-time DNS record lookup. 1 credit per query.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.dns_response import DnsResponse
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
    api_instance = whoisfreaks.DNSApi(api_client)
    type = 'all' # str | all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME (default to 'all')
    domain_name = 'domain_name_example' # str |  (optional)
    ip_address = 'ip_address_example' # str | Use for PTR lookups (optional)
    format = json # str |  (optional) (default to json)

    try:
        # Live DNS Lookup
        api_response = api_instance.dns_live(type, domain_name=domain_name, ip_address=ip_address, format=format)
        print("The response of DNSApi->dns_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME | [default to &#39;all&#39;]
 **domain_name** | **str**|  | [optional] 
 **ip_address** | **str**| Use for PTR lookups | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**DnsResponse**](DnsResponse.md)

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
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_reverse**
> ReverseDnsResponse dns_reverse(value, type, exact=exact, page=page, format=format)

Reverse DNS Lookup

Search domains by IP or DNS value. 5 credits per page.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import whoisfreaks
from whoisfreaks.models.reverse_dns_response import ReverseDnsResponse
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
    api_instance = whoisfreaks.DNSApi(api_client)
    value = 'value_example' # str | IP, CIDR, or record value
    type = 'type_example' # str | 
    exact = True # bool |  (optional) (default to True)
    page = 1 # int |  (optional) (default to 1)
    format = json # str |  (optional) (default to json)

    try:
        # Reverse DNS Lookup
        api_response = api_instance.dns_reverse(value, type, exact=exact, page=page, format=format)
        print("The response of DNSApi->dns_reverse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->dns_reverse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| IP, CIDR, or record value | 
 **type** | **str**|  | 
 **exact** | **bool**|  | [optional] [default to True]
 **page** | **int**|  | [optional] [default to 1]
 **format** | **str**|  | [optional] [default to json]

### Return type

[**ReverseDnsResponse**](ReverseDnsResponse.md)

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

