# TyposquattingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**total_records** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**has_next_page** | **bool** |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**domains** | [**List[TyposquattingDomain]**](TyposquattingDomain.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.typosquatting_response import TyposquattingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TyposquattingResponse from a JSON string
typosquatting_response_instance = TyposquattingResponse.from_json(json)
# print the JSON string representation of the object
print(TyposquattingResponse.to_json())

# convert the object into a dict
typosquatting_response_dict = typosquatting_response_instance.to_dict()
# create an instance of TyposquattingResponse from a dict
typosquatting_response_from_dict = TyposquattingResponse.from_dict(typosquatting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


