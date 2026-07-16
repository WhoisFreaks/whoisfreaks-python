# ReputationIndicators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_newly_registered** | **bool** |  | [optional] 
**uses_free_extension** | **bool** |  | [optional] 
**uses_free_ssl** | **bool** |  | [optional] 
**has_privacy_whois** | **bool** |  | [optional] 
**ssl_age_days** | **int** |  | [optional] 
**has_dmarc** | **bool** |  | [optional] 
**has_spf** | **bool** |  | [optional] 
**redirects_externally** | **bool** |  | [optional] 
**javascript_obfuscated** | **bool** |  | [optional] 
**domain_age_days** | **int** |  | [optional] 
**registrar** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.reputation_indicators import ReputationIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of ReputationIndicators from a JSON string
reputation_indicators_instance = ReputationIndicators.from_json(json)
# print the JSON string representation of the object
print(ReputationIndicators.to_json())

# convert the object into a dict
reputation_indicators_dict = reputation_indicators_instance.to_dict()
# create an instance of ReputationIndicators from a dict
reputation_indicators_from_dict = ReputationIndicators.from_dict(reputation_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


