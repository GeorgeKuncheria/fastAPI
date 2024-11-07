from fastapi import HTTPException, status
from sqlmodel import select

from ..models import BlogModel




def createBlog(request,session):
    new_model = BlogModel(title= request.title , body = request.body , creator_id=2)
    session.add(new_model)
    session.commit()
    session.refresh(new_model)
    return new_model


def get_all(session):
    allBlogs = session.exec(select(BlogModel)).all()
    return allBlogs


def someBlogs(session):
    someBlogs = session.exec(select(BlogModel).where(BlogModel.id >= 2)).all()
    return someBlogs


def selectBlogs(session,id):
    blog= session.exec(select(BlogModel).where(BlogModel.id == id)).first()

    # Use .first() to get a single blog by id.
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    

    return blog


def destroyBlog(session,id):
    blog = session.exec(select(BlogModel).where(BlogModel.id == id)).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    session.delete(blog)
    session.commit()
    return (f'Blog with id {id} deleted successfully')


def updateBlog(session,id,request):
    blog = session.exec(select(BlogModel).where(BlogModel.id == id)).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    blog.title= request.title
    blog.body = request.body

    session.add(blog)
    session.commit()
    return blog