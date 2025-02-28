import requests
import pytest

@pytest.mark.parametrize("name, job", [
    ("Assaf Yehezkel", "Automation Developer"),
    ("Jane Smith", "Backend Developer")
])
def test_create_user_happy_flow(name, job):
    created_user_data = {
                            "name": name,
                            "job": job
                         }
    response = requests.post(
        url = "https://reqres.in/api/users",
        json = created_user_data
    )
    assert response.status_code == 201, f"Expected status code 200, but got {response.status_code}"
    assert response.ok, f"Expected response to be OK, but got status code {response.status_code}"
    assert response.json().get("name") == name, f"Expected name to be '{name}', but got {response.json().get('name')}"
    assert response.json().get("job") == job, f"Expected job to be '{job}', but got {response.json().get('job')}"
    assert "id" in response.json().keys(), "Expected 'id' key in the response, but it was missing"
    assert "createdAt" in response.json().keys(), "Expected 'createdAt' key in the response, but it was missing"