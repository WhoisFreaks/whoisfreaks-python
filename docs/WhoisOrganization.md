# WhoisOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **List[str]** |  | [optional] 
**address** | **List[str]** |  | [optional] 
**street** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**country** | **List[str]** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**email** | **List[str]** |  | [optional] 
**abuse_mailbox** | **List[str]** |  | [optional] 
**phone** | **List[str]** |  | [optional] 
**fax_no** | **List[str]** |  | [optional] 
**organizations** | **List[str]** |  | [optional] 
**admin_contacts** | **List[str]** |  | [optional] 
**tech_contacts** | **List[str]** |  | [optional] 
**abuse_contacts** | **List[str]** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**remarks** | **List[str]** |  | [optional] 
**notify** | **List[str]** |  | [optional] 
**ref_nfy** | **List[str]** |  | [optional] 
**mnt_ref** | **List[str]** |  | [optional] 
**mnt_by** | **List[str]** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.whois_organization import WhoisOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of WhoisOrganization from a JSON string
whois_organization_instance = WhoisOrganization.from_json(json)
# print the JSON string representation of the object
print(WhoisOrganization.to_json())

# convert the object into a dict
whois_organization_dict = whois_organization_instance.to_dict()
# create an instance of WhoisOrganization from a dict
whois_organization_from_dict = WhoisOrganization.from_dict(whois_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


