import requests
import pytest

@pytest.mark.parametrize("page", [1, 2, 3])
def test_get_all_users_status_code_and_ok(page):
    response = requests.get("http://reqres.in/api/users", params = {"page": str(page)})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
    
@pytest.mark.parametrize("page", [1, 2])
def test_get_all_users_existing_keys(page):
    response = requests.get("http://reqres.in/api/users", params = {"page": str(page)})
    json_response = response.json()
    assert 'total_pages' in json_response.keys(), "'total_pages' key is missing in the response"
