# ReputationSignal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**polarity** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**evidence** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 

## Example

```python
from whoisfreaks.models.reputation_signal import ReputationSignal

# TODO update the JSON string below
json = "{}"
# create an instance of ReputationSignal from a JSON string
reputation_signal_instance = ReputationSignal.from_json(json)
# print the JSON string representation of the object
print(ReputationSignal.to_json())

# convert the object into a dict
reputation_signal_dict = reputation_signal_instance.to_dict()
# create an instance of ReputationSignal from a dict
reputation_signal_from_dict = ReputationSignal.from_dict(reputation_signal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


