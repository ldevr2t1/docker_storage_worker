from . import utilities

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
db = client.path_db


def delete_problem(problem_id):
    """
    Delete Problem
    This removes the problem by the given ID 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: None
    """
    if db.posts.delete_many({"problem_id": str(problem_id)}).deleted_count == 0:
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
