import connexion
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_problem(problem):
    """
    Creates a new problem and returns a problemID with default version 0
    
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        problem = Problem.from_dict(connexion.request.get_json())
    return 'do some magic!'


def get_problems():
    """
    Problems
    Returns a list of all of the Problems generated. This can be an empty list. 

    :rtype: List[int]
    """
    return 'do some magic!'
