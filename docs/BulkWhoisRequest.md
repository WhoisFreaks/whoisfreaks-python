# BulkWhoisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_names** | **List[str]** |  | 

## Example

```python
from whoisfreaks.models.bulk_whois_request import BulkWhoisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkWhoisRequest from a JSON string
bulk_whois_request_instance = BulkWhoisRequest.from_json(json)
# print the JSON string representation of the object
print(BulkWhoisRequest.to_json())

# convert the object into a dict
bulk_whois_request_dict = bulk_whois_request_instance.to_dict()
# create an instance of BulkWhoisRequest from a dict
bulk_whois_request_from_dict = BulkWhoisRequest.from_dict(bulk_whois_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


