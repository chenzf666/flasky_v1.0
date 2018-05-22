from abc import ABCMeta, abstractmethod


class BaseRepository:
    __metaclass__ = ABCMeta

    # get one model
    @abstractmethod
    def get(self, **pk):
        pass

    # find all model filtered by some conditions
    @abstractmethod
    def find(self, **keys):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def create(self, **kw):
        pass

    @abstractmethod
    def all(self):
        pass
