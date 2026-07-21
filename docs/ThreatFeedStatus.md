# ThreatFeedStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phishing** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**malware** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 
**spam** | [**DateRangeStatus**](DateRangeStatus.md) |  | [optional] 

## Example

```python
from whoisfreaks.models.threat_feed_status import ThreatFeedStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatFeedStatus from a JSON string
threat_feed_status_instance = ThreatFeedStatus.from_json(json)
# print the JSON string representation of the object
print(ThreatFeedStatus.to_json())

# convert the object into a dict
threat_feed_status_dict = threat_feed_status_instance.to_dict()
# create an instance of ThreatFeedStatus from a dict
threat_feed_status_from_dict = ThreatFeedStatus.from_dict(threat_feed_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


