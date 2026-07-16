# BulkDomainAvailabilityRequest

Request body for POST /v2.0/domain/availability. Use domainNames OR tld.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_names** | **List[str]** | Mode 1 — list of full domain names. Cannot be used with tld. | [optional] 
**tld** | **List[str]** | Mode 2 — TLDs to check against the domain query param. Cannot be used with domainNames. | [optional] 

## Example

```python
from whoisfreaks.models.bulk_domain_availability_request import BulkDomainAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDomainAvailabilityRequest from a JSON string
bulk_domain_availability_request_instance = BulkDomainAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDomainAvailabilityRequest.to_json())

# convert the object into a dict
bulk_domain_availability_request_dict = bulk_domain_availability_request_instance.to_dict()
# create an instance of BulkDomainAvailabilityRequest from a dict
bulk_domain_availability_request_from_dict = BulkDomainAvailabilityRequest.from_dict(bulk_domain_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


