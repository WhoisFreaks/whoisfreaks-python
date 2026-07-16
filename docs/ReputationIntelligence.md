# ReputationIntelligence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ioc_type** | **str** |  | [optional] 
**ioc_value** | **str** |  | [optional] 
**related_iocs** | [**List[RelatedIoc]**](RelatedIoc.md) |  | [optional] 
**feed_tags** | **List[str]** |  | [optional] 
**stix_pattern** | **str** |  | [optional] 
**recommended_action** | **str** |  | [optional] 
**first_seen** | **str** |  | [optional] 
**last_seen** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.reputation_intelligence import ReputationIntelligence

# TODO update the JSON string below
json = "{}"
# create an instance of ReputationIntelligence from a JSON string
reputation_intelligence_instance = ReputationIntelligence.from_json(json)
# print the JSON string representation of the object
print(ReputationIntelligence.to_json())

# convert the object into a dict
reputation_intelligence_dict = reputation_intelligence_instance.to_dict()
# create an instance of ReputationIntelligence from a dict
reputation_intelligence_from_dict = ReputationIntelligence.from_dict(reputation_intelligence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


