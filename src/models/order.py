from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AddOrder(BaseModel):
    user_id: int
    room_id: int
    start_date: datetime
    end_date: datetime


class OrderId(BaseModel):
    id: int


class Order(AddOrder, OrderId):
    model_config = ConfigDict(from_attributes=True)
