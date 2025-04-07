# UserRequestResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | first name of the user | 
**last_name** | **str** | last name of the user | 
**email** | **str** | email of the user | 
**password** | **str** | password of the user | 

## Example

```python
from ionos_reseller_api_v2_client.models.user_request_resource import UserRequestResource

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequestResource from a JSON string
user_request_resource_instance = UserRequestResource.from_json(json)
# print the JSON string representation of the object
print(UserRequestResource.to_json())

# convert the object into a dict
user_request_resource_dict = user_request_resource_instance.to_dict()
# create an instance of UserRequestResource from a dict
user_request_resource_from_dict = UserRequestResource.from_dict(user_request_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


