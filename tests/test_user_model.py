# -*- coding: utf-8 -*-
import unittest
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.models.anonymousUser import AnonymousUser


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(email='example@qq.com', username='aaa', password='666')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_setter(self):
        u = User(email='example@qq.com', username='aaa', password='666')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(email='example@qq.com', username='aaa', password='666')
        self.assertTrue(u.verify_password('666'))
        self.assertFalse(u.verify_password('777'))

    def test_password_salts_are_random(self):
        u1 = User(email='example1@qq.com', username='aaa', password='666')
        u2 = User(email='example2@qq.com', username='bbb', password='666')
        self.assertTrue(u1.password_hash != u2.password_hash)

    def test_roles_and_permission(self):
        Role.insert_roles()
        u = User(email='example@qq.com', username='aaa', password='666')
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
