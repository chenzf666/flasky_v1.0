from .base_repository import BaseRepository


class PostRepository(BaseRepository):
    def __init__(self, model, session):
        self.model = model
        self.session = session

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def delete(self, entity):
        self.session.delete(entity)
        self.session.commit()

    def get(self, **pk):
        return self.model.query.filter_by(**pk).first()

    def get_or_404(self, id):
        return self.model.query.get_or_404(id)

    def find(self, **keys):
        return self.model.query.filter_by(**keys).all()

    def create(self, **kw):
        return self.model(**kw)

    def all(self):
        return list(self.session.query(self.model).all())
