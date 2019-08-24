import pytest
import json

from schemas.json.loader import JSONSchemaLoader
from src.tax.v1.domain.tax import Tax
from src.tax.v1.repository.tax_repository_orator import TaxRepositoryOrator
from src.tax.v1.usecase.request_object import ListTaxRequestObject
from src.app import connect_db
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

@pytest.fixture(scope="module")
def db_con():
    db = connect_db()
    yield db
    db.disconnect()

def test_get_all(db_con):

    result = TaxRepositoryOrator(db=db_con).get_all(None)
    assert isinstance(result, list)
    assert isinstance(result[0], Tax)

def test_create(db_con):
    tax = Tax.from_dict({
        "id": None,
        "name": "Big Mac",
        "tax_code": 1,
        "tax_code_type": "Food & Beverage",
        "price": 1000,
    })
    res = TaxRepositoryOrator(db=db_con).create(tax)
    assert bool(res)
