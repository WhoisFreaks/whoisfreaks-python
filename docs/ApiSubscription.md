# ApiSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_limit** | **int** |  | [optional] 
**served_requests** | **int** |  | [optional] 
**subscription_status** | **str** |  | [optional] 
**surcharge_request_limit** | **int** |  | [optional] 
**served_surcharge_requests** | **int** |  | [optional] 

## Example

```python
from whoisfreaks.models.api_subscription import ApiSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSubscription from a JSON string
api_subscription_instance = ApiSubscription.from_json(json)
# print the JSON string representation of the object
print(ApiSubscription.to_json())

# convert the object into a dict
api_subscription_dict = api_subscription_instance.to_dict()
# create an instance of ApiSubscription from a dict
api_subscription_from_dict = ApiSubscription.from_dict(api_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


