# coding: utf-8

"""
    Reseller API

    API allowing resellers to create and manage contracts 

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_reseller_api_v2_client.models.info import Info

class TestInfo(unittest.TestCase):
    """Info unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Info:
        """Test Info
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Info`
        """
        model = Info()
        if include_optional:
            return Info(
                href = '',
                name = 'CLOUD API',
                version = '1.0'
            )
        else:
            return Info(
        )
        """

    def testInfo(self):
        """Test Info"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
