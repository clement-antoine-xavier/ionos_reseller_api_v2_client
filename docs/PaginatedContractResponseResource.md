# PaginatedContractResponseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContractResponseResource]**](ContractResponseResource.md) | Array of items in the collection. | [optional] [readonly] 
**offset** | **float** | The offset (if specified in the request). | [optional] 
**limit** | **float** | The limit (if specified in the request). | [optional] 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from ionos_reseller_api_v2_client.models.paginated_contract_response_resource import PaginatedContractResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedContractResponseResource from a JSON string
paginated_contract_response_resource_instance = PaginatedContractResponseResource.from_json(json)
# print the JSON string representation of the object
print(PaginatedContractResponseResource.to_json())

# convert the object into a dict
paginated_contract_response_resource_dict = paginated_contract_response_resource_instance.to_dict()
# create an instance of PaginatedContractResponseResource from a dict
paginated_contract_response_resource_from_dict = PaginatedContractResponseResource.from_dict(paginated_contract_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


