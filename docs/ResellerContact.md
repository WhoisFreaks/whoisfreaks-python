# ResellerContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.reseller_contact import ResellerContact

# TODO update the JSON string below
json = "{}"
# create an instance of ResellerContact from a JSON string
reseller_contact_instance = ResellerContact.from_json(json)
# print the JSON string representation of the object
print(ResellerContact.to_json())

# convert the object into a dict
reseller_contact_dict = reseller_contact_instance.to_dict()
# create an instance of ResellerContact from a dict
reseller_contact_from_dict = ResellerContact.from_dict(reseller_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


