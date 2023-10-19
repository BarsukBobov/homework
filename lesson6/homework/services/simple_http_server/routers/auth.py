import logging
from fastapi import (
    APIRouter,
    Depends,
)

from misc.fastapi.depends.session import (
    get_session_cookie,
    get_session_header,
    get_session_query,
    get_session_message_body
)

from misc.session import (
    Session,
)
from models.auth import (
    MeResponse,
    MeSuccessResponse,
)

DAY = 86400  # in seconds

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

logger = logging.getLogger(__name__)


@router.get('/me_cookie', name='me_cookie', response_model=MeSuccessResponse)
async def me_by_cookie(
        session: Session = Depends(get_session_cookie)
):
    return MeSuccessResponse(data=MeResponse(me=session.user, token=session.key))


@router.get('/me_header', name='me_header', response_model=MeSuccessResponse)
async def get_me_with_header(
        session: Session = Depends(get_session_header)
):
    return MeSuccessResponse(data=MeResponse(me=session.user, token=session.key))


@router.get('/me_query', name='me_query', response_model=MeSuccessResponse)
async def get_me_with_query(
        session: Session = Depends(get_session_query)
):
    return MeSuccessResponse(data=MeResponse(me=session.user, token=session.key))


@router.get('/me_message_body', name='me_message_body', response_model=MeSuccessResponse)
async def get_me_with_message_body(
        session: Session = Depends(get_session_message_body)
):
    return MeSuccessResponse(data=MeResponse(me=session.user, token=session.key))
