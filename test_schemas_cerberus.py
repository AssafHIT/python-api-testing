import requests
from cerberus import Validator

def test_register_user_schema():
    schema = {
                "id": {"type": "number"},
                "token": {"type": "string"}
             }
    validator = Validator(schema, require_all=True)
    
    register_user_data = {
                            "email": "eve.holt@reqres.in",
                             "password": "pistol"
                         }
    response = requests.post(
        url = "https://reqres.in/api/register",
        json = register_user_data
    )
    if response.status_code == 200:
        is_valid = validator.validate(response.json())
        assert is_valid, f"Response schema validation failed. Errors: {validator.errors}"
        