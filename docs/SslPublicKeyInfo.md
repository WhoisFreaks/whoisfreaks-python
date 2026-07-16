# SslPublicKeyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_size** | **str** |  | [optional] 
**key_algorithm** | **str** |  | [optional] 
**pem_raw** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_public_key_info import SslPublicKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SslPublicKeyInfo from a JSON string
ssl_public_key_info_instance = SslPublicKeyInfo.from_json(json)
# print the JSON string representation of the object
print(SslPublicKeyInfo.to_json())

# convert the object into a dict
ssl_public_key_info_dict = ssl_public_key_info_instance.to_dict()
# create an instance of SslPublicKeyInfo from a dict
ssl_public_key_info_from_dict = SslPublicKeyInfo.from_dict(ssl_public_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


