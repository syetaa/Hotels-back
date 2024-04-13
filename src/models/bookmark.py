from pydantic import BaseModel, ConfigDict


class AddBookmark(BaseModel):
    user_id: int
    room_id: int


class BookmarkId(BaseModel):
    id: int


class Bookmark(AddBookmark, BookmarkId):
    model_config = ConfigDict(from_attributes=True)
