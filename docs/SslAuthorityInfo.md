# SslAuthorityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuers** | **List[str]** |  | [optional] 
**ocsp** | **List[str]** |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_authority_info import SslAuthorityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SslAuthorityInfo from a JSON string
ssl_authority_info_instance = SslAuthorityInfo.from_json(json)
# print the JSON string representation of the object
print(SslAuthorityInfo.to_json())

# convert the object into a dict
ssl_authority_info_dict = ssl_authority_info_instance.to_dict()
# create an instance of SslAuthorityInfo from a dict
ssl_authority_info_from_dict = SslAuthorityInfo.from_dict(ssl_authority_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


