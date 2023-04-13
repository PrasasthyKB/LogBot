"""
This module contains the Model class for our LogFile, and click functions callable
    from the command line

The functions are responsible for initiliazing and populating the database, generating the
    admin key, and running the tests
"""
import datetime
from mongoengine import ( Document, StringField, DateTimeField)


class LogFile(Document):
    """
    Template for a mongoengine document, which represents a LogFile.
    Password is automatically hashed before saving.
    :param user_id: unique required login value
    :param documentId: required unique document id
    :param document: option unique string username
    :param document_summary: string representation of documents summary
    :param timestamp: timestamp of entry
    """
    
    user_id = StringField(required=True)
    document_id = StringField(required=True, unique= True)
    document_name  = StringField(required=True)
    chat_id = StringField(required=True)
    document = StringField(required=False)
    document_summary = StringField(max_length=6000)
    document_tag = StringField(required =True)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

    # JSON SCHEMA
    @staticmethod
    def json_schema():
        """
        :return: the valid JSON schema for the Assessment class
        """
        schema = {
            "type": "object",
            "required": ["user_id","document_id", "document_name", "chat_id", "document", "document_summary", "document_tag", "timestamp"]
        }
        props = schema["properties"] = {}
        props["user_id"] = {
            "description": "User Identifier",
            "type": "string",
        }
        props["document_id"] = {
            "description": "Document identifier",
            "type": "string",
        }
        props["document_name"] = {
            "description": "Title of the document/logfile",
            "type": "string"
        }
        props["chat_id"] = {
            "description": "Chat Identifier",
            "type": "string",
        }
        props["document"] = {
            "description": "The Document Contents",
            "type": "string",
        }
        props["document_summary"] = {
            "description": "Summay related to the document",
            "type": "string",
        }
        props["document_tag"] = {
            "description": "The Document Tag",
            "type": "string",
        }
        props["timestamp"] = {
            "description": "Timestamp of document/logfile marking in format yyyy-mm-dd",
            "type": "string",
            "format": "date-time"
        }
        return schema
    