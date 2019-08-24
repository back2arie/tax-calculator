class TaxCode(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_dict(self, adict):
        tax_code = TaxCode(
            id=adict['id'],
            name=adict['name'],
        )

        return tax_code
