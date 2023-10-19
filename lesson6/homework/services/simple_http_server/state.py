import asyncio
from fastapi import FastAPI
from misc import db, redis


class State(object):
    def __init__(self, loop: asyncio.BaseEventLoop, config: dict):
        super().__init__()
        self.loop: asyncio.BaseEventLoop = loop
        self.config: dict = config
        self.db_pool: db.Connection | None = None
        self.redis_pool: redis.Connection | None = None
        self.app: FastAPI | None = None
