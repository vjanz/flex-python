import os

from pytest_bdd import scenario, given, when, then
from starlette.testclient import TestClient

from app import crud
from app.schemas import UserCreate
from tests.util_functions.utils import gen_random_email, random_str_to_lowercase


@scenario('../features/login.feature', 'Login with correct credentials')
def test_login():
    pass


@scenario('../features/login.feature', 'Login and get access token')
def test_login():
    pass


BDD_BASE_URL = os.getenv("BDD_BASE_URL")


@given("User is registered in system")
def registered_user(db):
    email = gen_random_email()
    password = random_str_to_lowercase()
    user_create = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_create)

    return {"email": email, "password": password}


@when("Required data for login are set")
def set_data(registered_user):
    global data_login
    data_login = {
        'username': registered_user["email"],
        'password': registered_user["password"]
    }


@when("POST Request is made to login endpoint with specified data")
def step_impl(login_api_url, client: TestClient):
    global r
    r = client.post(
        login_api_url, data=data_login
    )


@then('Response status code should be 200')
def res_status():
    assert r.status_code == 200


@then("Response should contain access_token")
def access_token():
    res_json = r.json()
    assert "access_token" in res_json
    assert res_json["token_type"] == "bearer"
