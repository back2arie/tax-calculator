class TaxCode():
    """
    Domain layer for Tax Code.

    Attributes:
        id: Tax code id.
        name: Tax code name.
    """

    def __init__(self, id, name):
        """Construct Tax Code."""

        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, adict):
        """Construct Tax Code from dict of array-like or dicts."""

        tax_code = TaxCode(
            id=adict['id'],
            name=adict['name'],
        )

        return tax_code
