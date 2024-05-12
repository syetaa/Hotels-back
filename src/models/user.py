from pydantic import BaseModel, ConfigDict


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class User(BaseModel):
    username: str
    email: str
    name: str
    surname: str


class UserId(BaseModel):
    id: int


class UserInfo(User, UserId):
    ...


class AddUser(User):
    password: str


class UserInDb(UserId, AddUser):
    model_config = ConfigDict(from_attributes=True)
