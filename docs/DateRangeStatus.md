# DateRangeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_from** | **str** |  | [optional] 
**last_update** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.date_range_status import DateRangeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DateRangeStatus from a JSON string
date_range_status_instance = DateRangeStatus.from_json(json)
# print the JSON string representation of the object
print(DateRangeStatus.to_json())

# convert the object into a dict
date_range_status_dict = date_range_status_instance.to_dict()
# create an instance of DateRangeStatus from a dict
date_range_status_from_dict = DateRangeStatus.from_dict(date_range_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


