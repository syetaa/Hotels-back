from sqlalchemy import select

from src.db import new_session, BookmarkOrm
from src.models.bookmark import Bookmark, AddBookmark
from src.models.user import User


class BookmarkRepository:
    @classmethod
    async def add_bookmark(cls, data: AddBookmark):
        async with new_session() as session:
            bookmark_dict = data.model_dump()
            bookmark = BookmarkOrm(**bookmark_dict)
            session.add(bookmark)
            await session.flush()
            await session.commit()
            return bookmark.id

    @classmethod
    async def get_bookmarks(cls, user: User) -> list[Bookmark]:
        async with new_session() as session:
            query = select(BookmarkOrm).where(BookmarkOrm.user_id == user.id)
            result = await session.execute(query)
            bookmark_models = result.scalars().all()
            bookmarks = [Bookmark.model_validate(bookmark_model) for bookmark_model in bookmark_models]
            return bookmarks
