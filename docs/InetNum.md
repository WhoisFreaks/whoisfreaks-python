# InetNum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_ip** | **str** |  | [optional] 
**end_ip** | **str** |  | [optional] 
**cidr** | **List[str]** |  | [optional] 
**net_name** | **str** |  | [optional] 
**net_handle** | **str** |  | [optional] 
**description** | **List[str]** |  | [optional] 
**countries** | **List[str]** |  | [optional] 
**geofeed** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**city** | **str** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**sponsoring_organization** | **str** |  | [optional] 
**remarks** | **List[str]** |  | [optional] 
**assignment_size** | **str** |  | [optional] 
**notify** | **List[str]** |  | [optional] 
**mnt_by** | **List[str]** |  | [optional] 
**mnt_lower** | **List[str]** |  | [optional] 
**mnt_domains** | **List[str]** |  | [optional] 
**mnt_routes** | **List[str]** |  | [optional] 
**mnt_irt** | **List[str]** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**parents** | **List[str]** |  | [optional] 

## Example

```python
from whoisfreaks.models.inet_num import InetNum

# TODO update the JSON string below
json = "{}"
# create an instance of InetNum from a JSON string
inet_num_instance = InetNum.from_json(json)
# print the JSON string representation of the object
print(InetNum.to_json())

# convert the object into a dict
inet_num_dict = inet_num_instance.to_dict()
# create an instance of InetNum from a dict
inet_num_from_dict = InetNum.from_dict(inet_num_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


