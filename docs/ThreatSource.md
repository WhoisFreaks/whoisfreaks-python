# ThreatSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**indicator** | **str** |  | [optional] 
**threat_type** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 
**first_seen** | **str** |  | [optional] 
**last_seen** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.threat_source import ThreatSource

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatSource from a JSON string
threat_source_instance = ThreatSource.from_json(json)
# print the JSON string representation of the object
print(ThreatSource.to_json())

# convert the object into a dict
threat_source_dict = threat_source_instance.to_dict()
# create an instance of ThreatSource from a dict
threat_source_from_dict = ThreatSource.from_dict(threat_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


