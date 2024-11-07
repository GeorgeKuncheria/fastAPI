# dependencies.py
from typing import Annotated
from .database import Session, get_session
from fastapi import Depends

SessionDep = Annotated[Session, Depends(get_session)]
