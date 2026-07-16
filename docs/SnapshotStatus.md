# SnapshotStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**snapshot_creation_date** | **str** |  | [optional] 
**snapshot_name** | **str** |  | [optional] 
**snapshot_deletion_time** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.snapshot_status import SnapshotStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotStatus from a JSON string
snapshot_status_instance = SnapshotStatus.from_json(json)
# print the JSON string representation of the object
print(SnapshotStatus.to_json())

# convert the object into a dict
snapshot_status_dict = snapshot_status_instance.to_dict()
# create an instance of SnapshotStatus from a dict
snapshot_status_from_dict = SnapshotStatus.from_dict(snapshot_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


