from flask import Blueprint
from flask import current_app
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from .smoke import Smoke
from .films import FilmsListApi
from .actors import ActorListApi
from .aggregations import AggregationApi
from .auth import AuthRegister, AuthLogin
from .populate_db import PopulateDB, PopulateDBThreaded, PopulateDBThreadPoolExecutor


def api_setup():
    """
    Set up Api
    :return: api_bp
    """

    api_bp = Blueprint("api_v1", __name__)
    api = Api(api_bp)

    api.add_resource(Smoke, "/smoke", strict_slashes=False)

    api.add_resource(FilmsListApi, "/films", "/films/<uuid>", strict_slashes=False)
    api.add_resource(ActorListApi, "/actors", "/actors/<uuid>", strict_slashes=False)

    api.add_resource(AggregationApi, "/aggregations", strict_slashes=False)

    api.add_resource(AuthRegister, "/register", strict_slashes=False)
    api.add_resource(AuthLogin, "/login", strict_slashes=False)

    api.add_resource(PopulateDB, "/populate_db", strict_slashes=False)
    api.add_resource(PopulateDBThreaded, "/populate_db_threaded", strict_slashes=False)
    api.add_resource(PopulateDBThreadPoolExecutor, "/populate_db_executor", strict_slashes=False)

    return api_bp


def swagger_setup():
    """

    :return: swagger_bp
    """

    swagger_bp = get_swaggerui_blueprint(
        base_url=current_app.config.get("SWAGGER_BASE_URL", "/api/v1/swagger"),
        api_url=current_app.config.get("SWAGGER_API_URL", "/static/actorfilmswagger.json"),
        config={
            'app_name': current_app.config.get("SWAGGER_APP_NAME", "Flask Movie")
        }
    )

    return swagger_bp
