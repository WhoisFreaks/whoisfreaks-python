# HistoricalDnsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**total_records** | **int** |  | [optional] 
**historical_dns_records** | [**List[DnsResponse]**](DnsResponse.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.historical_dns_response import HistoricalDnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricalDnsResponse from a JSON string
historical_dns_response_instance = HistoricalDnsResponse.from_json(json)
# print the JSON string representation of the object
print(HistoricalDnsResponse.to_json())

# convert the object into a dict
historical_dns_response_dict = historical_dns_response_instance.to_dict()
# create an instance of HistoricalDnsResponse from a dict
historical_dns_response_from_dict = HistoricalDnsResponse.from_dict(historical_dns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


