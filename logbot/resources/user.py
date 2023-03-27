from flask import Response, request, jsonify, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from models.users import Users
from resources.errors import user_not_found, resource_already_exists

class UserApi(Resource):
    """
    Flask-resftul resource for returning db.loginprofile collection.
    """
    @jwt_required()
    def get(self, user_id: str) -> Response:
        """
        GET response method for acquiring single user data.
        JSON Web Token is required.
        :return: JSON object
        """
        authorized = Users.objects.get(id=get_jwt_identity())

        if authorized is None:
            return user_not_found()
        else:
            output = Users.objects.get(id=user_id)
            return jsonify({'result': output})

    @jwt_required()
    def put(self, user_id: str) -> Response:
        """
        PUT response method for updating a user.
        JSON Web Token is required.
        Authorization is required: UserId = get_jwt_identity()
        :return: JSON object
        """
        authorized = Users.objects.get(id=get_jwt_identity())

        if authorized is not None:
            data = request.get_json()
            put_user = Users.objects(id=user_id).update(**data)
            output = {'id': str(put_user.id)}
            return jsonify({'result': output})
        else:
            return user_not_found()

    @jwt_required()
    def post(self) -> Response:
        """
        POST response method for creating user.
        JSON Web Token is required.
        :return: JSON object
        """
        # authorized = Users.objects.get(id=get_jwt_identity())
        if not request.json:
            abort(415)
        try:
            data = request.get_json()
            print(data)
            post_user = Users(**data).save()
            output = {'id': str(post_user.id)}
        except KeyError:
            abort(400)
        return jsonify({'result': output})            

    @jwt_required()
    def delete(self, user_id: str) -> Response:
        """
        DELETE response method for deleting user.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        # try:
        #     output = Users.objects(id=user_id).delete()
        #     return jsonify({'result': output})
        # except Exception as e:
        #     print(e)
        #     return jsonify({"error": str(e)})
        authorized = Users.objects.get(id=get_jwt_identity())

        if authorized is not None:
            output = Users.objects(id=get_jwt_identity()).delete()
            return jsonify({'result': output})
        else:
            return user_not_found()