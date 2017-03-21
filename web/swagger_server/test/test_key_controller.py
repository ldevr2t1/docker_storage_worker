# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body import Body
from swagger_server.models.error import Error
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestKeyController(BaseTestCase):
    """ KeyController integration test stubs """

    def test_get_specific_key(self):
        """
        Test case for get_specific_key

        Specific Key
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/ver&#x3D;{version}/key&#x3D;{key}'.format(problem_id=56, version=56, key='key_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
