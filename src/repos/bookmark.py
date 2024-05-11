from sqlalchemy import delete, select

from src.db import RoomOrm, new_session, BookmarkOrm
from src.models.bookmark import Bookmark, AddBookmark
from src.models.user import User, UserInDb


class BookmarkRepository:
    @classmethod
    async def add_bookmark(cls, bookmark: Bookmark, user: UserInDb) -> int:
        async with new_session() as session:
            bookmark_dict = bookmark.model_dump()
            user_id = user.id
            bookmark_dict['user_id'] = user_id
            bookmark = BookmarkOrm(**bookmark_dict)
            session.add(bookmark)
            await session.flush()
            await session.commit()
            return bookmark.id

    @classmethod
    async def delete_bookmark(cls, bookmark: Bookmark, user: UserInDb):
        async with new_session() as session:
            user_id = user.id
            query = delete(BookmarkOrm).where(BookmarkOrm.user_id == user_id, BookmarkOrm.room_id == bookmark.room_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_bookmarks(cls, user: User) -> list[Bookmark]:
        async with new_session() as session:
            query = select(RoomOrm).join(BookmarkOrm, BookmarkOrm.room_id == RoomOrm.id).where(BookmarkOrm.user_id == user.id)
            result = await session.execute(query)
            room_models = result.scalars().all()
            print(room_models)
            bookmarks = [Bookmark.model_validate(room_model) for room_model in room_models]
            return bookmarks
