import os
import pathlib


def read_secret(secret_name: str):
    """Read a secret into docker container"""
    try:
        with open(file=f"/run/secrets/{secret_name}") as f:
            return f.read().strip()
    except:
        return None


class Config:
    DEBUG = False
    TESTING = False
    HOST = "127.0.0.1"
    PORT = 8001

    BASE_DIR = pathlib.Path(__file__).parent

    SECRET_KEY = read_secret("flask_secret_key") or os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASE_DIR / 'data' / 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_VERSION = "/api/v1"

    SWAGGER_BASE_URL = str(API_VERSION + "/swagger")
    SWAGGER_API_URL = "/static/actorfilmswagger.json"
    SWAGGER_APP_NAME = "Flask Movie"


class DevelopmentConfig(Config):
    DEBUG = True
    HOST = "0.0.0.0"


class ProductionConfig(Config):
    POSTGRES_PASSWORD = read_secret("pg_password") or os.getenv("POSTGRES_PASSWORD")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{POSTGRES_PASSWORD}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
