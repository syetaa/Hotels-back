from sqlalchemy import select

from src.db import new_session, UserOrm
from src.models.user import AddUser, UserInDb


class UserRepository:
    @classmethod
    async def add_user(cls, data: AddUser) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()
            user = UserOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_user(cls, username: str) -> UserInDb | bool:
        async with new_session() as session:
            query = select(UserOrm).where(UserOrm.username == username)
            result = await session.execute(query)
            user_model = result.scalars().first()
            if user_model is None:
                return False
            user = UserInDb.model_validate(user_model)
            return user
