from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select
from fastapi.security import OAuth2PasswordRequestForm

from ..schemas import Login , Token
from ..models import UserModel

from ..hashing import Hash
from ..dependencies import SessionDep
from ..JWTtoken import create_access_token



router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
# OAuth2PasswordRequestForm contains username and password
def login(session: SessionDep, request: OAuth2PasswordRequestForm = Depends()):
    user = session.exec(select(UserModel).where(UserModel.email == request.username)).first()
    if not user:
        raise HTTPException(status_code=404, detail=f'email: {request.username} not found')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=404, detail='Invalid Password')
    
    access_token = create_access_token(data={"sub": user.email})

    return Token(access_token=access_token, token_type="bearer")

