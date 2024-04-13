from sqlalchemy import select

from src.db import new_session, RoomOrm
from src.models.room import Room, RoomFilter, RoomId


class RoomRepository:
    @classmethod
    async def get_rooms(cls, data: RoomFilter) -> list[Room]:
        async with new_session() as session:
            query = select(RoomOrm).where(RoomOrm.capacity >= data.capacity).where(RoomOrm.price <= data.price).where(RoomOrm.city == data.city)
            result = await session.execute(query)
            room_models = result.scalars().all()
            rooms = [Room.model_validate(room_model) for room_model in room_models]
            return rooms

    @classmethod
    async def get_room(cls, data: RoomId) -> Room | bool:
        async with new_session() as session:
            query = select(RoomOrm).where(RoomOrm.id == data.id)
            result = await session.execute(query)
            room_model = result.scalars().first()
            print(room_model)
            if room_model is None:
                return False
            room = Room.model_validate(room_model)
            return room
