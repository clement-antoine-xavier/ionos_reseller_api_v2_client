# coding: utf-8

"""
    Reseller API

    API allowing resellers to create and manage contracts 

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_request_resource import UserRequestResource

class TestUserRequestResource(unittest.TestCase):
    """UserRequestResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserRequestResource:
        """Test UserRequestResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserRequestResource`
        """
        model = UserRequestResource()
        if include_optional:
            return UserRequestResource(
                first_name = '',
                last_name = '',
                email = '',
                password = ''
            )
        else:
            return UserRequestResource(
                first_name = '',
                last_name = '',
                email = '',
                password = '',
        )
        """

    def testUserRequestResource(self):
        """Test UserRequestResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
