# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.comment import Comment

post_parser = reqparse.RequestParser()
post_parser.add_argument('body', required=True, help='Please give me a comment!')
post_parser.add_argument('post_id', required=True, type=int, help='Please give me a post_id!')
post_parser.add_argument('author_id', required=True, type=int, help='Please give me a author_id!')


class CommentApi(Resource):
    def post(self):
        args = post_parser.parse_args()
        from app.models.post import Post
        post = Post.query.get_or_404(args.post_id)
        from app.models.user import User
        author = User.query.get_or_404(args.author_id)
        comment = Comment(body=args.body, post=post, author=author)
        from app import db
        db.session.add(comment)
        db.session.commit()
        return jsonify(comment.to_json())

    def get(self, id=None):
        if id:
            comment = Comment.query.get_or_404(id)
            return jsonify(comment.to_json())
        else:
            comments = Comment.query.all()
            return jsonify({'comments': [comment.to_json() for comment in comments]})

    def put(self):
        # ...
        pass

    def delete(self, id):
        comment = Comment.query.get_or_404(id)
        from app import db
        db.session.delete(comment)
        db.session.commit()
        return jsonify(comment.to_json())
