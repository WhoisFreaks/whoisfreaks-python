# ReverseWhoisResponse

Reverse WHOIS response. Pagination keys are capitalized (Total_Result/Total_Pages/Current_Page) as returned by the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_result** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**whois_domains_historical** | [**List[WhoisHistoricalItem]**](WhoisHistoricalItem.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.reverse_whois_response import ReverseWhoisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseWhoisResponse from a JSON string
reverse_whois_response_instance = ReverseWhoisResponse.from_json(json)
# print the JSON string representation of the object
print(ReverseWhoisResponse.to_json())

# convert the object into a dict
reverse_whois_response_dict = reverse_whois_response_instance.to_dict()
# create an instance of ReverseWhoisResponse from a dict
reverse_whois_response_from_dict = ReverseWhoisResponse.from_dict(reverse_whois_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


