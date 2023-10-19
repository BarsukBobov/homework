from fastapi import APIRouter
from . import (
    auth,
)


def register_routers(app):
    router = APIRouter(prefix='/api/v1')

    router.include_router(
        auth.router,
    )
    app.include_router(router)
    return app
