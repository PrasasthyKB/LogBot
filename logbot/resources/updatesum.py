from flask import  request,  Response, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
# project resources
from models.users import Users
from models.document import User_Document
from models.chat_history import Chat_History
import json
from resources.errors import user_not_found, resource_already_exists


class UpdateSum(Resource):
    @staticmethod
    @jwt_required()
    def patch() -> Response:
        
        authorized: bool = Users.objects.get(id=get_jwt_identity())
        if authorized:
            user_details= json.loads(Users.objects.get(id=get_jwt_identity()).to_json())

            print(user_details['user_id'])
            if not request.json:
                abort(415)
            data = request.get_json()
            doc_details = json.loads(User_Document.objects.get(document_id=data.get('document_id')).to_json())
            print(data["updatesum"])
            
            if data["updatesum"] == "True":
                new_summary_gen = data.get('new_summary')
                User_Document.objects(document_id=data.get('document_id')).update_one(set__document_summary=new_summary_gen)
                data_load_chat = {"user_id": [], "chat_id":[],"query":[],"response":[], 'document_id' : []}
                data_load_chat['user_id'] = user_details['user_id']
                data_load_chat['chat_id']= doc_details['chat_id']
                data_load_chat['query'] = "update summary"
                data_load_chat['response'] = 'Successfully updated summary for the file'
                data_load_chat['document_id'] = doc_details['document_id']
                chat_load = Chat_History(**data_load_chat)
                chat_load.save()
                session_response = {'message' : data_load_chat['response'], 'summary': new_summary_gen} 
        return Response(json.dumps(session_response), 200)
    