"""
This module contains the Model class for our users, and click functions callable
    from the command line

The functions are responsible for initiliazing and populating the database and running the tests
"""
import datetime
from mongoengine import ( Document, StringField, EmailField, DateTimeField,)
from flask_bcrypt import generate_password_hash, check_password_hash

class Users(Document):
    """
    Template for a mongoengine document, which represents a user.
    Password is automatically hashed before saving.
    :param email: unique required email-string value
    :param password: required string value, longer than 6 characters
    :param name: option unique string username
    """
    user_id  = StringField(required=True,unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    name = StringField(unique=False)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)

    # JSON SCHEMA
    @staticmethod
    def json_schema():
        """
        :return: the valid JSON schema for the Assessment class
        """
        schema = {
            "type": "object",
            "required": ["user_id","email", "password", "name", "timestamp"]
        }
        props = schema["properties"] = {}
        props["user_id"] = {
            "description": "User Identifier",
            "type": "string",
        }
        props["email"] = {
            "description": "User email",
            "type": "string",
        }
        props["password"] = {
            "description": "User password",
            "type": "string"
        }
        props["name"] = {
            "description": "User name",
            "type": "string",
        }
        props["timestamp"] = {
            "description": "Timestamp of document/logfile marking in format yyyy-mm-dd",
            "type": "string",
            "format": "date-time"
        }
        return schema
    

    def generate_pw_hash(self):
        """
        Function to hash the user password
        
        """
        self.password = generate_password_hash(password=self.password).decode('utf-8')
    
    #BCrypt for password hashing
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        """
        Function to check the hash of the user entered password
        
        """
        return check_password_hash(pw_hash=self.password, password=password)
    
    #BCrypt for password hashing
    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        if self._created:
            self.generate_pw_hash()
        super(Users, self).save(*args, **kwargs)
