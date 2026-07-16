# DnsResponse

Live DNS response (DnsInfo).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**query_time** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**domain_registered** | **bool** |  | [optional] 
**dns_types** | **object** |  | [optional] 
**dns_records** | [**List[DnsRecord]**](DnsRecord.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.dns_response import DnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnsResponse from a JSON string
dns_response_instance = DnsResponse.from_json(json)
# print the JSON string representation of the object
print(DnsResponse.to_json())

# convert the object into a dict
dns_response_dict = dns_response_instance.to_dict()
# create an instance of DnsResponse from a dict
dns_response_from_dict = DnsResponse.from_dict(dns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


