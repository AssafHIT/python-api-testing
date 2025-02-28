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
    assert response.status_code == 201 # Created
    assert response.ok is True 
    assert response.json().get("name") == name
    assert response.json().get("job") == job
    assert "id" in response.json().keys()
    assert "createdAt" in response.json().keys()