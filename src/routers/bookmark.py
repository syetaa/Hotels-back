from typing import Annotated

from fastapi import APIRouter, Depends

from src.models.bookmark import GetBookmark
from src.models.user import User
from src.repos.bookmark import BookmarkRepository
from src.utils import get_current_user

bookmarks_router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks"]
)


@bookmarks_router.get('/')
async def get_bookmarks(
    user: Annotated[User, Depends(get_current_user)]
) -> list[GetBookmark]:
    bookmarks = await BookmarkRepository.get_bookmarks(user)
    return bookmarks


@bookmarks_router.post('/{room_id}')
async def add_bookmark(
    user: Annotated[User, Depends(get_current_user)],
    room_id: int
) -> int:
    return await BookmarkRepository.add_bookmark(user=user, room_id=room_id)


@bookmarks_router.delete('/{room_id}')
async def delete_bookmark(
    user: Annotated[User, Depends(get_current_user)],
    room_id: int
):
    return await BookmarkRepository.delete_bookmark(user=user, room_id=room_id)

