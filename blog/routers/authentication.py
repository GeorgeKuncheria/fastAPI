from fastapi import APIRouter, HTTPException
from sqlmodel import select

from ..schemas import Login
from ..models import UserModel

from ..hashing import Hash
from ..dependencies import SessionDep

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request : Login , session : SessionDep):
    user = session.exec(select(UserModel).where(UserModel.email == request.email)).first()
    if not user:
        raise HTTPException(status_code=404,detail=f'email: {request.email} not found')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=404,detail='Invalid Password')
    
    return 'Login Successful'