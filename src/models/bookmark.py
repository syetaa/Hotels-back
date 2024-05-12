from pydantic import ConfigDict

from src.models.room import Room


class GetBookmark(Room):
    model_config = ConfigDict(from_attributes=True)
