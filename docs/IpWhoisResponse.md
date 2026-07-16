# IpWhoisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**as_number** | **str** |  | [optional] 
**query_time** | **str** |  | [optional] 
**whois_server** | **str** |  | [optional] 
**whois_raw_response** | **str** |  | [optional] 
**r_whois_raw_response** | **str** |  | [optional] 
**inet_nums** | [**List[InetNum]**](InetNum.md) |  | [optional] 
**organization** | [**WhoisOrganization**](WhoisOrganization.md) |  | [optional] 
**irt** | [**Irt**](Irt.md) |  | [optional] 
**administrative_contacts** | [**List[WhoisPerson]**](WhoisPerson.md) |  | [optional] 
**technical_contacts** | [**List[WhoisPerson]**](WhoisPerson.md) |  | [optional] 
**abuse_contacts** | [**List[WhoisPerson]**](WhoisPerson.md) |  | [optional] 
**routes** | [**List[Route]**](Route.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.ip_whois_response import IpWhoisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IpWhoisResponse from a JSON string
ip_whois_response_instance = IpWhoisResponse.from_json(json)
# print the JSON string representation of the object
print(IpWhoisResponse.to_json())

# convert the object into a dict
ip_whois_response_dict = ip_whois_response_instance.to_dict()
# create an instance of IpWhoisResponse from a dict
ip_whois_response_from_dict = IpWhoisResponse.from_dict(ip_whois_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


