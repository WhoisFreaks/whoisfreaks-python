# TyposquattingDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** |  | [optional] 
**create_date** | **str** |  | [optional] 
**expiry_date** | **str** |  | [optional] 
**last_seen** | **str** |  | [optional] 
**is_dropped** | **bool** |  | [optional] 

## Example

```python
from whoisfreaks.models.typosquatting_domain import TyposquattingDomain

# TODO update the JSON string below
json = "{}"
# create an instance of TyposquattingDomain from a JSON string
typosquatting_domain_instance = TyposquattingDomain.from_json(json)
# print the JSON string representation of the object
print(TyposquattingDomain.to_json())

# convert the object into a dict
typosquatting_domain_dict = typosquatting_domain_instance.to_dict()
# create an instance of TyposquattingDomain from a dict
typosquatting_domain_from_dict = TyposquattingDomain.from_dict(typosquatting_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


