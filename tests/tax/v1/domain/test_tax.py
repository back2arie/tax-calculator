import pytest

from src.tax.v1.domain.tax import Tax

def test_init():
    tax = Tax(
        name='Big Mac',
        tax_code=1,
        tax_code_type='Food & Beverage',
        price=1000,
    )

    assert tax.name == 'Big Mac'
    assert tax.tax_code == 1
    assert tax.tax_code_type == 'Food & Beverage'
    assert tax.price == 1000

def test_from_dict():
    tax = Tax.from_dict({
        'name': 'Big Mac',
        'tax_code': 1,
        'tax_code_type': 'Food & Beverage',
        'price':1000,
    })

    assert tax.name == 'Big Mac'
    assert tax.tax_code == 1
    assert tax.tax_code_type == 'Food & Beverage'
    assert tax.price == 1000
