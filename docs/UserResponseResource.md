# UserResponseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier | [optional] [readonly] 
**href** | **str** | URI for specific Admin in a Contract | [optional] [readonly] 
**first_name** | **str** | first name of the user | [optional] [readonly] 
**last_name** | **str** | last name of the user | [optional] [readonly] 
**email** | **str** | email of the user | [optional] [readonly] 

## Example

```python
from ionos_reseller_api_v2_client.models.user_response_resource import UserResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseResource from a JSON string
user_response_resource_instance = UserResponseResource.from_json(json)
# print the JSON string representation of the object
print(UserResponseResource.to_json())

# convert the object into a dict
user_response_resource_dict = user_response_resource_instance.to_dict()
# create an instance of UserResponseResource from a dict
user_response_resource_from_dict = UserResponseResource.from_dict(user_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


