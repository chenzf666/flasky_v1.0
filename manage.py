#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('models', MigrateCommand)
if __name__ == '__main__':
    with app.app_context():
        from app.models.user import User
        from app.models.role import Role
        from app.models.post import Post
        db.drop_all()
        db.create_all()
        Role.insert_roles()
        User.create_user()
        db.session.add_all([Post(body='#默认自己关注自己支持富文本', author_id=1), Post(body='#第二条微博<i>斜体字</i>', author_id=2)])
        db.session.commit()
        User.generate_fake(30)
        Post.generate_fake(150)
        User.add_self_follows()
        manager.run()
