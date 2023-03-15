from mongoengine import ( Document, StringField, DateTimeField, FileField)
import datetime

class User_Document(Document):
    """
    Template for a mongoengine document, which represents a user.
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
    
    
    
    