import inject
import random
from app.repositorys.user_repository import UserRepository
from app.repositorys.post_repository import PostRepository


class PostService:
    user_repository = inject.attr(UserRepository)
    post_repository = inject.attr(PostRepository)

    def generate_fake(self, count=100):
        from random import randint
        import forgery_py

        user_count = len(self.user_repository.all())
        for i in range(count):
            id = random.randint(0, user_count - 1)
            u = self.user_repository.get(id=id)
            p = self.post_repository.create(body=forgery_py.lorem_ipsum.sentences(randint(1, 3)),
                                            timestamp=forgery_py.date.date(True),
                                            author=u)
            self.post_repository.add(p)
