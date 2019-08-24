from config.config import Config
from src.shared.use_case import UseCase
from src.shared.response_object import CommonResponse, ResponseSuccess
from src.tax.v1.serializers.tax_serializers import ListTax

class ListTaxUsecase(UseCase): 

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        tax  = self.repo.get_all(request_objects)
        total     = self.repo.get_total(request_objects)
        schema    = ListTax()
        serialize = schema.dump(tax, many=True)

        response  = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'data': serialize.data
        }

        return ResponseSuccess(response)

class CreateTaxUsecase(UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        tax  = self.repo.create(request_objects)
        data = {
            "id": tax
        }

        response  = {
            'success': True,
            'code': Config.STATUS_CODES[Config.CREATED],
            'message': Config.SUCCESS.lower(),
            'data': data
        }

        return ResponseSuccess(response, Config.CREATED)
