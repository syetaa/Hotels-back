from typing import Annotated

from fastapi import APIRouter, Depends

from src.models.order import AddOrder, Order, OrderId
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
) -> list[Order]:
    orders = await OrderRepository.get_orders(user)
    return orders


@orders_router.post('/')
async def add_order(
    order: Annotated[AddOrder, Depends()]
) -> OrderId:
    return await OrderRepository.add_order(order)
