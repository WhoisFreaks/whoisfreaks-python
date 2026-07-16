# SslCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_order** | **str** |  | [optional] 
**authentication_type** | **str** |  | [optional] 
**validity_start_date** | **str** |  | [optional] 
**validity_end_date** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**signature_algorithm** | **str** |  | [optional] 
**subject** | [**SslUnitInfo**](SslUnitInfo.md) |  | [optional] 
**issuer** | [**SslUnitInfo**](SslUnitInfo.md) |  | [optional] 
**public_key** | [**SslPublicKeyInfo**](SslPublicKeyInfo.md) |  | [optional] 
**extensions** | [**SslExtensionsInfo**](SslExtensionsInfo.md) |  | [optional] 
**pem_raw** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_certificate import SslCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SslCertificate from a JSON string
ssl_certificate_instance = SslCertificate.from_json(json)
# print the JSON string representation of the object
print(SslCertificate.to_json())

# convert the object into a dict
ssl_certificate_dict = ssl_certificate_instance.to_dict()
# create an instance of SslCertificate from a dict
ssl_certificate_from_dict = SslCertificate.from_dict(ssl_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


