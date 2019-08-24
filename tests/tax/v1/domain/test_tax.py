import pytest

from src.tax.v1.domain.tax import Tax

def test_init():
    tax = Tax(
        name='Big Mac',
        tax_code=1,
        tax_code_type='Food & Beverage',
        refundable='Yes',
        price=1000,
        tax=100,
        amount=1100,
    )

    assert tax.name == 'Big Mac'
    assert tax.tax_code == 1
    assert tax.tax_code_type == 'Food & Beverage'
    assert tax.refundable == 'Yes'
    assert tax.price == 1000
    assert tax.tax == 100
    assert tax.amount == 1100

def test_from_dict():
    tax = Tax.from_dict({
        'name': 'Big Mac',
        'tax_code': 1,
        'tax_code_type': 'Food & Beverage',
        'refundable': 'Yes',
        'price':1000,
        'tax':100,
        'amount':1100,
    })

    assert tax.name == 'Big Mac'
    assert tax.tax_code == 1
    assert tax.tax_code_type == 'Food & Beverage'
    assert tax.refundable == 'Yes'
    assert tax.price == 1000
    assert tax.tax == 100
