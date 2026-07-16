# WhoisHistoricalItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num** | **int** |  | [optional] 
**status** | **bool** |  | [optional] 
**domain_name** | **str** |  | [optional] 
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
from whoisfreaks.models.whois_historical_item import WhoisHistoricalItem

# TODO update the JSON string below
json = "{}"
# create an instance of WhoisHistoricalItem from a JSON string
whois_historical_item_instance = WhoisHistoricalItem.from_json(json)
# print the JSON string representation of the object
print(WhoisHistoricalItem.to_json())

# convert the object into a dict
whois_historical_item_dict = whois_historical_item_instance.to_dict()
# create an instance of WhoisHistoricalItem from a dict
whois_historical_item_from_dict = WhoisHistoricalItem.from_dict(whois_historical_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


