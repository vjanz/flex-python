import requests
from pytest_bdd import given, when, scenario


@scenario('../features/login_lumen.feature', 'Login and create category')
def test_login():
    pass


@given("API endpoint for user login in lumen")
def url():
    API_URL = "http://localhost:8000/login"
    return API_URL


@given("API to create category")
def url_category():
    category_url = "http://localhost:8000/categories"
    return category_url


@when("Data are set")
def step_impl():
    global data
    data = {
        "email": "admin@test.com",
        "password": "12345"
    }


@when("Post is made to endpoint")
def req(url, url_category):
    access_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsdW1lbi1qd3QiLCJzdWIiOjEsImlhdCI6MTU5MTIxMTUwOCwiZXhwIjoxNTkxMjE1MTA4fQ.zg1gNrueCPE52TIQgqJTaPx5U2rr51x3_UFppJgOD-U"
    data_for_category = {
        "name": "somecategory",
        "description": "somedescription"
    }

    request_new = requests.post(
        url_category, json=data_for_category, headers={"Authorization": access_token}
    )

    print(request_new.json())
