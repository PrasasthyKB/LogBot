"""
This module contains all the classes related to the Users LogFile:
 - the collection of user Owned LogFiles
 - a singular log file
 - the related URL converter
"""

import json
import uuid
import textract

from jsonschema import validate, ValidationError
from flask import  request,  jsonify, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from werkzeug.utils import secure_filename

from models.users import Users
from models.document import LogFile
from models.chat_history import Chat_History
from utils.errors import invalidCredentials, invalid_schema, missing_resource
from utils.constants import ALLOWED_EXTENSIONS
from utils.utils import build_logfile_response

class LogFileCollection(Resource):
    """Class that represents the a collection of user owned logfiles

    Args:
        Resource (_type_): _description_
    """
    @jwt_required()
    def post(self):
        """Add a logfile 
        """
        valid_user: bool = Users.objects.get(id=get_jwt_identity())
        file = request.files['file']
            
        if not valid_user:
           return invalidCredentials()
        
        try:
            validate(request.json, LogFile.json_schema())
        except ValidationError:
           return invalid_schema()
      
        if not request.files:
            return missing_resource()
        
        if file and allowed_file(file.filename):
            #Save File
            file.save(secure_filename(file.filename))
            # Save 
            logfile = LogFile()
            logfile.deserialize(request.json)
            try:
                logfile.save()
            except Exception:
                resp = jsonify({'error': 'Unable to save Logfile'})
                resp.status_code = 400
                return resp
            
            chat_history = Chat_History()
            doc = {
                'user_id': logfile.user_id,
                'chat_id': logfile.chat_id,
                'query': 'Upload Log File',
                'response': 'File successfully uploaded. Opt for summary',
                'document_id': logfile.document_id
            }
            chat_history.deserialize(doc)
            chat_history.save()
            query = []
            response = []
            timestamp_sort = []
            for chat in Chat_History.objects(user_id = logfile.user_id):
                chat_details = (json.loads((chat).to_json()))
                query.append(chat_details['query'])
                response.append( chat_details['response'])
                timestamp_sort.append( chat_details['timestamp'])
                
            doc_name = []
            doc_summary = []
            doc_tag = []
            doc_timestamp = []
            for doc in LogFile.objects(user_id = logfile.user_id):
                doc_details = (json.loads((doc).to_json()))
                doc_name.append(doc_details['document_name'])
                doc_summary.append(doc_details['document_summary'])
                doc_tag.append(doc_details['document_tag'])
                doc_timestamp.append(doc_details['timestamp'])
        # if file.filename != logfile.filename:
        #     return missing_resource()
        #THIS LINE IS WRONG
        return Response(json.dumps(build_logfile_response(query, response, timestamp_sort, doc)), 200)

        
        
        
def allowed_file(filename):
    """check file extensions to only allow accepted file extensions

    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

        