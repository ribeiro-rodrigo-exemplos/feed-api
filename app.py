from resources.feed import Feed
from resources.auth import Auth
from resources.user import User
from flask_restful import Api
from flask import Flask

app = Flask(__name__)
api = Api(app)

api.add_resource(Feed, '/feeds')
api.add_resource(Auth, '/auth/token')
api.add_resource(User, '/users')

if __name__ == '__main__':
    app.run(debug=True)
