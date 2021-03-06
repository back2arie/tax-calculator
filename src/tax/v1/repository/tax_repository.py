from abc import ABCMeta, abstractmethod

class TaxRepository():
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, adict): pass

    @abstractmethod
    def get_all(self, request): pass
