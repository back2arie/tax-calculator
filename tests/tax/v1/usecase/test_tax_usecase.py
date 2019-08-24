from unittest import mock

from math import ceil

from config.config import Config
from schemas.json.loader import JSONSchemaLoader
from src.tax.v1.domain.tax import Tax
from src.tax.v1.serializers.tax_serializers import ListTax
from src.tax.v1.usecase.tax_use_cases import ListTaxUsecase
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

def domain_tax():
    tax_1 = Tax.from_dict(
        {
            'id': 1,
            'name': 'Lucky Stretch',
            'tax_code': 2,
            'tax_code_type': 'Tobacco',
            'price': 1000,
        }
    )

    tax_2 = Tax.from_dict(
        {
            'id': 2,
            'name': 'Big Mac',
            'tax_code': 1,
            'tax_code_type': 'Food & Beverage',
            'price': 1000,
        }
    )

    return [tax_1, tax_2]

def test_tax_get_all():
    total = len(domain_tax())

    repo = mock.Mock()
    repo.get_all.return_value = domain_tax()
    repo.get_total.return_value = total

    tax_get_all_usecase = ListTaxUsecase(repo=repo)
    request_objects = True
    total_page = 1

    response_object = tax_get_all_usecase.execute(request_objects)
    serialize = ListTax(many=True).dump(domain_tax())
    expected_return = {
        'success': True,
        'code': Config.STATUS_CODES[Config.SUCCESS],
        'message': Config.SUCCESS.lower(),
        'data': serialize.data
    }

    assert response_object.value == expected_return
