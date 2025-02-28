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
    assert response.status_code == 200 # OK
    assert response.ok
    assert 'token' in response.json().keys()
    assert 'id' in response.json().keys()

@pytest.mark.parametrize("email", [("eve.holt@reqres.in")])
def test_register_user_missing_password(email):
    register_user_data = {
                            "email": email
                         }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    assert response.status_code == 400 # Bad Request
    assert response.ok == False 
    
    assert response.json()["error"] == "Missing password"
  
@pytest.mark.parametrize("password", [("pistol")])  
def test_register_user_missing_email(password):
    register_user_data = {
                            "password": password
                         }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    assert response.status_code == 400 # Bad Request
    assert response.ok == False 
    assert response.json()["error"] == "Missing email or username"