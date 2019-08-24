import pytest
import json

from schemas.json.loader import JSONSchemaLoader
from src.tax.v1.domain.tax import Tax
from src.tax.v1.repository.tax_repository_orator import TaxRepositoryOrator
from src.app import connect_db
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

@pytest.fixture(scope="module")
def db_con():
    db = connect_db()
    yield db
    db.disconnect()

def test_get_all(db_con):

    result = TaxRepositoryOrator(db=db_con).get_all(True)
    assert isinstance(result, list)
    assert isinstance(result[0], Tax)

def test_get_price_subtotal():

    result = TaxRepositoryOrator(db=db_con).get_price_subtotal()
    assert isinstance(result, int)

def test_get_tax_subtotal():

    result = TaxRepositoryOrator(db=db_con).get_tax_subtotal()
    assert isinstance(result, int)

def test_get_grand_total():

    result = TaxRepositoryOrator(db=db_con).get_grand_total()
    assert isinstance(result, int)

def test_create(db_con):
    tax = Tax.from_dict({
        "id": None,
        "name": "Big Mac",
        "tax_code": 1,
        "tax_code_type": "Food & Beverage",
        "refundable": "Yes",
        "price": 1000,
        "tax": 100,
        "amount": 1100,
    })
    res = TaxRepositoryOrator(db=db_con).create(tax)
    assert bool(res)
