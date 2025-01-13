from pydantic import BaseModel
class AuthSchema(BaseModel):
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "test_user",
                    "password": "secure_password"
                }
            ]
        }
    }