import pytest
from sqlalchemy import create_engine

db_url = "postgresql://postgres:0510@localhost:5432/QA_135.2"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(db_url)
    yield engine
    engine.dispose()


@pytest.fixture()
def db_connection(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()

    yield connection

    transaction.rollback()
