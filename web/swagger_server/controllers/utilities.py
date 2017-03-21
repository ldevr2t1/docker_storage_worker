import json
import os
import connexion
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from flask import jsonify
from flask.ext.api import status
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