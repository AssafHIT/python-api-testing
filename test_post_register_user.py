import requests

def test_register_user_happy_flow():
    register_user_data = {
                            "email": "eve.holt@reqres.in",
                            "password": "pistol"
                         }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    assert response.status_code == 200
    assert response.ok == True 
    
    assert 'token' and 'id' in response.json().keys()