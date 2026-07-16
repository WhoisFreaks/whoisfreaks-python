# SslResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** |  | [optional] 
**query_time** | **str** |  | [optional] 
**ssl_certificates** | [**List[SslCertificate]**](SslCertificate.md) |  | [optional] 
**ssl_raw** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_response import SslResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SslResponse from a JSON string
ssl_response_instance = SslResponse.from_json(json)
# print the JSON string representation of the object
print(SslResponse.to_json())

# convert the object into a dict
ssl_response_dict = ssl_response_instance.to_dict()
# create an instance of SslResponse from a dict
ssl_response_from_dict = SslResponse.from_dict(ssl_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


