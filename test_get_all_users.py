import requests
from assertpy import assert_that

response = requests.get("http://reqres.in/api/users", params={"page": "2"})
print(response.json()['page'])


def test_get_all_users_status_code_and_ok():
    response = requests.get("http://reqres.in/api/users", params={"page": "2"})
    
    assert response.status_code == 200
    assert_that(response.status_code).is_equal_to(200)
    assert response.ok == True
    
def test_get_all_users_existing_keys():
    response = requests.get("http://reqres.in/api/users", params={"page": "2"})
    json_response = response.json()
    #assert "total_pages" in json_response.keys()
    assert_that(json_response).contains_key("data")