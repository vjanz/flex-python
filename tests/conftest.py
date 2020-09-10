import logging
import os
import time
from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from starlette.testclient import TestClient

from app.db.session import SessionLocal
from app.main import app
from initial_db import main
from .factories import UserCreateFactory


# Get postgres dsn
def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "app")
    return f"postgresql://{user}:{password}@{server}/{db}"


logger = logging.getLogger(__name__)
pg_dsn = get_url()


@pytest.yield_fixture(scope="session", autouse=True)
def db():
    from app.db.base import Base
    engine = create_engine(
        pg_dsn,
    )
    if database_exists(pg_dsn):
        drop_database(pg_dsn)
    create_database(pg_dsn)
    logger.info(f"creating {pg_dsn}")
    Base.metadata.create_all(engine)
    main()
    yield SessionLocal()

@pytest.yield_fixture(scope="function")
def session(db):
    """
    Creates a new database session with (with working transaction)
    for test duration.
    """
    db.begin_nested()
    yield db
    db.rollback()


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


# Factories fixtures
@pytest.fixture
def user_create():
    return UserCreateFactory()
