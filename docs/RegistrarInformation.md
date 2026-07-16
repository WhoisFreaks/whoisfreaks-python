# RegistrarInformation

Registrar details (used by domain_registrar, abuse_contact).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**id_type** | **str** |  | [optional] 
**iana_id** | **str** |  | [optional] 
**registry_id** | **str** |  | [optional] 
**handle** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**registrar_name** | **str** |  | [optional] 
**normalized_name** | **str** |  | [optional] 
**whois_server** | **str** |  | [optional] 
**rdap_server** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**authoritative_registry_name** | **str** |  | [optional] 
**organization_number** | **str** |  | [optional] 
**is_sponsor** | **bool** |  | [optional] 

## Example

```python
from whoisfreaks.models.registrar_information import RegistrarInformation

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrarInformation from a JSON string
registrar_information_instance = RegistrarInformation.from_json(json)
# print the JSON string representation of the object
print(RegistrarInformation.to_json())

# convert the object into a dict
registrar_information_dict = registrar_information_instance.to_dict()
# create an instance of RegistrarInformation from a dict
registrar_information_from_dict = RegistrarInformation.from_dict(registrar_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


