import configparser


class ConfigHelper:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.__config = config

    @property
    def config(self):
        return self.__config
