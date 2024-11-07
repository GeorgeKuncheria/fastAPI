from fastapi import HTTPException, status
from sqlmodel import select

from ..models import UserModel
from ..hashing import Hash


def createUser(session, request):
    # storing the hashed password in the database imported from hashing.py
    new_user = UserModel(name=request.name,email=request.email,password=Hash.bcrypt(request.password))

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user



def selectUser(session, id):
    user = session.exec(select(UserModel).where(UserModel.id == id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    return user