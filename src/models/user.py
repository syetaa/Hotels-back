from pydantic import BaseModel, ConfigDict


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class User(BaseModel):
    id: int
    username: str
    email: str
    name: str
    surname: str


class AddUser(User):
    password: str


class UserInDb(User):
    password: str
    model_config = ConfigDict(from_attributes=True)
