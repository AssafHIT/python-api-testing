import requests
import pytest

@pytest.mark.parametrize("id", [2]) # Brackets for Passing id as Int
def test_delete_user_by_id(id):
    response = requests.delete(f"http://reqres.in//api/users/{id}")
    assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"