import connexion
import json
import os
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
#____FOR DOCKER______
#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
#____________________

#____FOR LOCAL_______
client = MongoClient()
#_____________________

db = client.path_db

def insert_json(uid, version, body):
    print("inside func")
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
        db_size = db.posts.count()+1
        print("after_problem")
        problem = Body.from_dict(connexion.request.get_json())
        for i in range(1, db_size):
            if(db.posts.find_one({"problem_id":str(i)}) == None):
                insert_json(i, 0, problem)
                return jsonify({"problem_id": i})
            print(i)
        insert_json(db_size, 0, problem)
        print("out of func")
        return jsonify({"problem_id": db_size})
    except ValueError:
        print("error")
        return get_status(500, "Invalid JSON"), status.HTTP_500_INTERNAL_SERVER_ERROR


def get_problems():
    """
    Problems
    Returns a list of all of the Problems generated. This can be an empty list. 

    :rtype: List[int]
    """
    return 'do some magic!'
