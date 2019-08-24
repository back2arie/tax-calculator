from src.shared import helper
from src.shared.request_object import ValidRequestObject, InvalidRequestObject
from schemas.json.loader import JSONSchemaLoader

class ListTaxRequestObject(ValidRequestObject):
    # def __init__(self):
    
    @classmethod
    def from_dict(cls, adict):
        
        return ListTaxRequestObject()

    def __nonzero__(self):
        return True

class CreateTaxRequestObject(ValidRequestObject):
    def __init__(self, name, tax_code, price):
        self.name     = name
        self.tax_code = tax_code
        self.price    = price

    @classmethod
    def from_dict(cls, adict, validator):

        schema = JSONSchemaLoader.get("tax_schema_create_params")
        messages = JSONSchemaLoader.get("tax_custom_error_messages")
        if not validator.is_valid(adict=adict, schema=schema):
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=validator.get_errors())
            return invalid_req

        data = validator.get_valid_data()

        return CreateTaxRequestObject(**{
            'name': data['name'],
            'tax_code': data['taxCode'],
            'price': data['price'],
        })
