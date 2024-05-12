from pydantic import BaseModel, ConfigDict


class RoomFilter(BaseModel):
    city: str
    min_price: int
    max_price: int
    capacity: int


class AddRoom(BaseModel):
    city: str
    hotel: str
    price: int
    capacity: int


class RoomId(BaseModel):
    id: int


class Room(RoomId, AddRoom):
    model_config = ConfigDict(from_attributes=True)


class GetRoom(Room):
    liked: bool
    ordered: bool
    model_config = ConfigDict(from_attributes=True)

