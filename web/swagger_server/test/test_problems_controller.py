# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProblemsController(BaseTestCase):
    """ ProblemsController integration test stubs """

    def test_add_problem(self):
        """
        Test case for add_problem

        Creates a new problem and returns a problemID with default version 0
        """
        problem = Problem()
        response = self.client.open('/v2/',
                                    method='POST',
                                    data=json.dumps(problem),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_problems(self):
        """
        Test case for get_problems

        Problems
        """
        response = self.client.open('/v2/',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
