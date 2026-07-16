# DatabaseUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_whois** | [**UpdateFrequencies**](UpdateFrequencies.md) |  | [optional] 
**dns** | [**UpdateFrequencies**](UpdateFrequencies.md) |  | [optional] 
**subdomains** | [**UpdateFrequencies**](UpdateFrequencies.md) |  | [optional] 
**ip_whois** | [**UpdateFrequencies**](UpdateFrequencies.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.database_updates import DatabaseUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseUpdates from a JSON string
database_updates_instance = DatabaseUpdates.from_json(json)
# print the JSON string representation of the object
print(DatabaseUpdates.to_json())

# convert the object into a dict
database_updates_dict = database_updates_instance.to_dict()
# create an instance of DatabaseUpdates from a dict
database_updates_from_dict = DatabaseUpdates.from_dict(database_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


