from typing import Annotated

from fastapi import APIRouter, Depends

from src.models.bookmark import Bookmark
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
) -> list[Bookmark]:
    bookmarks = await BookmarkRepository.get_bookmarks(user)
    return bookmarks


@bookmarks_router.post('/')
async def add_bookmark(
    user: Annotated[User, Depends(get_current_user)],
    bookmark: Annotated[Bookmark, Depends()]
) -> int:
    return await BookmarkRepository.add_bookmark(user=user, bookmark=bookmark)


@bookmarks_router.delete('/')
async def delete_bookmark(
    user: Annotated[User, Depends(get_current_user)],
    bookmark: Annotated[Bookmark, Depends()]
):
    return await BookmarkRepository.delete_bookmark(user=user, bookmark=bookmark)
