import pytest

from config import Config
from src import create_app, db
from tests.tests_files._populate_DB import populate_db


@pytest.fixture()
def app_dev():
    return create_app(config_class="config.DevelopmentConfig")


@pytest.fixture()
def app_mock():
    return create_app(config_class="config.TestingConfig")


@pytest.fixture(scope='class')
def app_memory():
    app = create_app(config_class="config.TestingConfig")
    with app.app_context():
        db.create_all()
        populate_db(app=app, db=db)
        yield app
        # db.session.remove()
        db.drop_all()


@pytest.fixture
def api_ver():
    return str(getattr(Config, "API_VERSION", "/api/v1"))


@pytest.fixture(scope='class')
def client():
    app = create_app(config_class="config.TestingConfig")
    client = app.test_client()
    with app.app_context():
        db.create_all()
        populate_db(app=app, db=db)
    yield client
    with app.app_context():
        # db.session.remove()
        db.drop_all()
