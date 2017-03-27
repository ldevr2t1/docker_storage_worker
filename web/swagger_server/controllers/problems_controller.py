import connexion
import json
import os
import flask
from swagger_server.models.body import Body
from swagger_server.models.error import Error
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from flask import jsonify
from flask.ext.api import status
from pymongo import MongoClient
#from . import utility

#____FOR LOCAL_______
client = MongoClient()
#_____________________

db = client.path_db

def insert_json(uid, version, body):
    #print("inside func")
    db.posts.insert_one({"problem_id": str(uid), "version": version, "body":body})

def add_problem(problem):
    """
    Creates a new problem and returns a problemID with default version 0
    
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: int
    """
    try:
        str_body = str(problem.decode("utf-8")).replace('\'', '\"')
        json.loads(str_body)
        problem = Body.from_dict(connexion.request.get_json())
        problem_id = problem['problem_id']
        if(db.posts.find_one({"problem_id":str(problem_id)}) == None):
            insert_json(problem_id, 0, problem['body'])
            return jsonify({"problem_id": problem_id})
        else:
            return get_status(404, "COULD NOT FIND"), status.HTTP_404_NOT_FOUND
    except ValueError:
        print("error")
        return get_status(500, "Invalid JSON"), status.HTTP_500_INTERNAL_SERVER_ERROR


def get_problems():
    """
    Problems
    Returns a list of all of the Problems generated. This can be an empty list. 

    :rtype: List[int]
    """
    array = []
    for post in db.posts.distinct("problem_id"):
        print(post)
        array.append(int(post))
    #run a check to see if the uid exists
    if len(array) == 0:
        return get_status(404, "No problems found"), status.HTTP_404_NOT_FOUND
    #if the uid doesn't exist then just go ahead return error status
    return jsonify({"problem_id": array})