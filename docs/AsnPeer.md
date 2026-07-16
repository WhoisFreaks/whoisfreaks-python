# AsnPeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from whoisfreaks.models.asn_peer import AsnPeer

# TODO update the JSON string below
json = "{}"
# create an instance of AsnPeer from a JSON string
asn_peer_instance = AsnPeer.from_json(json)
# print the JSON string representation of the object
print(AsnPeer.to_json())

# convert the object into a dict
asn_peer_dict = asn_peer_instance.to_dict()
# create an instance of AsnPeer from a dict
asn_peer_from_dict = AsnPeer.from_dict(asn_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


