# EvidenceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**why_flagged** | **List[str]** |  | [optional] 

## Example

```python
from whoisfreaks.models.evidence_summary import EvidenceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EvidenceSummary from a JSON string
evidence_summary_instance = EvidenceSummary.from_json(json)
# print the JSON string representation of the object
print(EvidenceSummary.to_json())

# convert the object into a dict
evidence_summary_dict = evidence_summary_instance.to_dict()
# create an instance of EvidenceSummary from a dict
evidence_summary_from_dict = EvidenceSummary.from_dict(evidence_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


