# PersonalInformation

Contact block (registrant/administrative/technical/billing).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**id_type** | **str** |  | [optional] 
**handle** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**mailing_address** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.personal_information import PersonalInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalInformation from a JSON string
personal_information_instance = PersonalInformation.from_json(json)
# print the JSON string representation of the object
print(PersonalInformation.to_json())

# convert the object into a dict
personal_information_dict = personal_information_instance.to_dict()
# create an instance of PersonalInformation from a dict
personal_information_from_dict = PersonalInformation.from_dict(personal_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


