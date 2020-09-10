from pytest_bdd import when, then, scenarios
from starlette.testclient import TestClient

CONVERTERS = {
    'email': str,
    'password': str,
    'status_code': int,
    'message': str,
}
scenarios('../features/login_outline.feature', example_converters=CONVERTERS)


@when('Required data for login are set "<email>","<password>"')
def data_for_login(email, password):
    global login_data
    global user_password
    user_password = password
    login_data = {
        "username": email,
        "password": password
    }


@then("POST request is made to endpoint with data provided")
def step_impl(login_api_url, client: TestClient):
    global request_login
    request_login = client.post(
        login_api_url, data=login_data
    )


@then('Response message should be "<message>" and status code "<status_code>"')
def status_code_response(message, status_code):
    res_js = request_login.json()
    err_msg = message
    assert request_login.status_code == status_code
    if status_code == 400:
        assert res_js["detail"] == err_msg
    elif status_code == 422:
        assert res_js['detail'][0]['msg'] == err_msg
