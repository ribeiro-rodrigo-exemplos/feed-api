from flask_restful import Resource, wraps, request
from commons.token_helper import TokenHelper
from commons.config_helper import ConfigHelper

token_helper = TokenHelper(ConfigHelper())


def auth_interceptor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if 'Authorization' in request.headers and token_helper.is_valid(request.headers['Authorization']):
            return func(*args, **kwargs)

        return '', 401

    return wrapper


class Protected(Resource):
    method_decorators = [auth_interceptor]
