# ResourceLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ram_server_max** | **int** | maximum ram per virtual machine | 
**cpu_server_max** | **int** | maximum number of cpu per virtual machine | 
**hdd_volume_max_size** | **int** | maximum hdd volume size | 
**ssd_volume_max_size** | **int** | maximum ssd volume size | 
**ram_contract_max** | **int** | maximum ram per contract | 
**cpu_contract_max** | **int** | maximum cpu per contract | 
**hdd_volume_contract_max_size** | **int** | maximum hhd volume per contract | 
**ssd_volume_contract_max_size** | **int** | maximum ssd volume per contract | 
**ips** | **int** | maximum ips per contract | 

## Example

```python
from ionos_reseller_api_v2_client.models.resource_limits import ResourceLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLimits from a JSON string
resource_limits_instance = ResourceLimits.from_json(json)
# print the JSON string representation of the object
print(ResourceLimits.to_json())

# convert the object into a dict
resource_limits_dict = resource_limits_instance.to_dict()
# create an instance of ResourceLimits from a dict
resource_limits_from_dict = ResourceLimits.from_dict(resource_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


