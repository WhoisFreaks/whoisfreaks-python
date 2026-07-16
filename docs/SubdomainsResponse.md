# SubdomainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**query_time** | **str** |  | [optional] 
**total_records** | **int** |  | [optional] 
**subdomains** | [**List[Subdomain]**](Subdomain.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.subdomains_response import SubdomainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubdomainsResponse from a JSON string
subdomains_response_instance = SubdomainsResponse.from_json(json)
# print the JSON string representation of the object
print(SubdomainsResponse.to_json())

# convert the object into a dict
subdomains_response_dict = subdomains_response_instance.to_dict()
# create an instance of SubdomainsResponse from a dict
subdomains_response_from_dict = SubdomainsResponse.from_dict(subdomains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


