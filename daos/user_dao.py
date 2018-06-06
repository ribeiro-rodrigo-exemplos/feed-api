
class UserDao:

    def __init__(self, connection):
        self.__connection = connection

    def save(self, user):
        users_collection = self.__connection.get_collection('users')
        return users_collection.insert_one(user).inserted_id

    def find(self, username, password):
        user_collection = self.__connection.get_collection('users')
        return user_collection.find_one({'username': username, 'password': password})