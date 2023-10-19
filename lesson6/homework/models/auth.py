from pydantic import BaseModel
from .base import SuccessResponse
from .users import User


class MeResponse(BaseModel):
    token: str
    me: User


class MeSuccessResponse(SuccessResponse):
    data: MeResponse
