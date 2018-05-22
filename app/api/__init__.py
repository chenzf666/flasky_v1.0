# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from .resources.user import UserApi
from .resources.post import PostApi
from .resources.comment import CommentApi

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(UserApi, '/users', '/users/<int:id>')
api.add_resource(PostApi, '/posts', '/posts/<int:id>')
api.add_resource(CommentApi, '/comments', '/comments/<int:id>')
