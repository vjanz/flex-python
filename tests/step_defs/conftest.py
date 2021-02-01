import os

from pytest_bdd import given

FIRST_SUPERUSER_EMAIL = os.getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")
FIRST_SUPERUSER_FULL_NAME = os.getenv("FIRST_SUPERUSER_FULL_NAME")
BDD_BASE_URL = os.getenv("BDD_BASE_URL")


@given("API endpoint for user registration")
def api_endpoint() -> str:
    REGISTER_URL = "http://localhost:8000/api/v1/users/open"
    return REGISTER_URL


@given("API endpoint for user login")
def login_api_url():
    LOGIN_API_ENDPOINT = f"{BDD_BASE_URL}/login/access-token"
    return LOGIN_API_ENDPOINT
