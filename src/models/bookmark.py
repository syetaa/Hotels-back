
from pydantic import BaseModel, ConfigDict

from src.models.room import Room


class Bookmark(Room):
    id: int
    model_config = ConfigDict(from_attributes=True)


class AddBookmark(Bookmark):
    user_id: int


class BookmarkId(BaseModel):
    id: int