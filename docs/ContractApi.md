# openapi_client.ContractApi

All URIs are relative to */reseller/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract**](ContractApi.md#create_contract) | **POST** /contracts | Create new contract
[**find_all**](ContractApi.md#find_all) | **GET** /contracts | Get all contracts
[**find_by_id**](ContractApi.md#find_by_id) | **GET** /contracts/{contractNumber} | Find contract by ID
[**update_contract**](ContractApi.md#update_contract) | **PUT** /contracts/{contractNumber} | Update contract
[**update_contract_resource_limits**](ContractApi.md#update_contract_resource_limits) | **PUT** /contracts/{contractNumber}/resourcelimits | Update resource limits for contract
[**update_name**](ContractApi.md#update_name) | **PUT** /contracts/{contractNumber}/name | Update contract name


# **create_contract**
> ContractResponseResource create_contract(body=body)

Create new contract

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.contract_request_resource import ContractRequestResource
from openapi_client.models.contract_response_resource import ContractResponseResource
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /reseller/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/reseller/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContractApi(api_client)
    body = openapi_client.ContractRequestResource() # ContractRequestResource |  (optional)

    try:
        # Create new contract
        api_response = api_instance.create_contract(body=body)
        print("The response of ContractApi->create_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->create_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContractRequestResource**](ContractRequestResource.md)|  | [optional] 

### Return type

[**ContractResponseResource**](ContractResponseResource.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  * Location - URL of newly created contract <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> PaginatedContractResponseResource find_all(offset=offset, limit=limit, filter_status=filter_status)

Get all contracts

Retrieve a paginated list of contracts, provisioned under the Master Reseller contract. Default limit is the first 50 items; use pagination query parameters for listing more items.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.paginated_contract_response_resource import PaginatedContractResponseResource
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /reseller/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/reseller/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContractApi(api_client)
    offset = 0 # int | The first element (from the complete list of the elements) to include in the response (used together with <b><i>limit</i></b> for pagination). (optional) (default to 0)
    limit = 50 # int | The maximum number of elements to return (use together with offset for pagination). (optional) (default to 50)
    filter_status = 'filter_status_example' # str | Filter the list by contract status [BILLABLE, CEASED, REJECTED]. (optional)

    try:
        # Get all contracts
        api_response = api_instance.find_all(offset=offset, limit=limit, filter_status=filter_status)
        print("The response of ContractApi->find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->find_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first element (from the complete list of the elements) to include in the response (used together with &lt;b&gt;&lt;i&gt;limit&lt;/i&gt;&lt;/b&gt; for pagination). | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return (use together with offset for pagination). | [optional] [default to 50]
 **filter_status** | **str**| Filter the list by contract status [BILLABLE, CEASED, REJECTED]. | [optional] 

### Return type

[**PaginatedContractResponseResource**](PaginatedContractResponseResource.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_id**
> ContractResponseResource find_by_id(contract_number)

Find contract by ID

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.contract_response_resource import ContractResponseResource
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /reseller/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/reseller/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContractApi(api_client)
    contract_number = 56 # int | 

    try:
        # Find contract by ID
        api_response = api_instance.find_by_id(contract_number)
        print("The response of ContractApi->find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 

### Return type

[**ContractResponseResource**](ContractResponseResource.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract**
> ContractResponseResource update_contract(contract_number, body=body)

Update contract

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.contract_request_resource import ContractRequestResource
from openapi_client.models.contract_response_resource import ContractResponseResource
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /reseller/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/reseller/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContractApi(api_client)
    contract_number = 56 # int | 
    body = openapi_client.ContractRequestResource() # ContractRequestResource |  (optional)

    try:
        # Update contract
        api_response = api_instance.update_contract(contract_number, body=body)
        print("The response of ContractApi->update_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->update_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 
 **body** | [**ContractRequestResource**](ContractRequestResource.md)|  | [optional] 

### Return type

[**ContractResponseResource**](ContractResponseResource.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Location - URL of modified contract <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract_resource_limits**
> ContractResponseResource update_contract_resource_limits(contract_number, body=body)

Update resource limits for contract

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.contract_response_resource import ContractResponseResource
from openapi_client.models.resource_limits import ResourceLimits
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /reseller/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/reseller/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContractApi(api_client)
    contract_number = 56 # int | 
    body = openapi_client.ResourceLimits() # ResourceLimits |  (optional)

    try:
        # Update resource limits for contract
        api_response = api_instance.update_contract_resource_limits(contract_number, body=body)
        print("The response of ContractApi->update_contract_resource_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->update_contract_resource_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 
 **body** | [**ResourceLimits**](ResourceLimits.md)|  | [optional] 

### Return type

[**ContractResponseResource**](ContractResponseResource.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Location - URL of modified contract <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_name**
> ContractResponseResource update_name(contract_number, body=body)

Update contract name

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.contract_response_resource import ContractResponseResource
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /reseller/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/reseller/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuthentication
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: TokenAuthentication
configuration.api_key['TokenAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TokenAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ContractApi(api_client)
    contract_number = 56 # int | 
    body = 'body_example' # str |  (optional)

    try:
        # Update contract name
        api_response = api_instance.update_name(contract_number, body=body)
        print("The response of ContractApi->update_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractApi->update_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 
 **body** | **str**|  | [optional] 

### Return type

[**ContractResponseResource**](ContractResponseResource.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Location - URL of modified contract <br>  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

