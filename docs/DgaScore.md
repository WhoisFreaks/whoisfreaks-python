# DgaScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** |  | [optional] 
**is_dga** | **bool** |  | [optional] 
**model** | **str** |  | [optional] 
**features** | [**DgaFeatures**](DgaFeatures.md) |  | [optional] 
**interpretation** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.dga_score import DgaScore

# TODO update the JSON string below
json = "{}"
# create an instance of DgaScore from a JSON string
dga_score_instance = DgaScore.from_json(json)
# print the JSON string representation of the object
print(DgaScore.to_json())

# convert the object into a dict
dga_score_dict = dga_score_instance.to_dict()
# create an instance of DgaScore from a dict
dga_score_from_dict = DgaScore.from_dict(dga_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


