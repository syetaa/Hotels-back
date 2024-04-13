from typing import Annotated

from fastapi import APIRouter, Depends

from src.models.bookmark import AddBookmark, Bookmark, BookmarkId
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
    bookmark: Annotated[AddBookmark, Depends()]
) -> BookmarkId:
    return await BookmarkRepository.add_bookmark(bookmark)
