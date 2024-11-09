from fastapi import APIRouter,status,Depends

from ..dependencies import SessionDep
from ..oauth2 import get_current_user

from ..models import BlogModel
from ..schemas import Blog, ShowBlog,User

from ..repository.blogRepo import get_all, someBlogs, selectBlogs, destroyBlog, updateBlog, createBlog




router = APIRouter(
    tags=['Blogs'],
    prefix='/blog',

)


@router.post('',status_code=status.HTTP_201_CREATED)
def create(request : Blog, session : SessionDep,current_users : User = Depends(get_current_user)) -> BlogModel: 
    return createBlog(request,session)


# To get all blogs
@router.get('/all-blogs')
def all(session: SessionDep,current_users : User = Depends(get_current_user)  ) -> list[BlogModel]:
    return get_all(session)


# To get some blogs
@router.get('/some-blogs')
def some_Blogs(session: SessionDep,current_users : User = Depends(get_current_user) ) -> list[BlogModel]:
    return someBlogs(session)


# To get single one and to show the title for the blog title  as a response instead of the whole blog data we use 'response_model' parameter
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ShowBlog)
def select_blog(session : SessionDep , id : int,current_users : User = Depends(get_current_user) ):
    return selectBlogs(session,id)


# To delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(session: SessionDep , id : int,current_users : User = Depends(get_current_user)):
    return destroyBlog(session,id)


# To update a blog
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id : int,session : SessionDep, request : Blog ,current_users : User = Depends(get_current_user)):
    return updateBlog(session,id,request)

