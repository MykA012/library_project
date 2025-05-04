from pydantic import BaseModel
from typing import Optional, List

#Authors models
class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True


#Books models
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    year: Optional[int] = None
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True