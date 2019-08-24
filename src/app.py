import logging

from orator import DatabaseManager
from sanic import Sanic
from sanic_cors import CORS

from config.config import Config
from src.tax.v1.delivery.http_sanic import bp_tax

logger = logging.getLogger(__name__)


def config_log(app):
    # set log config from config
    logging.config.dictConfig(Config.LOGGING)


def connect_db():
    # postgres use pgsql
    config = {
        'postgres': {
            'driver': Config.DB_TYPE,
            'host': Config.DB_HOST,
            'port':Config.DB_PORT,
            'database': Config.DB_NAME,
            'user': Config.DB_USER,
            'password': Config.DB_PASS,
            'prefix': '',
            'log_queries': True,
        }
    }
    return DatabaseManager(config)

def create_app(config):
    app = Sanic(__name__)
    app.config.from_object(config)
    app.blueprint(bp_tax)
    CORS(app, automatic_options=True)
    
    return app
