# coding: utf-8

"""
    Reseller API

    API allowing resellers to create and manage contracts 

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ionos_reseller_api_v2_client.models.contract_response_resource import ContractResponseResource

class TestContractResponseResource(unittest.TestCase):
    """ContractResponseResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractResponseResource:
        """Test ContractResponseResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContractResponseResource`
        """
        model = ContractResponseResource()
        if include_optional:
            return ContractResponseResource(
                id = '15514',
                href = 'https://api.ionos.com/reseller/v2/contract/15514',
                name = '',
                reseller_reference = '',
                status = '',
                resource_limits = ionos_reseller_api_v2_client.models.resource_limits.ResourceLimits(
                    ram_server_max = 56, 
                    cpu_server_max = 56, 
                    hdd_volume_max_size = 56, 
                    ssd_volume_max_size = 56, 
                    ram_contract_max = 56, 
                    cpu_contract_max = 56, 
                    hdd_volume_contract_max_size = 56, 
                    ssd_volume_contract_max_size = 56, 
                    ips = 56, )
            )
        else:
            return ContractResponseResource(
        )
        """

    def testContractResponseResource(self):
        """Test ContractResponseResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
