from pydantic import BaseModel, ConfigDict


class Bookmark(BaseModel):
    room_id: int
    model_config = ConfigDict(from_attributes=True)


class AddBookmark(Bookmark):
    user_id: int


class BookmarkId(BaseModel):
    id: int
