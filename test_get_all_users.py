import requests

def test_get_all_users_status_code_and_ok():
    response = requests.get("http://reqres.in/api/users", params = {"page": "1"})
    assert response.status_code == 200 # OK
    assert response.ok == True
    
def test_get_all_users_existing_keys():
    response = requests.get("http://reqres.in/api/users", params = {"page": "1"})
    json_response = response.json()
    assert 'total_pages' in json_response.keys()
