import jwt
from datetime import datetime, timedelta


class TokenHelper:

    def __init__(self, config_helper):
        self.__secret = config_helper.config['auth']['secret']
        self.__algorithm = config_helper.config['auth']['algorithm']
        self.__expiration_hours = int(config_helper.config['auth']['expiration_hours'])

    def generate_token(self, username):

        expiration = datetime.utcnow() + timedelta(hours=self.__expiration_hours)

        encoded = jwt.encode({'user': username, 'exp': expiration}, self.__secret,
                             algorithm=self.__algorithm)

        return encoded

    def is_valid(self, token):
        try:
            jwt.decode(token, self.__secret, algorithms=[self.__algorithm])
            return True
        except:
            return False
