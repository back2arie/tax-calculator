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
            'refundable': 'No',
            'price': 1000,
            'tax': 100,
            'amount': 1100,
        }
    )

    tax_2 = Tax.from_dict(
        {
            'id': 2,
            'name': 'Big Mac',
            'tax_code': 1,
            'tax_code_type': 'Food & Beverage',
            'refundable': 'Yes',
            'price': 1000,
            'tax': 20,
            'amount': 1020,
        }
    )

    return [tax_1, tax_2]

def test_tax_get_all():
    price_subtotal = 1000 + 1000
    tax_subtotal = 100 + 20
    grand_total = price_subtotal + tax_subtotal

    repo = mock.Mock()
    repo.get_all.return_value = domain_tax()
    repo.get_price_subtotal.return_value = price_subtotal
    repo.get_tax_subtotal.return_value = tax_subtotal
    repo.get_grand_total.return_value = grand_total

    tax_get_all_usecase = ListTaxUsecase(repo=repo)
    total_page = 1

    response_object = tax_get_all_usecase.execute(True)
    serialize = ListTax(many=True).dump(domain_tax())
    expected_return = {
        'success': True,
        'code': Config.STATUS_CODES[Config.SUCCESS],
        'message': Config.SUCCESS.lower(),
        'data': serialize.data,
        'meta': {
            'priceSubtotal': price_subtotal,
            'taxSubtotal': tax_subtotal,
            'grandTotal': grand_total
        }
    }

    assert response_object.value == expected_return
