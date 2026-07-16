# DomainReputationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.domain_reputation_input import DomainReputationInput

# TODO update the JSON string below
json = "{}"
# create an instance of DomainReputationInput from a JSON string
domain_reputation_input_instance = DomainReputationInput.from_json(json)
# print the JSON string representation of the object
print(DomainReputationInput.to_json())

# convert the object into a dict
domain_reputation_input_dict = domain_reputation_input_instance.to_dict()
# create an instance of DomainReputationInput from a dict
domain_reputation_input_from_dict = DomainReputationInput.from_dict(domain_reputation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


