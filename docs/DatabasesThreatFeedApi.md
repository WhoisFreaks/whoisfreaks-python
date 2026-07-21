# whoisfreaks.DatabasesThreatFeedApi

All URIs are relative to *https://api.whoisfreaks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_threat_feed_malware**](DatabasesThreatFeedApi.md#download_threat_feed_malware) | **GET** /v3.4/download/threat-feed/malware | Download the daily malware threat feed (CSV)
[**download_threat_feed_malware_sample**](DatabasesThreatFeedApi.md#download_threat_feed_malware_sample) | **GET** /v3.4/download/threat-feed/malware/sample | Download a sample of the malware threat feed (CSV)
[**download_threat_feed_phishing**](DatabasesThreatFeedApi.md#download_threat_feed_phishing) | **GET** /v3.4/download/threat-feed/phishing | Download the daily phishing threat feed (CSV)
[**download_threat_feed_phishing_sample**](DatabasesThreatFeedApi.md#download_threat_feed_phishing_sample) | **GET** /v3.4/download/threat-feed/phishing/sample | Download a sample of the phishing threat feed (CSV)
[**download_threat_feed_spam**](DatabasesThreatFeedApi.md#download_threat_feed_spam) | **GET** /v3.4/download/threat-feed/spam | Download the daily spam threat feed (CSV)
[**download_threat_feed_spam_sample**](DatabasesThreatFeedApi.md#download_threat_feed_spam_sample) | **GET** /v3.4/download/threat-feed/spam/sample | Download a sample of the spam threat feed (CSV)


# **download_threat_feed_malware**
> bytearray download_threat_feed_malware(var_date=var_date)

Download the daily malware threat feed (CSV)

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
    api_instance = whoisfreaks.DatabasesThreatFeedApi(api_client)
    var_date = 'var_date_example' # str | Feed date (yyyy-MM-dd); defaults to latest available (optional)

    try:
        # Download the daily malware threat feed (CSV)
        api_response = api_instance.download_threat_feed_malware(var_date=var_date)
        print("The response of DatabasesThreatFeedApi->download_threat_feed_malware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesThreatFeedApi->download_threat_feed_malware: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Feed date (yyyy-MM-dd); defaults to latest available | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Malware threat feed as CSV (domain,threat_type,confidence,first_seen,last_seen,No_of_threat_matched_pivots) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_threat_feed_malware_sample**
> bytearray download_threat_feed_malware_sample()

Download a sample of the malware threat feed (CSV)

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
    api_instance = whoisfreaks.DatabasesThreatFeedApi(api_client)

    try:
        # Download a sample of the malware threat feed (CSV)
        api_response = api_instance.download_threat_feed_malware_sample()
        print("The response of DatabasesThreatFeedApi->download_threat_feed_malware_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesThreatFeedApi->download_threat_feed_malware_sample: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample malware threat feed as CSV |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_threat_feed_phishing**
> bytearray download_threat_feed_phishing(var_date=var_date)

Download the daily phishing threat feed (CSV)

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
    api_instance = whoisfreaks.DatabasesThreatFeedApi(api_client)
    var_date = 'var_date_example' # str | Feed date (yyyy-MM-dd); defaults to latest available (optional)

    try:
        # Download the daily phishing threat feed (CSV)
        api_response = api_instance.download_threat_feed_phishing(var_date=var_date)
        print("The response of DatabasesThreatFeedApi->download_threat_feed_phishing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesThreatFeedApi->download_threat_feed_phishing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Feed date (yyyy-MM-dd); defaults to latest available | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Phishing threat feed as CSV (domain,threat_type,confidence,first_seen,last_seen,No_of_threat_matched_pivots) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_threat_feed_phishing_sample**
> bytearray download_threat_feed_phishing_sample()

Download a sample of the phishing threat feed (CSV)

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
    api_instance = whoisfreaks.DatabasesThreatFeedApi(api_client)

    try:
        # Download a sample of the phishing threat feed (CSV)
        api_response = api_instance.download_threat_feed_phishing_sample()
        print("The response of DatabasesThreatFeedApi->download_threat_feed_phishing_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesThreatFeedApi->download_threat_feed_phishing_sample: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample phishing threat feed as CSV |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_threat_feed_spam**
> bytearray download_threat_feed_spam(var_date=var_date)

Download the daily spam threat feed (CSV)

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
    api_instance = whoisfreaks.DatabasesThreatFeedApi(api_client)
    var_date = 'var_date_example' # str | Feed date (yyyy-MM-dd); defaults to latest available (optional)

    try:
        # Download the daily spam threat feed (CSV)
        api_response = api_instance.download_threat_feed_spam(var_date=var_date)
        print("The response of DatabasesThreatFeedApi->download_threat_feed_spam:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesThreatFeedApi->download_threat_feed_spam: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| Feed date (yyyy-MM-dd); defaults to latest available | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Spam threat feed as CSV (domain,threat_type,confidence,first_seen,last_seen,No_of_threat_matched_pivots) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_threat_feed_spam_sample**
> bytearray download_threat_feed_spam_sample()

Download a sample of the spam threat feed (CSV)

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
    api_instance = whoisfreaks.DatabasesThreatFeedApi(api_client)

    try:
        # Download a sample of the spam threat feed (CSV)
        api_response = api_instance.download_threat_feed_spam_sample()
        print("The response of DatabasesThreatFeedApi->download_threat_feed_spam_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesThreatFeedApi->download_threat_feed_spam_sample: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sample spam threat feed as CSV |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

