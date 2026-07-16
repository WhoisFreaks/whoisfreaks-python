# BulkDomainAvailabilityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_domain_availability_response** | [**List[DomainAvailabilityItem]**](DomainAvailabilityItem.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.bulk_domain_availability_response import BulkDomainAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDomainAvailabilityResponse from a JSON string
bulk_domain_availability_response_instance = BulkDomainAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print(BulkDomainAvailabilityResponse.to_json())

# convert the object into a dict
bulk_domain_availability_response_dict = bulk_domain_availability_response_instance.to_dict()
# create an instance of BulkDomainAvailabilityResponse from a dict
bulk_domain_availability_response_from_dict = BulkDomainAvailabilityResponse.from_dict(bulk_domain_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


