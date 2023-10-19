import logging
from typing import (
    Optional
)
from models.users import (
    User
)
from misc import db

logger = logging.getLogger(__name__)

TABLE = 'users'

USER_DISPLAY_FIELDS = [
    'id',
    'en',
    'name',
    'email',
    'ctime',
    'atime',
    'dtime',
]


async def get_user(
        conn: db.Connection,
        pk: Optional[int]
) -> Optional[User]:
    values = [pk]
    query = f'SELECT {", ".join(USER_DISPLAY_FIELDS)} FROM {TABLE} WHERE id = $1 AND en'
    result = await conn.fetchrow(query, *values)
    return db.record_to_model(User, result)
