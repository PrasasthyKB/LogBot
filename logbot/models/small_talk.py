from mongoengine import ( Document, StringField, DateTimeField, ListField)


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
 