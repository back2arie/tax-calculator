from abc import ABCMeta, abstractmethod

class Validator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_valid(self): pass

    @abstractmethod
    def get_errors(self): pass

    @abstractmethod
    def get_valid_data(self): pass

    @abstractmethod
    def get_default_param(self): pass
