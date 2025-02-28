import requests
import pytest

@pytest.mark.parametrize("page", [1, 2, 3])
def test_get_all_users_status_code_and_ok(page):
    response = requests.get("http://reqres.in/api/users", params = {"page": str(page)})
    assert response.status_code == 200 # OK
    assert response.ok == True
    
@pytest.mark.parametrize("page", [1, 2])
def test_get_all_users_existing_keys(page):
    response = requests.get("http://reqres.in/api/users", params = {"page": str(page)})
    json_response = response.json()
    assert 'total_pages' in json_response.keys()
