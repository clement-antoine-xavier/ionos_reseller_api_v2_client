# Info


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | API entry point | [optional] [readonly] 
**name** | **str** | Name of the API | [optional] [readonly] 
**version** | **str** | Version of the API | [optional] [readonly] 

## Example

```python
from ionos_reseller_api_v2_client.models.info import Info

# TODO update the JSON string below
json = "{}"
# create an instance of Info from a JSON string
info_instance = Info.from_json(json)
# print the JSON string representation of the object
print(Info.to_json())

# convert the object into a dict
info_dict = info_instance.to_dict()
# create an instance of Info from a dict
info_from_dict = Info.from_dict(info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


