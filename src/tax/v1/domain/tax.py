class Tax():
    """
    Domain layer for Tax Object.

    Attributes:
        name: Tax object name.
        tax_code: Tax code.
        tax_code_type: Tax code name.
        refundable: A boolean indicating if tax object refundable or not.
        price: A decimal for tax object price.
        tax: A decimal for tax object tax.
        amount: A decimal for tax object amount (price plus tax).
    """

    def __init__(self, name, tax_code, tax_code_type, refundable, price, tax, amount):
        """Construct Tax Object."""

        self.name = name
        self.tax_code = tax_code
        self.tax_code_type = tax_code_type
        self.refundable = refundable
        self.price = price
        self.tax = tax
        self.amount = amount

    @classmethod
    def from_dict(cls, adict):
        """Construct Tax Object from dict of array-like or dicts."""

        tax = Tax(
            name=adict['name'],
            tax_code=adict['tax_code'],
            tax_code_type=adict['tax_code_type'],
            refundable=adict['refundable'],
            price=adict['price'],
            tax=adict['tax'],
            amount=adict['amount'],
        )

        return tax
