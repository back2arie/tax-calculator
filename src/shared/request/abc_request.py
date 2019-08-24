from abc import ABC, abstractmethod

class Request(ABC, object):

    @abstractmethod
    def json_to_dict(): pass

    @abstractmethod
    def query_to_dict(): pass

    @abstractmethod
    def parse_all_to_dict(): pass
