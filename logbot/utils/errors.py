from flask import Response, jsonify


def unauthorized() -> Response:
    output = {"error":
              {"msg": "401 error: Email or password is invalid."}
              }
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp

def invalid_route() -> Response:
    output = {"error":
              {"msg": "404 error: This route is not supported"}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp

def user_not_found() -> Response:
    output = {"error":
              {"msg": "404 error: User not Found"}
              }
    resp = jsonify({'result': output})
    resp.status_code = 404
    return resp

def resource_already_exists() -> Response:
    output = {"error":
              {"msg": "400 error: User not Found"}
              }
    resp = jsonify({'result': output})
    resp.status_code = 400
    return resp
