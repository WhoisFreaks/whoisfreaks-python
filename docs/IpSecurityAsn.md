# IpSecurityAsn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**date_allocated** | **str** |  | [optional] 
**rir** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.ip_security_asn import IpSecurityAsn

# TODO update the JSON string below
json = "{}"
# create an instance of IpSecurityAsn from a JSON string
ip_security_asn_instance = IpSecurityAsn.from_json(json)
# print the JSON string representation of the object
print(IpSecurityAsn.to_json())

# convert the object into a dict
ip_security_asn_dict = ip_security_asn_instance.to_dict()
# create an instance of IpSecurityAsn from a dict
ip_security_asn_from_dict = IpSecurityAsn.from_dict(ip_security_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


