# openapi_client.AdminApi

All URIs are relative to */reseller/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_admin**](AdminApi.md#create_admin) | **POST** /contracts/{contractNumber}/admins | Create new admin user for contract
[**delete_admin**](AdminApi.md#delete_admin) | **DELETE** /contracts/{contractNumber}/admins/{adminId} | Delete admin user
[**find_admin_by_id**](AdminApi.md#find_admin_by_id) | **GET** /contracts/{contractNumber}/admins/{adminId} | Find admin by ID
[**find_all_admins**](AdminApi.md#find_all_admins) | **GET** /contracts/{contractNumber}/admins | Get all admin users of the contract
[**update_admin**](AdminApi.md#update_admin) | **PATCH** /contracts/{contractNumber}/admins/{adminId} | Partially update admin user


# **create_admin**
> UserResponseResource create_admin(contract_number, body=body)

Create new admin user for contract

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.user_request_resource import UserRequestResource
from openapi_client.models.user_response_resource import UserResponseResource
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
    api_instance = openapi_client.AdminApi(api_client)
    contract_number = 56 # int | 
    body = openapi_client.UserRequestResource() # UserRequestResource |  (optional)

    try:
        # Create new admin user for contract
        api_response = api_instance.create_admin(contract_number, body=body)
        print("The response of AdminApi->create_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 
 **body** | [**UserRequestResource**](UserRequestResource.md)|  | [optional] 

### Return type

[**UserResponseResource**](UserResponseResource.md)

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

# **delete_admin**
> object delete_admin(contract_number, admin_id)

Delete admin user

This method call will remove admin user from the contract. This is a highly destructive method and must be used with caution.

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
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
    api_instance = openapi_client.AdminApi(api_client)
    contract_number = 56 # int | 
    admin_id = 56 # int | 

    try:
        # Delete admin user
        api_response = api_instance.delete_admin(contract_number, admin_id)
        print("The response of AdminApi->delete_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 
 **admin_id** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_admin_by_id**
> UserResponseResource find_admin_by_id(contract_number, admin_id)

Find admin by ID

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.user_response_resource import UserResponseResource
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
    api_instance = openapi_client.AdminApi(api_client)
    contract_number = 56 # int | 
    admin_id = 56 # int | 

    try:
        # Find admin by ID
        api_response = api_instance.find_admin_by_id(contract_number, admin_id)
        print("The response of AdminApi->find_admin_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->find_admin_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 
 **admin_id** | **int**|  | 

### Return type

[**UserResponseResource**](UserResponseResource.md)

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

# **find_all_admins**
> List[UserResponseResource] find_all_admins(contract_number)

Get all admin users of the contract

You can retrieve a complete list of admin users of the contract

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.user_response_resource import UserResponseResource
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
    api_instance = openapi_client.AdminApi(api_client)
    contract_number = 56 # int | 

    try:
        # Get all admin users of the contract
        api_response = api_instance.find_all_admins(contract_number)
        print("The response of AdminApi->find_all_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->find_all_admins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 

### Return type

[**List[UserResponseResource]**](UserResponseResource.md)

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

# **update_admin**
> UserResponseResource update_admin(contract_number, admin_id, body=body)

Partially update admin user

You can use this method to partially update admin user properties (firstName and/or lastName and/or email)

### Example

* Basic Authentication (BasicAuthentication):
* Api Key Authentication (TokenAuthentication):

```python
import openapi_client
from openapi_client.models.user_response_resource import UserResponseResource
from openapi_client.models.user_update_request_resource import UserUpdateRequestResource
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
    api_instance = openapi_client.AdminApi(api_client)
    contract_number = 56 # int | 
    admin_id = 56 # int | 
    body = openapi_client.UserUpdateRequestResource() # UserUpdateRequestResource |  (optional)

    try:
        # Partially update admin user
        api_response = api_instance.update_admin(contract_number, admin_id, body=body)
        print("The response of AdminApi->update_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_number** | **int**|  | 
 **admin_id** | **int**|  | 
 **body** | [**UserUpdateRequestResource**](UserUpdateRequestResource.md)|  | [optional] 

### Return type

[**UserResponseResource**](UserResponseResource.md)

### Authorization

[BasicAuthentication](../README.md#BasicAuthentication), [TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Any erroneous status code: 400 (parse error), 401 (auth error), 403 (insufficient privileges), 404 (not found), 405 (unsupported HTTP method), 415 (unsupported content type, 422 (validation error), 429 (request rate limit exceeded), 500 (server error), or 503 (maintenance). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

