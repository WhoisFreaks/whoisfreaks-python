# DatabaseFileStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newly** | [**NewlyStatus**](NewlyStatus.md) |  | [optional] 
**expired** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**cleaned_expired** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**dropped** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**dropped_with_backlinks** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**database_updates** | [**DatabaseUpdates**](DatabaseUpdates.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.database_file_status import DatabaseFileStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseFileStatus from a JSON string
database_file_status_instance = DatabaseFileStatus.from_json(json)
# print the JSON string representation of the object
print(DatabaseFileStatus.to_json())

# convert the object into a dict
database_file_status_dict = database_file_status_instance.to_dict()
# create an instance of DatabaseFileStatus from a dict
database_file_status_from_dict = DatabaseFileStatus.from_dict(database_file_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


