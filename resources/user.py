from flask_restful import Resource, request
from daos.mongo_connection_factory import MongoConnectionFactory
from daos.user_dao import UserDao
from commons.encrypt_helper import EncryptHelper
from pymongo.errors import DuplicateKeyError


class User(Resource):

    def __init__(self):

        self.__mongo_connection_factory = MongoConnectionFactory()

    def post(self):

        user = request.json

        if 'username' not in user or 'password' not in user:
            return 'O usuário cadastrado está inválido', 422

        user['password'] = EncryptHelper.encrypt(user['password'])

        connection = None

        try:

            connection = self.__mongo_connection_factory.create_connection()
            user_dao = UserDao(connection)
            user_dao.save(user)

            return '', 201

        except DuplicateKeyError:

            return 'Nome de usuario encontra-se em uso', 422

        except:

            return '', 500

        finally:

            if connection:
                connection.close()

