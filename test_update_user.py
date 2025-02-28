import requests
import pytest
from datetime import datetime, timezone

def verify_updated_at(response, current_time):
    updated_at = datetime.fromisoformat(response.json().get("updatedAt").replace("Z", "+00:00"))
    assert updated_at is not None
    assert abs((current_time - updated_at).total_seconds()) < 10  # Allow for a 10-second difference

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

    assert response.status_code == 200 # OK
    assert response.ok
    assert response.json().get("name") == name
    assert response.json().get("job") == job
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
    
    assert response.status_code == 200 # OK
    assert response.ok
    assert response.json().get("job") == job
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
    
    assert response.status_code == 200 # OK
    assert response.ok
    assert response.json().get("name") == name
    verify_updated_at(response, current_time) 