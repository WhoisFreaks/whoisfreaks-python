# GeoNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | [**GeoAsn**](GeoAsn.md) |  | [optional] 
**connection_type** | **str** |  | [optional] 
**company** | [**GeoCompany**](GeoCompany.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.geo_network import GeoNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNetwork from a JSON string
geo_network_instance = GeoNetwork.from_json(json)
# print the JSON string representation of the object
print(GeoNetwork.to_json())

# convert the object into a dict
geo_network_dict = geo_network_instance.to_dict()
# create an instance of GeoNetwork from a dict
geo_network_from_dict = GeoNetwork.from_dict(geo_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


