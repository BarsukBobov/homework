from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    Field
)


class BaseUser(BaseModel):
    id: int = 0
    en: Optional[bool]
    name: Optional[str] = ''
    email: Optional[str] = ''
    ctime: Optional[datetime] = Field(None, nullable=True)
    atime: Optional[datetime] = Field(None, nullable=True)
    dtime: Optional[datetime] = Field(None, nullable=True)

    @property
    def is_authenticated(self):
        return bool(self.id)


class Anonymous(BaseUser):
    pass


class User(BaseUser):
    pass
