# DomainAvailabilityItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**availability** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 

## Example

```python
from whoisfreaks.models.domain_availability_item import DomainAvailabilityItem

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAvailabilityItem from a JSON string
domain_availability_item_instance = DomainAvailabilityItem.from_json(json)
# print the JSON string representation of the object
print(DomainAvailabilityItem.to_json())

# convert the object into a dict
domain_availability_item_dict = domain_availability_item_instance.to_dict()
# create an instance of DomainAvailabilityItem from a dict
domain_availability_item_from_dict = DomainAvailabilityItem.from_dict(domain_availability_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


