import connexion
from swagger_server.models.body import Body
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def delete_problem(problem_id):
    """
    Delete Problem
    This removes the problem by the given ID 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: None
    """
    return 'do some magic!'

def get_problem(problem_id):
    """
    Problems
    Returns most updated problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """
    return 'do some magic!'


def update_problem(problem_id, version, problem):
    """
    Update the existing problem
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the problem being manipulated
    :type version: int
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        problem = Body.from_dict(connexion.request.get_json())
    return 'do some magic!'

def get_specific_key(problem_id, version, key):
    """
    Specific Key
    Returns a specific key in the body of the most updated problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the problem being manipulated
    :type version: int
    :param key: The key within the body of the problem being manipulated
    :type key: str

    :rtype: Body
    """
    return jsonify({"test":1})
