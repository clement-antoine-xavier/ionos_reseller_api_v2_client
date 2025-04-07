# ContractRequestResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the contract | 
**reseller_reference** | **str** | reseller reference of the contract | [optional] 
**resource_limits** | [**ResourceLimits**](ResourceLimits.md) |  | 

## Example

```python
from ionos_reseller_api_v2_client.models.contract_request_resource import ContractRequestResource

# TODO update the JSON string below
json = "{}"
# create an instance of ContractRequestResource from a JSON string
contract_request_resource_instance = ContractRequestResource.from_json(json)
# print the JSON string representation of the object
print(ContractRequestResource.to_json())

# convert the object into a dict
contract_request_resource_dict = contract_request_resource_instance.to_dict()
# create an instance of ContractRequestResource from a dict
contract_request_resource_from_dict = ContractRequestResource.from_dict(contract_request_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


