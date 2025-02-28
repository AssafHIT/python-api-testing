import requests
import pytest

@pytest.mark.parametrize("email, password", [("eve.holt@reqres.in", "pistol")])
def test_register_user_happy_flow(email, password):
    register_user_data = {
                            "email": email,
                            "password": password
                         }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
    assert 'token' in response.json().keys(), "Expected 'token' key in the response"
    assert 'id' in response.json().keys(), "Expected 'id' key in the response"

@pytest.mark.parametrize("email", [("eve.holt@reqres.in")])
def test_register_user_missing_password(email):
    register_user_data = {
                            "email": email
                         }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert not response.ok, f"Expected response to be False, but got {response.ok}"
    
    assert response.json()["error"] == "Missing password", "Expected error message 'Missing password', but got a different error"
  
@pytest.mark.parametrize("password", [("pistol")])  
def test_register_user_missing_email(password):
    register_user_data = {
                            "password": password
                         }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert not response.ok, f"Expected response to be False, but got {response.ok}"
    assert response.json()["error"] == "Missing email or username", "Expected error message 'Missing email or username', but got a different error"