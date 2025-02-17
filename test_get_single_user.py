import requests
from assertpy import assert_that


def test_get_user_status_code_and_ok():
    response = requests.get("http://reqres.in/api/users/")
    
    assert response.status_code == 200
    assert_that(response.status_code).is_equal_to(200)
    assert response.ok == True
    
def test_get_user_id():
    id = 1
    response = requests.get(f"http://reqres.in/api/users/{id}")
    json_response = response.json()
    
    assert json_response["data"]["id"] == id 
    