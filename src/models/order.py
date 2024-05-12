from pydantic import ConfigDict

from src.models.room import Room


class GetOrder(Room):
    model_config = ConfigDict(from_attributes=True)
