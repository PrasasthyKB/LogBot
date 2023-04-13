"""
This module contains the Model class for our chat history, and click functions callable
    from the command line

The functions are responsible for initiliazing and populating the database and running the tests
"""
import datetime
from mongoengine import ( Document, StringField, DateTimeField,)


class Chat_History(Document):
    """
    Template for a mongoengine document, which represents the chat_history.
    :param user_id: unique required login value
    :param chat_id: unique required chat id
    :param query: question to ask chatbot
    :param response: chatbot response
    :param documentId: document id
    :param timestamp: timestamp of entry
    """
    
    user_id = StringField(required=True)
    chat_id = StringField(required=True)
    query = StringField(required=False)
    response = StringField(required=True)
    document_id = StringField(required=False)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

    # JSON SCHEMA
    @staticmethod
    def json_schema():
        """
        :return: the valid JSON schema for the Assessment class
        """
        schema = {
            "type": "object",
            "required": ["user_id", "chat_id", "query", "response", "document_id", "timestamp"]
        }
        props = schema["properties"] = {}
        props["user_id"] = {
            "description": "User Identifier",
            "type": "string",
        }
        props["chat_id"] = {
            "description": "Chat Identifier",
            "type": "string",
        }
        props["query"] = {
            "description": "User Query sent to the logbot",
            "type": "string"
        }
        props["response"] = {
            "description": "Response to query from the logbot",
            "type": "string",
        }
        props["document_id"] = {
            "description": "Document Identifier",
            "type": "string",
        }
        props["timestamp"] = {
            "description": "Timestamp of document/logfile marking in format yyyy-mm-dd",
            "type": "string",
            "format": "date-time"
        }
        return schema
    