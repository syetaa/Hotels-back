from sqlalchemy import delete, select

from src.db import new_session, OrderOrm, RoomOrm
from src.models.order import GetOrder
from src.models.user import User


class OrderRepository:
    @classmethod
    async def add_order(cls, user: User, room_id: int) -> int:
        async with new_session() as session:
            order_dict = {'room_id': room_id, 'user_id': user.id}
            order = OrderOrm(**order_dict)
            session.add(order)
            await session.flush()
            await session.commit()
            return order.id

    @classmethod
    async def delete_order(cls, room_id: int, user: User):
        async with new_session() as session:
            query = delete(OrderOrm).where(OrderOrm.user_id == user.id, OrderOrm.room_id == room_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_orders(cls, user: User) -> list[GetOrder]:
        async with new_session() as session:
            query = select(RoomOrm).join(OrderOrm, OrderOrm.room_id == RoomOrm.id).where(OrderOrm.user_id == user.id)
            result = await session.execute(query)
            order_models = result.scalars().all()
            orders = [GetOrder.model_validate(order_model) for order_model in order_models]
            return orders
