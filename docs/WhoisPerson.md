# WhoisPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
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
**notify** | **List[str]** |  | [optional] 
**mnt_by** | **List[str]** |  | [optional] 
**mnt_ref** | **List[str]** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.whois_person import WhoisPerson

# TODO update the JSON string below
json = "{}"
# create an instance of WhoisPerson from a JSON string
whois_person_instance = WhoisPerson.from_json(json)
# print the JSON string representation of the object
print(WhoisPerson.to_json())

# convert the object into a dict
whois_person_dict = whois_person_instance.to_dict()
# create an instance of WhoisPerson from a dict
whois_person_from_dict = WhoisPerson.from_dict(whois_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


