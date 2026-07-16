# Irt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** |  | [optional] 
**address** | **List[str]** |  | [optional] 
**street** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**email** | **List[str]** |  | [optional] 
**abuse_mailbox** | **List[str]** |  | [optional] 
**phone** | **List[str]** |  | [optional] 
**fax_no** | **List[str]** |  | [optional] 
**organizations** | **List[str]** |  | [optional] 
**admin_contacts** | **List[str]** |  | [optional] 
**tech_contacts** | **List[str]** |  | [optional] 
**remarks** | **List[str]** |  | [optional] 
**signature** | **List[str]** |  | [optional] 
**encryption** | **List[str]** |  | [optional] 
**auth** | **List[str]** |  | [optional] 
**notify** | **List[str]** |  | [optional] 
**irt_nfy** | **List[str]** |  | [optional] 
**mnt_by** | **List[str]** |  | [optional] 
**mnt_ref** | **List[str]** |  | [optional] 

## Example

```python
from whoisfreaks.models.irt import Irt

# TODO update the JSON string below
json = "{}"
# create an instance of Irt from a JSON string
irt_instance = Irt.from_json(json)
# print the JSON string representation of the object
print(Irt.to_json())

# convert the object into a dict
irt_dict = irt_instance.to_dict()
# create an instance of Irt from a dict
irt_from_dict = Irt.from_dict(irt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


