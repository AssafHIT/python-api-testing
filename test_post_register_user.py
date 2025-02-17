import requests
from assertpy import assert_that

def test_register_user_happy_flow():
    register_user_data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
    
    response = requests.post(
        url = "http://reqres.in/api/register",
        json = register_user_data
        )
    
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.ok).is_true()
    
    
    