# DgaFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_length** | **int** |  | [optional] 
**vowel_consonant_ratio** | **float** |  | [optional] 
**ngram_perplexity** | **float** |  | [optional] 
**shannon_entropy** | **float** |  | [optional] 
**digit_letter_ratio** | **float** |  | [optional] 
**consonant_streak_max** | **int** |  | [optional] 
**tld_in_known_dga_set** | **bool** |  | [optional] 

## Example

```python
from whoisfreaks.models.dga_features import DgaFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of DgaFeatures from a JSON string
dga_features_instance = DgaFeatures.from_json(json)
# print the JSON string representation of the object
print(DgaFeatures.to_json())

# convert the object into a dict
dga_features_dict = dga_features_instance.to_dict()
# create an instance of DgaFeatures from a dict
dga_features_from_dict = DgaFeatures.from_dict(dga_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


