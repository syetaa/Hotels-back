from pydantic import BaseModel, ConfigDict

from src.models.room import Room


class GetBookmark(Room):
    id: int
    model_config = ConfigDict(from_attributes=True)


class Bookmark(BaseModel):
    user_id: int | None
    model_config = ConfigDict(from_attributes=True)

