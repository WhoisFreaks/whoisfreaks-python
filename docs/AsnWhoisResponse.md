# AsnWhoisResponse

ASN WHOIS v2 (/v2.0/asn-whois) — pass-through of ipgeolocation ASN data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | [**AsnInfo**](AsnInfo.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.asn_whois_response import AsnWhoisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsnWhoisResponse from a JSON string
asn_whois_response_instance = AsnWhoisResponse.from_json(json)
# print the JSON string representation of the object
print(AsnWhoisResponse.to_json())

# convert the object into a dict
asn_whois_response_dict = asn_whois_response_instance.to_dict()
# create an instance of AsnWhoisResponse from a dict
asn_whois_response_from_dict = AsnWhoisResponse.from_dict(asn_whois_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


