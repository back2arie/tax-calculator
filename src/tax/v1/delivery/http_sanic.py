from sanic import Blueprint
from sanic.response import json
from config.config import Config
from src.tax.v1.repository.tax_repository_orator import TaxRepositoryOrator
from src.shared.request.request_sanic import RequestSanicDict
from src.tax.v1.usecase.tax_use_cases import ListTaxUsecase, CreateTaxUsecase
from src.tax.v1.usecase.request_object import ListTaxRequestObject, CreateTaxRequestObject
from src.shared.validator.validator_jsonschema import JSONSchemaValidator

bp_tax = Blueprint('Tax V1', url_prefix='v1/tax')

@bp_tax.route('/', methods=['GET', 'POST'])
async def index(request):
    obj_dict = RequestSanicDict(request).parse_all_to_dict()
    validator = JSONSchemaValidator()
    repo  = TaxRepositoryOrator(db=request.app.db)
    request_dict = RequestSanicDict(request)

    if request.method == 'POST':
        
        adict = request_dict.parse_all_to_dict()
        request_object = CreateTaxRequestObject.from_dict(adict=adict, validator=validator)

        use_case = CreateTaxUsecase(repo=repo)    
    else:

        adict = request_dict.query_to_dict()
        adict = validator.get_default_param(adict)

        request_object = ListTaxRequestObject.from_dict(adict=adict)
        use_case = ListTaxUsecase(repo)

    response = use_case.execute(request_object=request_object)

    return json(response.value, status=Config.STATUS_CODES[response.type])
