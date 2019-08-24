from marshmallow import Schema, fields

class ListTax(Schema):
    name = fields.Str(attribute="name")
    taxCode = fields.Integer(attribute="tax_code")
    type = fields.Str(attribute="tax_code_type")
    refundable = fields.Str(attribute="refundable")
    price = fields.Decimal(attribute="price")
    tax = fields.Decimal(attribute="tax")
    amount = fields.Decimal(attribute="amount")
