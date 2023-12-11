from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def fit():
        pass

    @abstractmethod
    def generate():
        pass

    @abstractmethod
    def evaluate():
        pass


