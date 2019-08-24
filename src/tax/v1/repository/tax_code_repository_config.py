from config.config import Config
from src.tax.v1.repository.tax_code_repository import TaxCodeRepository

class TaxCodeRepositoryConfig(TaxCodeRepository):
    """Repository implementation for Tax Code using static config."""

    def __init__(self):
        """Construct Tax Code Repository."""

        self.__name = Config.TAX_CODE
        super(TaxCodeRepositoryConfig, self).__init__()

    def get_type_by_code(self, code):
        """
        Performs get tax code name by code operations.

        Attributes:
            code: Tax code id
        """

        tax_code_list = Config.serialize(self.__name)
        tax_code_row = next(filter(lambda row: row['id'] == code, tax_code_list), None)
        tax_code_type = tax_code_row['name'] if tax_code_row else None
        return tax_code_type
