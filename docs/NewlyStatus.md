# NewlyStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gtld** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**cctld** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**dns** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**cleaned_gtld** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**cleaned_cctld** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.newly_status import NewlyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NewlyStatus from a JSON string
newly_status_instance = NewlyStatus.from_json(json)
# print the JSON string representation of the object
print(NewlyStatus.to_json())

# convert the object into a dict
newly_status_dict = newly_status_instance.to_dict()
# create an instance of NewlyStatus from a dict
newly_status_from_dict = NewlyStatus.from_dict(newly_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


