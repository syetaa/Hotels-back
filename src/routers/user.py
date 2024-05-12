from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.consts import ACCESS_TOKEN_EXPIRE_MINUTES
from src.models.user import AddUser, Token, User, UserId, UserInfo
from src.repos.user import UserRepository
from src.utils import authenticate_user, create_access_token, get_current_user, get_password_hash

users_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@users_router.post('/token')
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await authenticate_user(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@users_router.get('/')
async def get_user_info(
    user: Annotated[User, Depends(get_current_user)],
) -> UserInfo:
    return user


@users_router.post('/')
async def add_user(
    user: Annotated[AddUser, Depends()],
) -> UserId:
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    user_id = await UserRepository.add_user(user)
    return {'id': user_id}
