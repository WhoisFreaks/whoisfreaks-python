# RelatedIoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 

## Example

```python
from whoisfreaks.models.related_ioc import RelatedIoc

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedIoc from a JSON string
related_ioc_instance = RelatedIoc.from_json(json)
# print the JSON string representation of the object
print(RelatedIoc.to_json())

# convert the object into a dict
related_ioc_dict = related_ioc_instance.to_dict()
# create an instance of RelatedIoc from a dict
related_ioc_from_dict = RelatedIoc.from_dict(related_ioc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


