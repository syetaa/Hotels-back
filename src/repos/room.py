from sqlalchemy import select

from src.db import BookmarkOrm, new_session, OrderOrm, RoomOrm
from src.models.bookmark import Bookmark
from src.models.order import Order
from src.models.room import AddRoom, GetRoom, Room, RoomFilter
from src.models.user import User


class RoomRepository:
    @classmethod
    async def add_room(cls, data: AddRoom) -> int:
        async with new_session() as session:
            room_dict = data.model_dump()
            room = RoomOrm(**room_dict)
            session.add(room)
            await session.flush()
            await session.commit()
            return room.id

    @classmethod
    async def get_room(cls, room_id: int, user: User) -> GetRoom | bool:
        async with new_session() as session:
            query = select(RoomOrm, BookmarkOrm, OrderOrm).outerjoin(BookmarkOrm, BookmarkOrm.room_id == RoomOrm.id).outerjoin(OrderOrm, OrderOrm.room_id == RoomOrm.id).where(RoomOrm.id == room_id)
            result = await session.execute(query)
            room_model, bookmark_model, order_model = result.first()
            if room_model is None:
                return False
            room = Room.model_validate(room_model).model_dump()
            if bookmark_model is None:
                room['liked'] = False
            else:
                bookmark = Bookmark.model_validate(bookmark_model).model_dump()
                room['liked'] = True if bookmark['user_id'] == user.id else False
            if order_model is None:
                room['ordered'] = False
            else:
                order = Order.model_validate(order_model).model_dump()
                room['ordered'] = True if order['user_id'] == user.id else False
            return room

    @classmethod
    async def get_rooms(cls, data: RoomFilter) -> list[Room]:
        async with new_session() as session:
            query = select(RoomOrm).where(RoomOrm.capacity >= data.capacity, RoomOrm.price >= data.min_price, RoomOrm.price <= data.max_price, RoomOrm.city == data.city)
            result = await session.execute(query)
            room_models = result.scalars().all()
            rooms = [Room.model_validate(room_model) for room_model in room_models]
            return rooms
