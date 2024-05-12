from sqlalchemy import delete, select

from src.db import RoomOrm, new_session, BookmarkOrm
from src.models.bookmark import GetBookmark
from src.models.user import User


class BookmarkRepository:
    @classmethod
    async def add_bookmark(cls, room_id: int, user: User) -> int:
        async with new_session() as session:
            bookmark_dict = {'room_id': room_id, 'user_id': user.id}
            bookmark = BookmarkOrm(**bookmark_dict)
            session.add(bookmark)
            await session.flush()
            await session.commit()
            return bookmark.id

    @classmethod
    async def delete_bookmark(cls, room_id: int, user: User):
        async with new_session() as session:
            query = delete(BookmarkOrm).where(BookmarkOrm.user_id == user.id, BookmarkOrm.room_id == room_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_bookmarks(cls, user: User) -> list[GetBookmark]:
        async with new_session() as session:
            query = select(RoomOrm).join(BookmarkOrm, BookmarkOrm.room_id == RoomOrm.id).where(BookmarkOrm.user_id == user.id)
            result = await session.execute(query)
            room_models = result.scalars().all()
            bookmarks = [GetBookmark.model_validate(room_model) for room_model in room_models]
            return bookmarks
