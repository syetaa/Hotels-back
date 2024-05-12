from typing import Annotated

from fastapi import APIRouter, Depends

from src.models.order import GetOrder
from src.models.user import User
from src.repos.order import OrderRepository
from src.utils import get_current_user

orders_router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@orders_router.get('/')
async def get_orders(
    user: Annotated[User, Depends(get_current_user)]
) -> list[GetOrder]:
    orders = await OrderRepository.get_orders(user)
    return orders


@orders_router.post('/{room_id}')
async def add_order(
    user: Annotated[User, Depends(get_current_user)],
    room_id: int
) -> int:
    return await OrderRepository.add_order(user=user, room_id=room_id)


@orders_router.delete('/{room_id}')
async def delete_order(
    user: Annotated[User, Depends(get_current_user)],
    room_id: int
):
    await OrderRepository.delete_order(user=user, room_id=room_id)
