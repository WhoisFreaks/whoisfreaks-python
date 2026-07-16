# GeoAsn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**asn_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**date_allocated** | **str** |  | [optional] 
**allocation_status** | **str** |  | [optional] 
**num_of_ipv4_routes** | **str** |  | [optional] 
**num_of_ipv6_routes** | **str** |  | [optional] 
**rir** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.geo_asn import GeoAsn

# TODO update the JSON string below
json = "{}"
# create an instance of GeoAsn from a JSON string
geo_asn_instance = GeoAsn.from_json(json)
# print the JSON string representation of the object
print(GeoAsn.to_json())

# convert the object into a dict
geo_asn_dict = geo_asn_instance.to_dict()
# create an instance of GeoAsn from a dict
geo_asn_from_dict = GeoAsn.from_dict(geo_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


