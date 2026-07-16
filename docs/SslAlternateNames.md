# SslAlternateNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_names** | **List[str]** |  | [optional] 
**email_addresses** | **List[str]** |  | [optional] 
**ip_addresses** | **List[str]** |  | [optional] 
**uris** | **List[str]** |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_alternate_names import SslAlternateNames

# TODO update the JSON string below
json = "{}"
# create an instance of SslAlternateNames from a JSON string
ssl_alternate_names_instance = SslAlternateNames.from_json(json)
# print the JSON string representation of the object
print(SslAlternateNames.to_json())

# convert the object into a dict
ssl_alternate_names_dict = ssl_alternate_names_instance.to_dict()
# create an instance of SslAlternateNames from a dict
ssl_alternate_names_from_dict = SslAlternateNames.from_dict(ssl_alternate_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


