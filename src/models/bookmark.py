from pydantic import BaseModel, ConfigDict

from src.models.room import Room


class Bookmark(BaseModel):
    id: int
    user_id: int
    room_id: int
    model_config = ConfigDict(from_attributes=True)


class GetBookmark(Room):
    model_config = ConfigDict(from_attributes=True)
