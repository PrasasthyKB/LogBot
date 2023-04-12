from flask import Response, request, abort, jsonify
from flask_restful import Resource
import json
from models.chat_history import Chat_History
from flask_jwt_extended import jwt_required, get_jwt_identity


class ChatHistory(Resource):
    
    @jwt_required()
    def get(self, user_id: str) -> Response:
        pass
    
    @jwt_required()
    def post(self, user_id: str) -> Response:
        pass
    
    @jwt_required()
    def delete(self, user_id: str) -> Response:
        pass
    
    @jwt_required()
    def put(self, user_id: str) -> Response:
        pass
