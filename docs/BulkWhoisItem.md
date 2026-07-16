# BulkWhoisItem

One bulk WHOIS result; success items also carry all WhoisResponse fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.bulk_whois_item import BulkWhoisItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkWhoisItem from a JSON string
bulk_whois_item_instance = BulkWhoisItem.from_json(json)
# print the JSON string representation of the object
print(BulkWhoisItem.to_json())

# convert the object into a dict
bulk_whois_item_dict = bulk_whois_item_instance.to_dict()
# create an instance of BulkWhoisItem from a dict
bulk_whois_item_from_dict = BulkWhoisItem.from_dict(bulk_whois_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


