# GeoCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.geo_company import GeoCompany

# TODO update the JSON string below
json = "{}"
# create an instance of GeoCompany from a JSON string
geo_company_instance = GeoCompany.from_json(json)
# print the JSON string representation of the object
print(GeoCompany.to_json())

# convert the object into a dict
geo_company_dict = geo_company_instance.to_dict()
# create an instance of GeoCompany from a dict
geo_company_from_dict = GeoCompany.from_dict(geo_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


