from flask_restplus import Resource
from app.main.utils.dto import UserDto
from app.main.core.user_helper import (new_user, get_users, 
    get_user_by_id)

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('create new user')
    @api.expect(_user, validate = True)
    def post(self):
        '''Resource to create new user'''
        return new_user()

    @api.doc('list of all users')
    @api.marshal_list_with(_user, envelope = True)
    def get(self):
        '''Resource to return a list of users'''
        return get_users()

@api.route('/<int:id>')
@api.param('id', 'the user identifier')
@api.response(404, 'user not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, id):
        '''Resource to return a user'''
        user = get_user_by_id(id)
        if not user:
            api.abort(404)
        else:
            return user
