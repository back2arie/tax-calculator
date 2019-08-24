from src.shared import helper
from src.tax.v1.domain.tax import Tax
from src.tax.v1.repository.tax_repository import TaxRepository
from src.tax.v1.repository.tax_code_repository_config import TaxCodeRepositoryConfig

class TaxRepositoryOrator(TaxRepository):
    def __init__(self, db):
        self.db = db

    def get_all(self, request_objects):
        query = self.db.table('tax')
        query = query.get()
        repo = TaxCodeRepositoryConfig()

        result = []
        for row in query:
            data = Tax.from_dict({
                # 'id': row['id'],
                'name': row['name'],
                'tax_code': row['tax_code'],
                'tax_code_type': repo.get_type_by_code(row['tax_code']),
                'price': row['price'],
            })
            result.append(data)

        return result
    
    def get_total(self, request_objects):
        query = self.db.table('tax')
    
        return query.count()
    
    def create(self, request_objects):
        
        return self.db.table('tax').insert({
            'name': request_objects.name,
            'tax_code': request_objects.tax_code,
            'price': request_objects.price,
        })

