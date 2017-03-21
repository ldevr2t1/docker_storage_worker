import connexion
from swagger_server.models.body import Body
from swagger_server.models.error import Error
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import json

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
