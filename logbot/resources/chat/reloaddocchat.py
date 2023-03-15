from flask import  request,  Response, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
# project resources
from models.users import Users
from models.document import User_Document
from models.chat_history import Chat_History
import json
from resources.errors import user_not_found, resource_already_exists


class ReloadDoc(Resource):
    @staticmethod
    @jwt_required()
    def post() -> Response:
        
        authorized: bool = Users.objects.get(id=get_jwt_identity())
        if authorized:
            user_details= json.loads(Users.objects.get(id=get_jwt_identity()).to_json())

            print(user_details['user_id'])
            if not request.json:
                abort(415)
            data = request.get_json()
            doc_details = json.loads(User_Document.objects.get(document_id=data.get('document_id')).to_json())
            
            print(data["reloaddocchat"])
            query = []
            response = []
            timestamp_sort = []
            if data["reloaddocchat"] == "True":
                for chat in Chat_History.objects(document_id=data.get('document_id')):
                    chat_details = (json.loads((chat).to_json()))
                    query.append(chat_details['query'])
                    response.append( chat_details['response'])
                    timestamp_sort.append( chat_details['timestamp'])
                    
                session_response = {'message' : "Document and chat reloaded", 
                                    'chathistory': {'query':query,
                                'response':response,
                                'timestamp' :timestamp_sort
                    },
                'docdetails':{
                    'document_id': doc_details['document_id'],
                    'document_name': doc_details['document_name'],
                    'doc_summaries': doc_details['document_summary'],
                    'doc_tag': doc_details['document_tag'],
                    'doc_timestamp' : doc_details['timestamp'] }
                } 
        return Response(json.dumps(session_response), 200)
    