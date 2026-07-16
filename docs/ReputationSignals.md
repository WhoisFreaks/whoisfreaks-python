# ReputationSignals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive** | [**List[ReputationSignal]**](ReputationSignal.md) |  | [optional] 
**negative** | [**List[ReputationSignal]**](ReputationSignal.md) |  | [optional] 
**neutral** | [**List[ReputationSignal]**](ReputationSignal.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.reputation_signals import ReputationSignals

# TODO update the JSON string below
json = "{}"
# create an instance of ReputationSignals from a JSON string
reputation_signals_instance = ReputationSignals.from_json(json)
# print the JSON string representation of the object
print(ReputationSignals.to_json())

# convert the object into a dict
reputation_signals_dict = reputation_signals_instance.to_dict()
# create an instance of ReputationSignals from a dict
reputation_signals_from_dict = ReputationSignals.from_dict(reputation_signals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


