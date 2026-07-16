# ApiCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_credits** | **int** |  | [optional] 
**served_request** | **int** |  | [optional] 

## Example

```python
from whoisfreaks.models.api_credits import ApiCredits

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCredits from a JSON string
api_credits_instance = ApiCredits.from_json(json)
# print the JSON string representation of the object
print(ApiCredits.to_json())

# convert the object into a dict
api_credits_dict = api_credits_instance.to_dict()
# create an instance of ApiCredits from a dict
api_credits_from_dict = ApiCredits.from_dict(api_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


