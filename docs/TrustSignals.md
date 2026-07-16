# TrustSignals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trust_score** | **int** |  | [optional] 
**trust_band** | **str** |  | [optional] 
**signals** | [**ReputationSignals**](ReputationSignals.md) |  | [optional] 
**indicators** | [**ReputationIndicators**](ReputationIndicators.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.trust_signals import TrustSignals

# TODO update the JSON string below
json = "{}"
# create an instance of TrustSignals from a JSON string
trust_signals_instance = TrustSignals.from_json(json)
# print the JSON string representation of the object
print(TrustSignals.to_json())

# convert the object into a dict
trust_signals_dict = trust_signals_instance.to_dict()
# create an instance of TrustSignals from a dict
trust_signals_from_dict = TrustSignals.from_dict(trust_signals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


