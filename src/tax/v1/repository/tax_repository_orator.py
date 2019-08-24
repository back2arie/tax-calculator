from src.shared.helper import calculate_tax, calculate_amount, is_refundable
from src.tax.v1.domain.tax import Tax
from src.tax.v1.repository.tax_repository import TaxRepository
from src.tax.v1.repository.tax_code_repository_config import TaxCodeRepositoryConfig

class TaxRepositoryOrator(TaxRepository):
    """
    Repository implementation for Tax Object using Orator ORM.

    Attributes:
        db: Database instance.
    """

    def __init__(self, db):
        """Construct Tax Object Repository."""

        self.db = db
        self.price_subtotal = 0
        self.tax_subtotal = 0

    def get_all(self, request_objects):
        """Performs get all operations."""

        query = self.db.table('tax')
        query = query.get()
        repo_tax_code = TaxCodeRepositoryConfig()

        result = []
        for row in query:
            tax_code = row['tax_code']
            price = row['price']
            tax = calculate_tax(price, tax_code)
            data = Tax.from_dict({
                'name': row['name'],
                'tax_code': tax_code,
                'tax_code_type': repo_tax_code.get_type_by_code(tax_code),
                'refundable': is_refundable(row['tax_code']),
                'price': price,
                'tax': tax,
                'amount': calculate_amount(price, tax)
            })
            self.price_subtotal += price
            self.tax_subtotal += tax
            result.append(data)

        return result

    def get_price_subtotal(self):
        """Performs get price subtotal operations."""

        return self.price_subtotal

    def get_tax_subtotal(self):
        """Performs get tax subtotal operations."""

        return self.tax_subtotal

    def get_grand_total(self):
        """Performs get grand total operations."""

        return self.price_subtotal + self.tax_subtotal

    def create(self, request_objects):
        """Performs create tax object operations."""

        return self.db.table('tax').insert({
            'name': request_objects.name,
            'tax_code': request_objects.tax_code,
            'price': request_objects.price,
        })
