from mongoengine import ( Document, StringField, DateTimeField,)
import datetime


class Chat_History(Document):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
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

    
    
    
    