from flask import Response, request, abort, jsonify
from flask_restful import Resource
import json
from models.users import Users
from flask_jwt_extended import create_access_token, create_refresh_token
from resources.errors import unauthorized
from models.chat_history import Chat_History
from models.document import User_Document
import datetime
import uuid


class SignUp(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        
        """
        if not request.json:
            abort(415)
        try:
            data = request.get_json() 
            user_id =str(uuid.uuid4()) +"LOGIN"
            data['user_id'] = user_id
            new_user = Users(**data)
            new_user.save()
            
        except KeyError:
            abort(400)
        try:

            response = "Hello " + str(new_user.name)+ ". " +"Welcome to LogBot, Please share your log file for analysis"
            data_load = {"user_id": [], "chat_id":[],"query":[],"response":[], 'document_id' : []}
            data_load['user_id'] = user_id
            data_load['chat_id'] = str(uuid.uuid4()) +"CHAT"
            data_load['query'] = "Introduction"
            data_load['response'] = response
            data_load['document_id'] = str(uuid.uuid4())
            chat_load = Chat_History(**data_load)
            chat_load.save()
            session_response = {'id': str(new_user.id), 'response' : response}
            #print("user_res_sess: ", session_response)
        except KeyError:
                abort(400)
        return Response(json.dumps(session_response), 200)
            
class Login(Resource):
    """
    Flask-resftul resource for retrieving user web token.
    """
    @staticmethod
    def post() -> Response:
        """
        POST response method for retrieving user web token.
        :return: JSON object
        """
        if not request.json:
            abort(415)
        data = request.get_json()
        user = Users.objects.get(email=data.get('email'))
        auth_success = user.check_pw_hash(data.get('password'))
        user_details = json.loads((Users.objects(email=data.get('email')).first()).to_json())
        user_id = user_details["user_id"]
        #chat_load =json.loads((Chat_History.objects(user_id = user_id).first()).to_json())
        query = []
        response = []
        for chat in Chat_History.objects(user_id = user_id):
            chat_details = (json.loads((chat).to_json()))
            query.append(chat_details['query'])
            response.append( chat_details['response'])
        doc_name = []
        doc_summary = []
        doc_tag = []
        for doc in User_Document.objects(user_id = user_id):
            doc_details = (json.loads((doc).to_json()))
            doc_name.append(doc_details['document_name'])
            doc_summary.append(doc_details['document_summary'])
            doc_tag.append(doc_details['document_tag'])
            
        if not auth_success:
            return unauthorized()
        else:
            expiry = datetime.timedelta(days=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
            refresh_token = create_refresh_token(identity=str(user.id))
            session_response=  {'result': {'access_token': access_token,
                                       'refresh_token': refresh_token,
                                       'logged_in_as': f"{user.email}"},
                                'chathistory': {'query':query,
                                                'response':response
                                    },
                                'dochistory':{'document_list': doc_name,
                                    'doc_summaries': doc_summary,
                                    'doc_tag': doc_tag}
                                }
            #print(session_response['chathistory']['query'][0])
            return jsonify(session_response)
        