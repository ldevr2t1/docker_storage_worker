import connexion
import json
import os
from flask import jsonify
from flask.ext.api import status
from swagger_server.models.error import Error
from swagger_server.models.generic_object import GenericObject
from swagger_server.models.uid_info import UidInfo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from pymongo import MongoClient
from flask.ext.api import status

def create_json(uid, version, body):
	#gotta check if the body is valid jsonc
	return jsonify({"problem_id":str(uid), "version": str(version), "body":str(body)})


def insert_json(uid, version, body):
	db.posts.insert_one({"problem_id": str(uid), "version": str(version), "body":body})


def get_status(status, message):
	return jsonify({"Status": status, "Message": message})


def root_get():
	return 'This is version 2.0'