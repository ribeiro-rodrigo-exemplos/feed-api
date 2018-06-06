
class MongoConnection:
    def __init__(self, connection, db):
        self.__connection = connection
        self.__db = db

    def get_collection(self, collection):
        return self.__db[collection]

    def close(self):
        self.__connection.close()