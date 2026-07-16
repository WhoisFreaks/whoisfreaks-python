# UpdateFrequencies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**weekly** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**monthly** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.update_frequencies import UpdateFrequencies

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFrequencies from a JSON string
update_frequencies_instance = UpdateFrequencies.from_json(json)
# print the JSON string representation of the object
print(UpdateFrequencies.to_json())

# convert the object into a dict
update_frequencies_dict = update_frequencies_instance.to_dict()
# create an instance of UpdateFrequencies from a dict
update_frequencies_from_dict = UpdateFrequencies.from_dict(update_frequencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


