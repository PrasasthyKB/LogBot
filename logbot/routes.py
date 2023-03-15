from flask_restful import Api
# Project Resources
from resources.authentication import SignUp, Login
from resources.actions import UserApi
from resources.uploaddocument import UploadFile
from resources.generatesummary import GenSumm
from resources.generatetag import GenTag
from resources.deletedocall import DelDoc
from resources.deletesum import DelSumm
from resources.deletetag import DelTag
from resources.reloaddocchat import ReloadDoc
from resources.updatesum import UpdateSum
from resources.updatetag import UpdateTag
from resources.chatwindowQ import QueriesRes

def create_routes(api: Api):
    """
    Adds resources to the api.
    :param api: Flask-RESTful Api Object
    
    """
    
    # User Authentication 
    api.add_resource(SignUp, '/authentication/signup/')
    api.add_resource(Login, '/authentication/login/')

    # Platform Users
    api.add_resource(UserApi, '/actions/user_action')
    api.add_resource(UploadFile, '/uploaddocument/uploadfile/')
    api.add_resource(GenSumm, '/generatesummary/GenSumm/')
    api.add_resource(GenTag, '/generatetag/GenTag/')
    api.add_resource(DelDoc, '/deletedocall/DelDoc/')
    api.add_resource(DelSumm, '/deletesum/DelSumm/')
    api.add_resource(DelTag, '/deletetag/DelTag/')
    api.add_resource(ReloadDoc, '/reloaddocchat/ReloadDoc/')
    api.add_resource(UpdateSum, '/updatesum/UpdateSum/')
    api.add_resource(UpdateTag, '/updatetag/UpdateTag/')
    api.add_resource(QueriesRes, '/chatwindowQ/QueriesRes/')
    