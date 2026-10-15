# DnsRecord

Union of all DNS record variants (A/AAAA/MX/NS/CNAME/PTR/TXT/SPF/SOA).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Numeric DNS record type: 1 A, 2 NS, 5 CNAME, 6 SOA, 12 PTR, 15 MX, 16 TXT, 28 AAAA, 99 SPF. | [optional] 
**dns_type** | **str** | Record type name, e.g. A, MX, TXT | [optional] 
**name** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 
**raw_text** | **str** | The record in zone-file format | [optional] 
**r_rset_type** | **int** |  | [optional] 
**single_name** | **str** | Target host for NS, CNAME and PTR records | [optional] 
**address** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**exchange** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**strings** | **List[str]** |  | [optional] 
**host** | **str** |  | [optional] 
**admin** | **str** |  | [optional] 
**serial** | **int** | SOA serial; values above 2^31 are common, so it is 64-bit | [optional] 
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


