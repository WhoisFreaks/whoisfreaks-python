# SslUnitInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**organizational_unit** | **str** |  | [optional] 
**locality** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**inc_country** | **str** |  | [optional] 
**inc_state** | **str** |  | [optional] 
**business_category** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_unit_info import SslUnitInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SslUnitInfo from a JSON string
ssl_unit_info_instance = SslUnitInfo.from_json(json)
# print the JSON string representation of the object
print(SslUnitInfo.to_json())

# convert the object into a dict
ssl_unit_info_dict = ssl_unit_info_instance.to_dict()
# create an instance of SslUnitInfo from a dict
ssl_unit_info_from_dict = SslUnitInfo.from_dict(ssl_unit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


