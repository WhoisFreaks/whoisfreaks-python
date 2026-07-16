# DomainReputationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**DomainReputationInput**](DomainReputationInput.md) |  | [optional] 
**assessed_at** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**processing_time_ms** | **int** |  | [optional] 
**risk_category** | [**RiskCategory**](RiskCategory.md) |  | [optional] 
**dga_score** | [**DgaScore**](DgaScore.md) |  | [optional] 
**trust_signals** | [**TrustSignals**](TrustSignals.md) |  | [optional] 
**intelligence** | [**ReputationIntelligence**](ReputationIntelligence.md) |  | [optional] 
**evidence_summary** | [**EvidenceSummary**](EvidenceSummary.md) |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from whoisfreaks.models.domain_reputation_response import DomainReputationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainReputationResponse from a JSON string
domain_reputation_response_instance = DomainReputationResponse.from_json(json)
# print the JSON string representation of the object
print(DomainReputationResponse.to_json())

# convert the object into a dict
domain_reputation_response_dict = domain_reputation_response_instance.to_dict()
# create an instance of DomainReputationResponse from a dict
domain_reputation_response_from_dict = DomainReputationResponse.from_dict(domain_reputation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


