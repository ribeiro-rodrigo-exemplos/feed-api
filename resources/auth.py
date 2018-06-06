from flask_restful import Resource, request
from commons.token_helper import TokenHelper
from commons.config_helper import ConfigHelper
from commons.encrypt_helper import EncryptHelper
from daos.mongo_connection_factory import MongoConnectionFactory
from daos.user_dao import UserDao


class Auth(Resource):

    def __init__(self):

        self.__token_helper = TokenHelper(ConfigHelper())
        self.__encrypt_helper = EncryptHelper()
        self.__mongo_connection_factory = MongoConnectionFactory()

    def post(self):

        connection = None

        try:

            username = request.json['username']
            password = request.json['password']

            connection = self.__mongo_connection_factory.create_connection()

            if self.__user_valid(username, password, connection):
                encoded = self.__token_helper.generate_token(username)
                return {"token": str(encoded, 'utf-8')}

            return '', 401

        except:

            return '', 500

        finally:

            if connection:
                connection.close()

    def __user_valid(self, username, password, connection):
        password = self.__encrypt_helper.encrypt(password)
        user_dao = UserDao(connection)
        user = user_dao.find(username, password)
        return user
