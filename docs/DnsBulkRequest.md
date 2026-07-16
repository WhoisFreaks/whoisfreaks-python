# DnsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_names** | **List[str]** |  | [optional] 
**ip_addresses** | **List[str]** |  | [optional] 

## Example

```python
from whoisfreaks.models.dns_bulk_request import DnsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DnsBulkRequest from a JSON string
dns_bulk_request_instance = DnsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(DnsBulkRequest.to_json())

# convert the object into a dict
dns_bulk_request_dict = dns_bulk_request_instance.to_dict()
# create an instance of DnsBulkRequest from a dict
dns_bulk_request_from_dict = DnsBulkRequest.from_dict(dns_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


