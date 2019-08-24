from abc import ABCMeta, abstractmethod

class TaxCodeRepository(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_type_by_code(self, code): pass
