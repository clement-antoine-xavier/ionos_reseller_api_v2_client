# ContractResponseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier | [optional] [readonly] 
**href** | **str** | URI for specific Contract | [optional] [readonly] 
**name** | **str** | name of the contract | [optional] 
**reseller_reference** | **str** | reseller reference of the contract | [optional] 
**status** | **str** | status of the contract | [optional] 
**resource_limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 

## Example

```python
from openapi_client.models.contract_response_resource import ContractResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of ContractResponseResource from a JSON string
contract_response_resource_instance = ContractResponseResource.from_json(json)
# print the JSON string representation of the object
print(ContractResponseResource.to_json())

# convert the object into a dict
contract_response_resource_dict = contract_response_resource_instance.to_dict()
# create an instance of ContractResponseResource from a dict
contract_response_resource_from_dict = ContractResponseResource.from_dict(contract_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


