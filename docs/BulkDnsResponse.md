# BulkDnsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_dns_info** | [**List[DnsResponse]**](DnsResponse.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.bulk_dns_response import BulkDnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDnsResponse from a JSON string
bulk_dns_response_instance = BulkDnsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkDnsResponse.to_json())

# convert the object into a dict
bulk_dns_response_dict = bulk_dns_response_instance.to_dict()
# create an instance of BulkDnsResponse from a dict
bulk_dns_response_from_dict = BulkDnsResponse.from_dict(bulk_dns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


