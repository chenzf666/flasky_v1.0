import inject
from app.repositorys.comment_repository import CommentRepository


class CommentService:
    comment_repository = inject.attr(CommentRepository)

    pass
