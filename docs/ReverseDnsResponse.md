# ReverseDnsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_records** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**reverse_dns_records** | [**List[DnsResponse]**](DnsResponse.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.reverse_dns_response import ReverseDnsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseDnsResponse from a JSON string
reverse_dns_response_instance = ReverseDnsResponse.from_json(json)
# print the JSON string representation of the object
print(ReverseDnsResponse.to_json())

# convert the object into a dict
reverse_dns_response_dict = reverse_dns_response_instance.to_dict()
# create an instance of ReverseDnsResponse from a dict
reverse_dns_response_from_dict = ReverseDnsResponse.from_dict(reverse_dns_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


