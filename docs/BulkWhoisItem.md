# BulkWhoisItem

One bulk WHOIS result. Successful items carry the same fields as a live WHOIS lookup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**query_time** | **str** |  | [optional] 
**whois_server** | **str** |  | [optional] 
**domain_registered** | **str** |  | [optional] 
**secure_dns** | **bool** |  | [optional] 
**domain_handle** | **str** |  | [optional] 
**create_date** | **str** |  | [optional] 
**update_date** | **str** |  | [optional] 
**expiry_date** | **str** |  | [optional] 
**domain_registrar** | [**RegistrarInformation**](RegistrarInformation.md) |  | [optional] 
**reseller_contact** | [**ResellerContact**](ResellerContact.md) |  | [optional] 
**registrant_contact** | [**PersonalInformation**](PersonalInformation.md) |  | [optional] 
**administrative_contact** | [**PersonalInformation**](PersonalInformation.md) |  | [optional] 
**technical_contact** | [**PersonalInformation**](PersonalInformation.md) |  | [optional] 
**billing_contact** | [**PersonalInformation**](PersonalInformation.md) |  | [optional] 
**eligibility_info** | [**EligibilityInfo**](EligibilityInfo.md) |  | [optional] 
**abuse_contact** | [**RegistrarInformation**](RegistrarInformation.md) |  | [optional] 
**name_servers** | **List[str]** |  | [optional] 
**domain_status** | **List[str]** |  | [optional] 
**whois_raw_domain** | **str** |  | [optional] 
**registry_data** | [**RegistryData**](RegistryData.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.bulk_whois_item import BulkWhoisItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkWhoisItem from a JSON string
bulk_whois_item_instance = BulkWhoisItem.from_json(json)
# print the JSON string representation of the object
print(BulkWhoisItem.to_json())

# convert the object into a dict
bulk_whois_item_dict = bulk_whois_item_instance.to_dict()
# create an instance of BulkWhoisItem from a dict
bulk_whois_item_from_dict = BulkWhoisItem.from_dict(bulk_whois_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


