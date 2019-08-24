from config.config import Config
from src.shared.use_case import UseCase
from src.shared.response_object import ResponseSuccess
from src.tax.v1.serializers.tax_serializers import ListTax

class ListTaxUsecase(UseCase):
    """
    Use case for list tax object.

    Story:
        As user I want to see my bill.

    Attributes:
        repo: Repository instance.
    """

    def __init__(self, repo):
        """Construct List Tax Use case."""

        self.repo = repo

    def process_request(self, request_objects):
        """Performs List Tax Use case."""

        tax = self.repo.get_all(request_objects)
        schema = ListTax()
        serialize = schema.dump(tax, many=True)

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.SUCCESS],
            'message': Config.SUCCESS.lower(),
            'meta': {
                'priceSubtotal': self.repo.get_price_subtotal(),
                'taxSubtotal': self.repo.get_tax_subtotal(),
                'grandTotal': self.repo.get_grand_total(),
            },
            'data': serialize.data
        }

        return ResponseSuccess(response)

class CreateTaxUsecase(UseCase):
    """
    Use case for create tax object.

    Story:
        As user I want to create my tax object.

    Attributes:
        repo: Repository instance.
    """

    def __init__(self, repo):
        """Construct Create Tax Use case."""

        self.repo = repo

    def process_request(self, request_objects):
        """Performs Create Tax Use case."""

        tax = self.repo.create(request_objects)
        data = {
            "name": request_objects.name
        }

        response = {
            'success': True,
            'code': Config.STATUS_CODES[Config.CREATED],
            'message': Config.SUCCESS.lower(),
            'data': data
        }

        return ResponseSuccess(response, Config.CREATED)
