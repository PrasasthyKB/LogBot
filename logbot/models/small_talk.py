"""
This module contains the Model class for our small talk, and click functions callable
    from the command line

The functions are responsible for initiliazing and populating the database and running the tests
"""

from mongoengine import ( Document, StringField, ListField)

class Small_Talk(Document):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
    :param tag: Tag attributed to this small talk
    :param patterns: array of strings that represents the users small talk
    :param responses: array of strings that represents the logbots response to users small talk
    :param context: array of string that represents the context of the small talk
    """
    
   
    patterns = ListField(StringField(max_length=100))
    responses = ListField(StringField(max_length=100))

    # JSON SCHEMA
    @staticmethod
    def json_schema():
        """
        :return: the valid JSON schema for the Assessment class
        """
        schema = {
            "type": "object",
            "required": ["patterns","responses"]
        }
        props = schema["properties"] = {}
        props["patterns"] = {
            "description": "Array of patterns in small talk chat",
            "type": "array",
        }
        props["responses"] = {
            "description": "Array of responses in small talk chat",
            "type": "array",
        }

        return schema
    
 