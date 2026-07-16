# IpLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continent_code** | **str** |  | [optional] 
**continent_name** | **str** |  | [optional] 
**country_code2** | **str** |  | [optional] 
**country_code3** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**country_name_official** | **str** |  | [optional] 
**country_capital** | **str** |  | [optional] 
**state_prov** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**locality** | **str** |  | [optional] 
**accuracy_radius** | **str** |  | [optional] 
**confidence** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**is_eu** | **bool** |  | [optional] 
**geoname_id** | **str** |  | [optional] 
**country_emoji** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.ip_location import IpLocation

# TODO update the JSON string below
json = "{}"
# create an instance of IpLocation from a JSON string
ip_location_instance = IpLocation.from_json(json)
# print the JSON string representation of the object
print(IpLocation.to_json())

# convert the object into a dict
ip_location_dict = ip_location_instance.to_dict()
# create an instance of IpLocation from a dict
ip_location_from_dict = IpLocation.from_dict(ip_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


