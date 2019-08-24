from marshmallow import Schema, fields

class ListTax(Schema):
    # id=fields.Str(attribute="id")
    name=fields.Str(attribute="name")
    taxCode=fields.Str(attribute="tax_code")
    type=fields.Str(attribute="tax_code_type")
    price=fields.Str(attribute="price")


