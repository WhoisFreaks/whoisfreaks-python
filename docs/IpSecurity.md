# IpSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_score** | **int** |  | [optional] 
**is_tor** | **bool** |  | [optional] 
**is_proxy** | **bool** |  | [optional] 
**proxy_provider_names** | **List[str]** |  | [optional] 
**proxy_confidence_score** | **int** |  | [optional] 
**proxy_last_seen** | **str** |  | [optional] 
**is_residential_proxy** | **bool** |  | [optional] 
**is_vpn** | **bool** |  | [optional] 
**vpn_provider_names** | **List[str]** |  | [optional] 
**vpn_confidence_score** | **int** |  | [optional] 
**vpn_last_seen** | **str** |  | [optional] 
**is_relay** | **bool** |  | [optional] 
**relay_provider_name** | **str** |  | [optional] 
**is_anonymous** | **bool** |  | [optional] 
**is_known_attacker** | **bool** |  | [optional] 
**is_bot** | **bool** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**is_cloud_provider** | **bool** |  | [optional] 
**cloud_provider_name** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.ip_security import IpSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of IpSecurity from a JSON string
ip_security_instance = IpSecurity.from_json(json)
# print the JSON string representation of the object
print(IpSecurity.to_json())

# convert the object into a dict
ip_security_dict = ip_security_instance.to_dict()
# create an instance of IpSecurity from a dict
ip_security_from_dict = IpSecurity.from_dict(ip_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


