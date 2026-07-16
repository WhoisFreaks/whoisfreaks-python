# IpSecurityNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** |  | [optional] 
**route** | **str** |  | [optional] 
**is_anycast** | **bool** |  | [optional] 

## Example

```python
from whoisfreaks.models.ip_security_network import IpSecurityNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of IpSecurityNetwork from a JSON string
ip_security_network_instance = IpSecurityNetwork.from_json(json)
# print the JSON string representation of the object
print(IpSecurityNetwork.to_json())

# convert the object into a dict
ip_security_network_dict = ip_security_network_instance.to_dict()
# create an instance of IpSecurityNetwork from a dict
ip_security_network_from_dict = IpSecurityNetwork.from_dict(ip_security_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


