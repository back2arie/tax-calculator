from jsonschema import Draft4Validator, exceptions
from src.shared.validator.ivalidator import Validator

class JSONSchemaValidator(Validator):
    def __init__(self):
        self.__errors = []
        self.__data = []

        super(JSONSchemaValidator, self).__init__()

    def is_valid(self, adict, schema):
        def trace_error_value(error):
            if len(error.path) != 0: return (error.path[-1], error.message)
            return ('keyError', error.message)

        self.__errors = dict(
            trace_error_value(e) for e in sorted(
                Draft4Validator(schema).iter_errors(adict), key=exceptions.by_relevance()
            )
        )

        self.__data = adict if len(self.__errors) == 0 else []

        return len(self.__errors) == 0

    def get_errors(self):
        return self.__errors

    def get_valid_data(self):
        return self.__data
