# AccountUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**api_credits** | [**ApiCredits**](ApiCredits.md) |  | [optional] 
**api_subscription** | [**ApiSubscription**](ApiSubscription.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.account_usage_response import AccountUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUsageResponse from a JSON string
account_usage_response_instance = AccountUsageResponse.from_json(json)
# print the JSON string representation of the object
print(AccountUsageResponse.to_json())

# convert the object into a dict
account_usage_response_dict = account_usage_response_instance.to_dict()
# create an instance of AccountUsageResponse from a dict
account_usage_response_from_dict = AccountUsageResponse.from_dict(account_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


