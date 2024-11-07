from fastapi import APIRouter,status,HTTPException
from sqlmodel import select

from ..dependencies import SessionDep

from ..models import UserModel
from ..hashing import Hash
from ..schemas import User,ShowUser
from ..repository.userRepo import createUser, selectUser


router = APIRouter(
    tags=['User'],
    prefix='/user',
)

# To create a user
@router.post('',status_code=status.HTTP_201_CREATED)
def create_user(request: User , session : SessionDep):
    return createUser(session, request)



# To show user
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ShowUser)
def select_user(id : int, session : SessionDep ):
    return selectUser(session,id)
