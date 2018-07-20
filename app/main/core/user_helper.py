from flask_restplus import reqparse
from app.main.models.user import User

def new_user():
    '''Create a new user'''
    parser = reqparse.RequestParser()
    parser.add_argument('username', required = True)
    parser.add_argument('email', required = True)
    parser.add_argument('password', required = True)
    
    data = parser.parse_args()
    user = {
        "id": User.users[-1]['id'] + 1,
		"username": data["username"],
		"email": data["email"],
		"password": data["password"]
    }
    User.users.append(user)
    return {
        'message': 'User succesfully created'
    }, 201

def get_users():
    '''Return a list of users'''
    return User.users, 200

def get_user_by_id(id):
    '''Return a user by id'''
    return [user for user in User.users if user['id'] == id]
