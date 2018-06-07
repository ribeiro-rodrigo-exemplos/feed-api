from resources.feed import Feed
from resources.auth import Auth
from resources.user import User
from flask_restful import Api
from flask import Flask

import os

app = Flask(__name__)
api = Api(app)

api.add_resource(Feed, '/feeds')
api.add_resource(Auth, '/auth/token')
api.add_resource(User, '/users')

if __name__ == '__main__':
    port = os.environ['PORT'] if 'PORT' in os.environ else 5000
    app.run(debug=True, host='0.0.0.0', port=port)
