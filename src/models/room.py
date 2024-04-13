from pydantic import BaseModel, ConfigDict


class RoomFilter(BaseModel):
    city: str
    price: int
    capacity: int


class RoomId(BaseModel):
    id: int


class Room(RoomFilter, RoomId):
    hotel: str
    model_config = ConfigDict(from_attributes=True)
