import requests
import pytest
from datetime import datetime, timezone

def verify_updated_at(response, current_time):
    updated_at = datetime.fromisoformat(response.json().get("updatedAt").replace("Z", "+00:00"))
    assert updated_at is not None, "updatedAt is None in the response"
    time_diff = abs((current_time - updated_at).total_seconds())
    assert abs((current_time - updated_at).total_seconds()) < 10, f"Time difference between current time and updatedAt is too large: {time_diff} seconds"

@pytest.mark.parametrize("name, job, id",[("Morpheus", "HR", [2])])
def test_update_user_with_put(name, job, id):
    updated_user_data = {
                            "name": name,
                            "job": job
                         }
    response = requests.put(
        url = f"https://reqres.in/api/users/{id}",
        json = updated_user_data
    )
    
    current_time = datetime.now(timezone.utc)

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.ok, f"Expected OK response, but got status code {response.status_code}"
    assert response.json().get("name") == name, f"Expected name '{name}', but got {response.json().get('name')}"
    assert response.json().get("job") == job, f"Expected job '{job}', but got {response.json().get('job')}"
    verify_updated_at(response, current_time)
    
@pytest.mark.parametrize("job, id",[("Software Development", [2])])
def test_update_user_job_with_patch(job, id):
    updated_user_data = {
                            "job": job
                         }
    response = requests.patch(
        url = f"https://reqres.in/api/users/{id}",
        json = updated_user_data
    )
    current_time = datetime.now(timezone.utc)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.ok, f"Expected OK response, but got status code {response.status_code}"
    assert response.json().get("job") == job, f"Expected job '{job}', but got {response.json().get('job')}"
    verify_updated_at(response, current_time) 

@pytest.mark.parametrize("name, id",[("Dave Morpheus", [2])])
def test_update_user_name_with_patch(name, id):
    updated_user_data = {
                            "name": name
                         }
    response = requests.patch(
        url = f"https://reqres.in/api/users/{id}",
        json = updated_user_data
    )
    current_time = datetime.now(timezone.utc)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.ok, f"Expected OK response, but got status code {response.status_code}"
    assert response.json().get("name") == name, f"Expected name '{name}', but got {response.json().get('name')}"
    verify_updated_at(response, current_time) 