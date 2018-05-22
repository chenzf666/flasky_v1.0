import inject

from app.repositorys.post_repository import PostRepository
from app.repositorys.user_repository import UserRepository


class UserService:
    user_repository = inject.attr(UserRepository)

    def create_user(self):
        from flask import current_app
        user1 = self.user_repository.create(email=current_app.config['FLASKY_ADMIN'], username='管理员的账号', password='111',
                                            confirmed=True)
        user2 = self.user_repository.create(email='2460415145@qq.com', username='某个小号', password='111', confirmed=True)
        self.user_repository.add(user1)
        self.user_repository.add(user2)

    def generate_fake(self, count=100):
        import forgery_py
        for i in range(count):
            u = self.user_repository.create(
                email=forgery_py.internet.email_address(),
                username=forgery_py.internet.user_name(True),
                password=forgery_py.lorem_ipsum.word(),
                confirmed=True,
                name=forgery_py.name.full_name(),
                location=forgery_py.address.city(),
                about_me=forgery_py.lorem_ipsum.sentence(),
                member_since=forgery_py.date.date(True)
            )
            self.user_repository.add(u)

    def add_self_follows(self):
        for user in self.user_repository.all():
            if not user.is_following(user):
                user.follow(user)
                self.user_repository.add(user)
