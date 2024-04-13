from sqlalchemy import select

from src.db import new_session, OrderOrm
from src.models.order import Order, AddOrder
from src.models.user import User


class OrderRepository:
    @classmethod
    async def add_order(cls, data: AddOrder) -> int:
        async with new_session() as session:
            order_dict = data.model_dump()
            order = OrderOrm(**order_dict)
            session.add(order)
            await session.flush()
            await session.commit()
            return order.id

    @classmethod
    async def get_orders(cls, user: User) -> list[Order]:
        async with new_session() as session:
            query = select(OrderOrm).where(OrderOrm.user_id == user.id)
            result = await session.execute(query)
            order_models = result.scalars().all()
            orders = [Order.model_validate(order_model) for order_model in order_models]
            return orders
