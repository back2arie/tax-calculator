import pytest

from src.tax.v1.domain.tax_code import TaxCode

def test_init():
    tax_code = TaxCode(
        id=1,
        name='Food & Beverage',
    )

    assert tax_code.id == 1
    assert tax_code.name == 'Food & Beverage'

def test_from_dict():
    tax_code = TaxCode.from_dict({
        'id': 2,
        'name': 'Tobacco',
    })

    assert tax_code.id == 2
    assert tax_code.name == 'Tobacco'
