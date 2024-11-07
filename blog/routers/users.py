from fastapi import APIRouter,status,HTTPException
from sqlmodel import select

from ..dependencies import SessionDep

from ..models import UserModel
from ..hashing import Hash
from ..schemas import User,ShowUser

router = APIRouter(
    tags=['User'],
    prefix='/user',
)

# To create a user
@router.post('',status_code=status.HTTP_201_CREATED)
def create_user(request: User , session : SessionDep):

    # storing the hashed password in the database imported from hashing.py
    new_user = UserModel(name=request.name,email=request.email,password=Hash.bcrypt(request.password))

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user



# To show user
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ShowUser)
def select_user(id : int, session : SessionDep ):
    user = session.exec(select(UserModel).where(UserModel.id == id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    return user
