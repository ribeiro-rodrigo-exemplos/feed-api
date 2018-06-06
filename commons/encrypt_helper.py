from hashlib import md5


class EncryptHelper:

    @staticmethod
    def encrypt(value):
        return md5(value.encode('utf-8')).hexdigest()
