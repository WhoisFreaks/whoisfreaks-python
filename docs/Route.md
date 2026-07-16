# Route


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route** | **str** |  | [optional] 
**description** | **List[str]** |  | [optional] 
**origin** | **str** |  | [optional] 
**pingable** | **List[str]** |  | [optional] 
**ping_hdl** | **List[str]** |  | [optional] 
**holes** | **List[str]** |  | [optional] 
**country** | **str** |  | [optional] 
**organizations** | **List[str]** |  | [optional] 
**member_of** | **List[str]** |  | [optional] 
**inject** | **List[str]** |  | [optional] 
**aggr_mtd** | **str** |  | [optional] 
**aggr_bndry** | **str** |  | [optional] 
**export_comps** | **str** |  | [optional] 
**components** | **str** |  | [optional] 
**remarks** | **List[str]** |  | [optional] 
**notify** | **List[str]** |  | [optional] 
**mnt_lower** | **List[str]** |  | [optional] 
**mnt_routes** | **List[str]** |  | [optional] 
**mnt_by** | **List[str]** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print(Route.to_json())

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_from_dict = Route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


