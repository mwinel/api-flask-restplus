from flask_restplus import Api
from flask import Blueprint
from app.main.resources.user_resource import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title = 'Flask RESTplus API boilerplate',
    version = 1.0, description = 'A boilerplate for a flask web service'
)

api.add_namespace(user_ns, path = '/users')
