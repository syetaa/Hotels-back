from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.models.room import AddRoom, GetRoom, RoomFilter, Room, RoomId
from src.models.user import User
from src.repos.room import RoomRepository
from src.utils import get_current_user

rooms_router = APIRouter(
    prefix="/rooms",
    tags=["rooms"]
)


@rooms_router.get('/')
async def get_rooms(
    room: Annotated[RoomFilter, Depends()]
) -> list[Room]:
    print(room)
    rooms = await RoomRepository.get_rooms(room)
    return rooms


@rooms_router.post('/')
async def add_room(
    room: Annotated[AddRoom, Depends()]
) -> RoomId:
    room_id = await RoomRepository.add_room(room)
    return {'id': room_id}


@rooms_router.get('/{room_id}')
async def get_room(
    user: Annotated[User, Depends(get_current_user)],
    room_id: int
) -> GetRoom:
    room = await RoomRepository.get_room(room_id)
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No room with such id",
        )
    return room

