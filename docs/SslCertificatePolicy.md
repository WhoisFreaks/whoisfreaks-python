# SslCertificatePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** |  | [optional] 
**policy_qualifier** | **object** |  | [optional] 

## Example

```python
from whoisfreaks.models.ssl_certificate_policy import SslCertificatePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of SslCertificatePolicy from a JSON string
ssl_certificate_policy_instance = SslCertificatePolicy.from_json(json)
# print the JSON string representation of the object
print(SslCertificatePolicy.to_json())

# convert the object into a dict
ssl_certificate_policy_dict = ssl_certificate_policy_instance.to_dict()
# create an instance of SslCertificatePolicy from a dict
ssl_certificate_policy_from_dict = SslCertificatePolicy.from_dict(ssl_certificate_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


