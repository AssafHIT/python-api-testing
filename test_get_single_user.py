import requests
import pytest

@pytest.mark.parametrize("id", [1]) # Brackets for Passing id as Int
def test_get_user_by_id(id):
    response = requests.get(f"http://reqres.in/api/users/{id}")
    json_response = response.json()
    assert json_response["data"]["id"] == id
    
def test_get_single_user_status_code_and_ok():
    response = requests.get("http://reqres.in/api/users/2")
    assert response.status_code == 200 # OK
    assert response.ok == True
    
def test_get_single_user_existing_keys():
    response = requests.get("http://reqres.in/api/users/2")
    json_response = response.json()
    assert 'data' in json_response.keys()


