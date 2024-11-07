from sqlmodel import Field, SQLModel,Relationship

class BlogModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    body: str | None = Field(default=None)

    creator_id : int | None = Field(default=None, foreign_key='usermodel.id')

    creator : "UserModel" = Relationship(back_populates='blogs')




class UserModel(SQLModel , table = True):
    id : int | None = Field(default=None, primary_key=True)
    name : str = Field(index=True)
    email : str = Field(index=True)
    password : str

    blogs : list["BlogModel"] = Relationship(back_populates='creator')

