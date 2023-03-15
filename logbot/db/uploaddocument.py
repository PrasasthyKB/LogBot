import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask import Response, request, jsonify, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
# project resources
from models.users import Users
import json
from resources.errors import user_not_found, resource_already_exists
ALLOWED_EXTENSIONS = set(['txt'])


def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadFile(Resource):
    @staticmethod
    @jwt_required()
    def post() -> Response:

        authorized: bool = Users.objects.get(id=get_jwt_identity())
        if authorized:
            user_details= json.loads(Users.objects.get(id=get_jwt_identity()).to_json())
            print(user_details)
            print(type(user_details))
            print(user_details['user_id'])
            if 'file' not in request.files:
                resp = jsonify({'message' : 'No file part in the request'})
                resp.status_code = 400
                return resp
            file = request.files['file']
            if file.filename == '':
                resp = jsonify({'message' : 'No file selected for uploading'})
                resp.status_code = 400
                return resp
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(filename)
                resp = jsonify({'message' : 'File successfully uploaded'})
                resp.status_code = 201 
                return resp 
            else: 
                resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'}) 
                resp.status_code = 400 
                return resp
