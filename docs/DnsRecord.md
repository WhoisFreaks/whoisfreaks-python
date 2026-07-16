# DnsRecord

Union of all DNS record variants (A/AAAA/MX/NS/CNAME/PTR/TXT/SPF/SOA).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 
**address** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**exchange** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**strings** | **List[str]** |  | [optional] 
**host** | **str** |  | [optional] 
**admin** | **str** |  | [optional] 
**serial** | **int** |  | [optional] 
**refresh** | **int** |  | [optional] 
**retry** | **int** |  | [optional] 
**expire** | **int** |  | [optional] 
**minimum** | **int** |  | [optional] 

## Example

```python
from whoisfreaks.models.dns_record import DnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecord from a JSON string
dns_record_instance = DnsRecord.from_json(json)
# print the JSON string representation of the object
print(DnsRecord.to_json())

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DnsRecord from a dict
dns_record_from_dict = DnsRecord.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


