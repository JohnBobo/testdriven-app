# services/users/project/__init__.py
import sys
import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

print(app.config, file=sys.stderr)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object('project.config.DevelopmentConfig')

# instantiate the db
db = SQLAlchemy(app)


# model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    aactive = db.Column(db.Boolean(), defualt=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UsersPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!',
        }


api.add_resource(UsersPing, '/users/ping')
