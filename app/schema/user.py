from pydantic import BaseModel, validator


class UserCreateRequest(BaseModel):
    id: int
    username: str
    hashed_password: str
    disabled: bool
    role: str

    @validator('username')
    def validate_username(cls, username):
        # Add custom validation logic here
        if len(username) < 5:
            raise ValueError('Username must be at least 5 characters long')
        return username
