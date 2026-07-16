# SslExtensionsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority_key_identifier** | **str** |  | [optional] 
**subject_key_identifier** | **str** |  | [optional] 
**key_usages** | **List[str]** |  | [optional] 
**extended_key_usages** | **List[str]** |  | [optional] 
**crl_distribution_points** | **List[str]** |  | [optional] 
**authority_info_access** | [**SslAuthorityInfo**](SslAuthorityInfo.md) |  | [optional] 
**subject_alternative_names** | [**SslAlternateNames**](SslAlternateNames.md) |  | [optional] 
**certificate_policies** | [**List[SslCertificatePolicy]**](SslCertificatePolicy.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_extensions_info import SslExtensionsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SslExtensionsInfo from a JSON string
ssl_extensions_info_instance = SslExtensionsInfo.from_json(json)
# print the JSON string representation of the object
print(SslExtensionsInfo.to_json())

# convert the object into a dict
ssl_extensions_info_dict = ssl_extensions_info_instance.to_dict()
# create an instance of SslExtensionsInfo from a dict
ssl_extensions_info_from_dict = SslExtensionsInfo.from_dict(ssl_extensions_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


