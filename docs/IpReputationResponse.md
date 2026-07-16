# IpReputationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**location** | [**IpLocation**](IpLocation.md) |  | [optional] 
**network** | [**IpSecurityNetwork**](IpSecurityNetwork.md) |  | [optional] 
**asn** | [**IpSecurityAsn**](IpSecurityAsn.md) |  | [optional] 
**security** | [**IpSecurity**](IpSecurity.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.ip_reputation_response import IpReputationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IpReputationResponse from a JSON string
ip_reputation_response_instance = IpReputationResponse.from_json(json)
# print the JSON string representation of the object
print(IpReputationResponse.to_json())

# convert the object into a dict
ip_reputation_response_dict = ip_reputation_response_instance.to_dict()
# create an instance of IpReputationResponse from a dict
ip_reputation_response_from_dict = IpReputationResponse.from_dict(ip_reputation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


