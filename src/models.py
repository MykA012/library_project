from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True,)
    name: Mapped[str] = mapped_column(nullable=False)
    bio: Mapped[Optional[str]] = mapped_column()
    
    books: Mapped[list["Book"]] = relationship(
        back_populates="author", 
        cascade="all, delete-orphan",
        passive_deletes=True
    )


class Book(Base):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column()
    year: Mapped[Optional[int]] = mapped_column()
    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id", ondelete="CASCADE")
    )
    
    author: Mapped["Author"] = relationship(back_populates="books")
