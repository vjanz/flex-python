from pytest_bdd import when, then, scenario
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from app import crud
from app.schemas import UserCreate
from tests.util_functions.utils import gen_random_email, random_str_to_lowercase


@scenario("../features/register.feature", "User Registration with correct credentials")
def test_register_with_right_credentials():
    pass


@scenario("../features/register.feature", "User Registration with wrong credentials")
def test_register_with_wrong_credentials():
    pass


@scenario("../features/register.feature", "User exist while trying to register")
def test_register_with_existing_user():
    pass


##############################       Scenario 1       ###################################################

@when("Required data for registration are set")
def required_data() -> None:
    global registration_data
    registration_data = {
        'email': 'valon@test.com',
        'password': 'P@SSW0RD',
        'full_name': 'Valon Januzaj'
    }


@when('POST request is made to endpoint with specified data')
def post_to_endpoint(api_endpoint, client: TestClient) -> None:
    # making the request
    global request
    request = client.post(
        api_endpoint, json=registration_data
    )


@then("Response status code should be 200")
def response_code() -> None:
    response = request
    response_json = request.json()
    assert response.status_code == 200


@then("The response body should contain id, email and hashed_password")
def request_body() -> None:
    response_to_json = request.json()
    assert response_to_json
    assert "id" in response_to_json
    assert "email" in response_to_json


##############################       Scenario 2       ###################################################


@when("Data for registration don't fit the requirement fields")
def bad_data() -> None:
    global data
    data = {
        'email': 'valon@test.com',
        'password': '12',  # Pass min length is 6
        'full_name': 'Valon Januzaj'
    }


@when("POST request is made to endpoint with bad body request")
def request_with_bad_data(api_endpoint, client: TestClient):
    global r
    r = client.post(
        api_endpoint, json=data
    )
    return r


@then("Response status code should be 422")
def response_status_code() -> None:
    res_json: dict = r.json()
    assert r.status_code == 422
    assert res_json
    assert res_json['detail'][0]['msg'] == "ensure this value has at least 3 characters"


##############################       Scenario 3       ###################################################

@when("Data for a user that is already registered is set")
def set_data(db: Session) -> None:
    email = gen_random_email()
    password = random_str_to_lowercase()
    user_create = UserCreate(email=email, password=password)

    user = crud.user.create(db, obj_in=user_create)
    global user_data
    user_data = {
        "email": email,
        "password": password
    }


@when("POST Request is made to endpoint with those data")
def post_exist_data(api_endpoint, client: TestClient) -> None:
    global register_response
    register_response = client.post(
        api_endpoint, json=user_data
    )


@then("Response status code should be 400")
def step_status_code() -> None:
    assert register_response.status_code == 400
