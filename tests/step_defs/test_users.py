from pytest_bdd import given, when, then, scenario
from starlette.testclient import TestClient

from tests.step_defs.conftest import FIRST_SUPERUSER_EMAIL, FIRST_SUPERUSER_PASSWORD, BDD_BASE_URL


@scenario('../features/users.feature', 'Get the user that is logged in')
def test_login():
    pass


@given("User is logged in")
def user_logged_in(client: TestClient):
    email = FIRST_SUPERUSER_EMAIL
    password = FIRST_SUPERUSER_PASSWORD

    data = {
        'username': email,
        'password': password
    }

    r = client.post(
        f"{BDD_BASE_URL}/login/access-token", data=data
    )
    tokens = r.json()
    access_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    return headers


@given("API endpoint /api/v1/users/me")
def me_endpoint():
    ME_ENDPOINT = f"{BDD_BASE_URL}/login/me"
    return ME_ENDPOINT


@when("POST Request is made to the specified endpoint with access_token in request header")
def post_req(me_endpoint, user_logged_in, client: TestClient):
    global response
    response = client.post(
        me_endpoint, headers=user_logged_in
    )
    return response


@then("Response should contain email,full_name,and id of current logged user")
def contains_results():
    res_json = response.json()
    assert "email" in res_json
    assert "full_name" in res_json
    assert "id" in res_json
