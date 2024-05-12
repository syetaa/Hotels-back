from pydantic import BaseModel, ConfigDict

from src.models.room import Room


class Order(BaseModel):
    id: int
    user_id: int
    room_id: int
    model_config = ConfigDict(from_attributes=True)


class GetOrder(Room):
    model_config = ConfigDict(from_attributes=True)
