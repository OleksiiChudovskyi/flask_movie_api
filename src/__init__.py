import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=None):
    """
    Build and configure the Flask application.

    This function initializes the app instance, applies the given configuration,
    and registers all necessary components.

    :param config_class: Configuration class to apply
    :return: Configured Flask application instance
    """

    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", "development")
    if config_class is None:
        if env == "development":
            config_class = "config.DevelopmentConfig"
        elif env == "testing":
            config_class = "config.TestingConfig"
        else:
            config_class = "config.ProductionConfig"
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from src import models
        from src.resources import api_setup, swagger_setup

        app.register_blueprint(
            blueprint=api_setup(),
            url_prefix=app.config.get("API_VERSION", "/api/v1")
        )
        app.register_blueprint(
            blueprint=swagger_setup(),
            url_prefix=app.config.get("SWAGGER_BASE_URL", "/api/v1/swagger")
        )

    return app
