# UserUpdateRequestResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | first name of the user | 
**last_name** | **str** | last name of the user | 
**email** | **str** | email of the user | 

## Example

```python
from openapi_client.models.user_update_request_resource import UserUpdateRequestResource

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateRequestResource from a JSON string
user_update_request_resource_instance = UserUpdateRequestResource.from_json(json)
# print the JSON string representation of the object
print(UserUpdateRequestResource.to_json())

# convert the object into a dict
user_update_request_resource_dict = user_update_request_resource_instance.to_dict()
# create an instance of UserUpdateRequestResource from a dict
user_update_request_resource_from_dict = UserUpdateRequestResource.from_dict(user_update_request_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


