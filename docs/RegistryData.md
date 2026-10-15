# RegistryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** |  | [optional] 
**query_time** | **str** |  | [optional] 
**whois_server** | **str** |  | [optional] 
**domain_registered** | **str** |  | [optional] 
**create_date** | **str** |  | [optional] 
**update_date** | **str** |  | [optional] 
**expiry_date** | **str** |  | [optional] 
**domain_registrar** | [**RegistrarInformation**](RegistrarInformation.md) |  | [optional] 
**name_servers** | **List[str]** |  | [optional] 
**domain_status** | **List[str]** |  | [optional] 
**whois_raw_registery** | **str** | Raw registry WHOIS text (field name spelled as the API returns it) | [optional] 

## Example

```python
from whoisfreaks.models.registry_data import RegistryData

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryData from a JSON string
registry_data_instance = RegistryData.from_json(json)
# print the JSON string representation of the object
print(RegistryData.to_json())

# convert the object into a dict
registry_data_dict = registry_data_instance.to_dict()
# create an instance of RegistryData from a dict
registry_data_from_dict = RegistryData.from_dict(registry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


