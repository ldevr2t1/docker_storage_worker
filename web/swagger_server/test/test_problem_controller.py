# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.body import Body
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProblemController(BaseTestCase):
    """ ProblemController integration test stubs """

    def test_delete_problem(self):
        """
        Test case for delete_problem

        Delete Problem
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/'.format(problem_id=56),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_problem(self):
        """
        Test case for get_problem

        Problems
        """
        response = self.client.open('/v2/id&#x3D;{problem_id}/'.format(problem_id=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_problem(self):
        """
        Test case for update_problem

        Update the existing problem
        """
        problem = Body()
        response = self.client.open('/v2/id&#x3D;{problem_id}/ver&#x3D;{version}/'.format(problem_id=56, version=56),
                                    method='PUT',
                                    data=json.dumps(problem),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
