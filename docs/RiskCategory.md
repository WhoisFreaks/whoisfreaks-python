# RiskCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdict** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 
**primary_threat** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**threat_types** | **List[str]** |  | [optional] 
**sources** | [**List[ThreatSource]**](ThreatSource.md) |  | [optional] 
**pivot_matches** | [**List[PivotMatch]**](PivotMatch.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.risk_category import RiskCategory

# TODO update the JSON string below
json = "{}"
# create an instance of RiskCategory from a JSON string
risk_category_instance = RiskCategory.from_json(json)
# print the JSON string representation of the object
print(RiskCategory.to_json())

# convert the object into a dict
risk_category_dict = risk_category_instance.to_dict()
# create an instance of RiskCategory from a dict
risk_category_from_dict = RiskCategory.from_dict(risk_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


