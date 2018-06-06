from commons.config_helper import ConfigHelper
from pymongo import MongoClient
from daos.mongo_connection import MongoConnection


class MongoConnectionFactory:
    def __init__(self):
        config = ConfigHelper().config
        self.__host = config['database']['host']
        self.__port = config['database']['port']

    def create_connection(self):
        client = MongoClient(self.__host, int(self.__port))
        feed_db = client['feed']

        return MongoConnection(client, feed_db)

