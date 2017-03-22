import connexion
from swagger_server.models.body import Body
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
#____________________

db = client.path_db

def create_json(uid, version, body):
    #gotta check if the body is valid jsonc
    return jsonify({"problem_id":str(uid), "version": str(version), "body":str(body)})


def insert_json(uid, version, body):
    db.posts.insert_one({"problem_id": str(uid), "version": str(version), "body":body})


def get_status(status, message):
    return jsonify({"Status": status, "Message": message})


def root_get():
    return 'This is version 2.0'

def delete_problem(problem_id):
    """
    Delete Problem
    This removes the problem by the given ID 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: None
    """
    if db.posts.delete_many({"uid": str(uid)}).deleted_count == 0:
        return get_status(404, "NOT FOUND"), status.HTTP_404_NOT_FOUND
    else:
        return get_status(200, "Successfully Deleted")
        
def get_problem(problem_id):
    """
    Problems
    Returns most updated problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """
    ret_object = db.posts.find_one({"problem_id": str(problem_id)})
    #run a check to see if the uid exists
    if ret_object is None:
        return get_status(404, "COULD NOT FIND"), status.HTTP_404_NOT_FOUND
    #if the uid doesn't exist then just go ahead return error status
    ret_object.pop('problem_id', 0)
    return jsonify(ret_object)


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
    #this checks if incoming data is valid json and for valid uid
    try:
        str_body = str(problem).replace('\'', '\"')
        json.loads(str_body)
        #update the version
        new_version = version + 1
        body = GenericObject.from_dict(connexion.request.get_json())
        if db.posts.find_one_and_update({"problem_id":str(uid), "version": str(version)}, {"$set": {"body": body, "version": new_version}}) is None:
            return get_status(404, "COULD NOT FIND"), status.HTTP_404_NOT_FOUND
        #need to write better messages to return for a success
        return jsonify(new_version)
    except ValueError:
        return get_status(500, "Invalid JSON"), status.HTTP_500_INTERNAL_SERVER_ERROR

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
    return 'do some magic!'
