# AsnInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**date_allocated** | **str** |  | [optional] 
**asn_name** | **str** |  | [optional] 
**allocation_status** | **str** |  | [optional] 
**num_of_ipv4_routes** | **str** |  | [optional] 
**num_of_ipv6_routes** | **str** |  | [optional] 
**rir** | **str** |  | [optional] 
**routes** | **List[str]** |  | [optional] 
**downstreams** | [**List[AsnPeer]**](AsnPeer.md) |  | [optional] 
**upstreams** | [**List[AsnPeer]**](AsnPeer.md) |  | [optional] 
**peers** | [**List[AsnPeer]**](AsnPeer.md) |  | [optional] 
**whois_response** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.asn_info import AsnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AsnInfo from a JSON string
asn_info_instance = AsnInfo.from_json(json)
# print the JSON string representation of the object
print(AsnInfo.to_json())

# convert the object into a dict
asn_info_dict = asn_info_instance.to_dict()
# create an instance of AsnInfo from a dict
asn_info_from_dict = AsnInfo.from_dict(asn_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


