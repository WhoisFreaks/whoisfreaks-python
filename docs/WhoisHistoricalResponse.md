# WhoisHistoricalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**whois** | **str** |  | [optional] 
**total_records** | **str** |  | [optional] 
**whois_domains_historical** | [**List[WhoisHistoricalItem]**](WhoisHistoricalItem.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.whois_historical_response import WhoisHistoricalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WhoisHistoricalResponse from a JSON string
whois_historical_response_instance = WhoisHistoricalResponse.from_json(json)
# print the JSON string representation of the object
print(WhoisHistoricalResponse.to_json())

# convert the object into a dict
whois_historical_response_dict = whois_historical_response_instance.to_dict()
# create an instance of WhoisHistoricalResponse from a dict
whois_historical_response_from_dict = WhoisHistoricalResponse.from_dict(whois_historical_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


