class Tax(object):
    def __init__(self, name, tax_code, tax_code_type, price):
        # self.id             = id
        self.name           = name
        self.tax_code       = tax_code
        self.tax_code_type  = tax_code_type
        self.price          = price

    @classmethod
    def from_dict(self, adict):
        tax = Tax(
            # id=adict['id'],
            name=adict['name'],
            tax_code=adict['tax_code'],
            tax_code_type=adict['tax_code_type'],
            price=adict['price'],
        )

        return tax
