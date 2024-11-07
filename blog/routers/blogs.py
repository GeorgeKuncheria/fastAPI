from fastapi import APIRouter,status,HTTPException
from sqlmodel import select

from ..dependencies import SessionDep

from ..models import BlogModel
from ..schemas import Blog, ShowBlog

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog',

)


@router.post('',status_code=status.HTTP_201_CREATED)
def create(request : Blog, session : SessionDep) -> BlogModel: 
    new_model = BlogModel(title= request.title , body = request.body , creator_id=2)
    session.add(new_model)
    session.commit()
    session.refresh(new_model)
    return new_model


# To get all blogs
@router.get('/all-blogs')
def all(session: SessionDep ) -> list[BlogModel]:
    allBlogs = session.exec(select(BlogModel)).all()
    return allBlogs


# To get some blogs
@router.get('/some-blogs')
def someBlogs(session: SessionDep ) -> list[BlogModel]:
    allBlogs = session.exec(select(BlogModel).where(BlogModel.id >2 )).all()
    return allBlogs


# To get single one and to show the title for the blog title  as a response instead of the whole blog data we use 'response_model' parameter
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ShowBlog)
def select_blog(session : SessionDep , id : int ):
    blog= session.exec(select(BlogModel).where(BlogModel.id == id)).first()

    # Use .first() to get a single blog by id.
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    

    return blog


# To delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(session: SessionDep , id : int):
    blog = session.exec(select(BlogModel).where(BlogModel.id == id)).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    session.delete(blog)
    session.commit()
    return (f'Blog with id {id} deleted successfully')

# To update a blog
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id : int,session : SessionDep, request : Blog):
    blog = session.exec(select(BlogModel).where(BlogModel.id == id)).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    blog.title= request.title
    blog.body = request.body

    session.add(blog)
    session.commit()
    session.refresh(blog)
    return (f'Blog with id {id} updated successfully')


