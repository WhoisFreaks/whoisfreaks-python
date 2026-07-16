# BulkWhoisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_whois_response** | [**List[BulkWhoisItem]**](BulkWhoisItem.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.bulk_whois_response import BulkWhoisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkWhoisResponse from a JSON string
bulk_whois_response_instance = BulkWhoisResponse.from_json(json)
# print the JSON string representation of the object
print(BulkWhoisResponse.to_json())

# convert the object into a dict
bulk_whois_response_dict = bulk_whois_response_instance.to_dict()
# create an instance of BulkWhoisResponse from a dict
bulk_whois_response_from_dict = BulkWhoisResponse.from_dict(bulk_whois_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


