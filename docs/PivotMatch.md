# PivotMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pivot** | **str** |  | [optional] 
**pivot_type** | **str** |  | [optional] 
**total_related_threats** | **int** |  | [optional] 
**confidence** | **float** |  | [optional] 

## Example

```python
from whoisfreaks.models.pivot_match import PivotMatch

# TODO update the JSON string below
json = "{}"
# create an instance of PivotMatch from a JSON string
pivot_match_instance = PivotMatch.from_json(json)
# print the JSON string representation of the object
print(PivotMatch.to_json())

# convert the object into a dict
pivot_match_dict = pivot_match_instance.to_dict()
# create an instance of PivotMatch from a dict
pivot_match_from_dict = PivotMatch.from_dict(pivot_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


