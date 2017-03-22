import connexion
import json
import os
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from flask import jsonify
from flask.ext.api import status
from pymongo import MongoClient

#____FOR DOCKER______
#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
#____________________

#____FOR LOCAL_______
client = MongoClient()
#_____________________

db = client.path_db
def insert_json(uid, version, body):
	print("in function")
    db.posts.insert_one({"problem_id": str(uid), "version": str(version), "body":body})

def add_problem(problem):
    """
    Creates a new problem and returns a problemID with default version 0
    
    :param problem: Problem object that needs to be updated.
    :type problem: dict | bytes

    :rtype: int
    """
    try:
        print(problem)
        str_body = str(problem).replace('\'', '\"')
        print(str_body)
        json.loads('{"test": 1}')
        print("after_problem")
        problem = Problem.from_dict(connexion.request.get_json())
        db_size = db.posts.count()+1
        print("after_connexion")
        for i in range(1, db_size):
            if(db.posts.find_one({"uid":str(i)}) == None):
                insert_json(i, 0, problem)
                return jsonify({"uid": i})
            print(i)
        create_json(db_size, 0, problem)
        return jsonify({"uid": i})
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
    for post in db.posts.find({}, {"problem_id": 1}):
    	array.append(post)
    #run a check to see if the uid exists
    if array.len == 0:
    	return get_status(404, "No problems found"), status.HTTP_404_NOT_FOUND
    #if the uid doesn't exist then just go ahead return error status
    return jsonify(array)
