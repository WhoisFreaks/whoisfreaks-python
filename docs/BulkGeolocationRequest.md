# BulkGeolocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **List[str]** |  | 

## Example

```python
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGeolocationRequest from a JSON string
bulk_geolocation_request_instance = BulkGeolocationRequest.from_json(json)
# print the JSON string representation of the object
print(BulkGeolocationRequest.to_json())

# convert the object into a dict
bulk_geolocation_request_dict = bulk_geolocation_request_instance.to_dict()
# create an instance of BulkGeolocationRequest from a dict
bulk_geolocation_request_from_dict = BulkGeolocationRequest.from_dict(bulk_geolocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


