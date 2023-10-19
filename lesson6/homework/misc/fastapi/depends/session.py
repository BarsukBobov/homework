import logging

from fastapi import Request, Response, Security, Depends
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKeyCookie

from db.users import get_user
from misc import db, redis
from misc.fastapi.depends.db import get as get_db
from misc.fastapi.depends.redis import get as get_redis
from misc.session import (
    COOKIE_SESSION_NAME,
    HEADERS_SESSION_NAME,
    TOKEN_SESSION_NAME,

    COOKIE_SESSION,
    HEADERS_SESSION,
    TOKEN_SESSION,

    Session,
    SessionType, MESSAGE_BODY_SESSION
)

logger = logging.getLogger(__name__)

api_key_query = APIKeyQuery(name=TOKEN_SESSION_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=HEADERS_SESSION_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=COOKIE_SESSION_NAME, auto_error=False)


async def get_session_cookie(
        request: Request,
        response: Response,
        db_conn: db.Connection = Depends(get_db),
        redis_conn: redis.Connection = Depends(get_redis),
        api_key_cookie: str = Security(api_key_cookie)
) -> Session:
    session = await get_session(
        db_conn,
        redis_conn,
        api_key_cookie
    )
    request.state.session = session
    if session.session_type == COOKIE_SESSION:
        response.set_cookie(COOKIE_SESSION_NAME, session.key, max_age=session.max_age)

    yield session

    await save_to_redis(session, redis_conn)


async def get_session_header(
        request: Request,
        response: Response,
        db_conn: db.Connection = Depends(get_db),
        redis_conn: redis.Connection = Depends(get_redis),
        api_key_header: str = Security(api_key_header)
) -> Session:
    session = await get_session(
        db_conn,
        redis_conn,
        api_key_header
    )
    request.state.session = session
    if session.session_type == COOKIE_SESSION:
        response.set_cookie(COOKIE_SESSION_NAME, session.key, max_age=session.max_age)
    logger.info("22")
    yield session
    logger.info("11")
    await save_to_redis(session, redis_conn)


async def get_session_query(
        request: Request,
        response: Response,
        db_conn: db.Connection = Depends(get_db),
        redis_conn: redis.Connection = Depends(get_redis),
        api_key_query: str = Security(api_key_query)
) -> Session:
    session = await get_session(
        db_conn,
        redis_conn,
        api_key_query
    )
    request.state.session = session
    if session.session_type == COOKIE_SESSION:
        response.set_cookie(COOKIE_SESSION_NAME, session.key, max_age=session.max_age)

    yield session

    await save_to_redis(session, redis_conn)


async def get_session_message_body(
        request: Request,
        response: Response,
        sid: str,
        db_conn: db.Connection = Depends(get_db),
        redis_conn: redis.Connection = Depends(get_redis)
) -> Session:
    session = await get_session(
        db_conn,
        redis_conn,
        api_key_message_body=sid
    )
    request.state.session = session
    if session.session_type == COOKIE_SESSION:
        response.set_cookie(COOKIE_SESSION_NAME, session.key, max_age=session.max_age)

    yield session

    await save_to_redis(session, redis_conn)


async def get_session(
        db_conn: db.Connection,
        redis_conn: redis.Connection,
        api_key_query: str = None,
        api_key_header: str = None,
        api_key_cookie: str = None,
        api_key_message_body: str = None,
) -> Session:
    values = [
        [api_key_cookie, COOKIE_SESSION],
        [api_key_header, HEADERS_SESSION],
        [api_key_query, TOKEN_SESSION],
        [api_key_message_body, MESSAGE_BODY_SESSION],
    ]
    logger.info("33")
    session = None
    for key, session_type in values:
        if key:
            session = await get_from_redis(session_type, key, redis_conn)
            if session is not None:
                session = await get_session_user(session, db_conn)
                return session

    return Session(
        session_type=COOKIE_SESSION
    )


async def get_from_redis(session_type: SessionType, key: str, redis_conn: redis.Connection) -> Session:
    data = await redis.get(cache_key(key), redis_conn)
    if data is None:
        return None
    session = Session(
        session_type=session_type,
        key=key,
        data=data
    )
    return session


async def save_to_redis(session: Session, redis_conn: redis.Connection):
    await redis.setex(
        cache_key(session.key),
        session.max_age,
        session.data,
        redis_conn
    )


async def get_session_user(session: Session, db_conn: db.Connection) -> Session:
    if session.session_user_id:
        user = await get_user(db_conn, session.session_user_id)
        if user is not None:
            session.set_user(user)
    return session


def cache_key(key: str) -> str:
    return f'session_{key}'
