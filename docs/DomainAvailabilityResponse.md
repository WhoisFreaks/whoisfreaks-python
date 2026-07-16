# DomainAvailabilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**availability** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**domain_available_response** | [**List[DomainAvailabilityItem]**](DomainAvailabilityItem.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.domain_availability_response import DomainAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAvailabilityResponse from a JSON string
domain_availability_response_instance = DomainAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print(DomainAvailabilityResponse.to_json())

# convert the object into a dict
domain_availability_response_dict = domain_availability_response_instance.to_dict()
# create an instance of DomainAvailabilityResponse from a dict
domain_availability_response_from_dict = DomainAvailabilityResponse.from_dict(domain_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


