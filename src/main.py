import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud, models, schemas
from database import get_session, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# POST
@app.post("/authors/", tags=["Authors"], summary="Add author", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_session)):
    return crud.create_author(db=db, author=author)

@app.post("/books/", tags=["Books"], summary="Add single book", response_model=schemas.Book)
def create_book(book: schemas.BookCreate | list[schemas.BookCreate], db: Session = Depends(get_session)):
    return crud.create_book(db=db, book=book)

@app.post("/books/bulk", tags=["Books"], summary="Add books list", response_model=list[schemas.Book])
def create_books_list(books_list: list[schemas.BookCreate], db: Session = Depends(get_session)):
    return crud.create_books_list(db=db, books_list=books_list)

# GET
@app.get("/authors/{author_id}", tags=["Authors"], summary="Get one author with id", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_session)):
    db_author = crud.get_single_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@app.get("/authors/", tags=["Authors"], summary="Get all authors", response_model=list[schemas.Author])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return authors


@app.get("/books/{book_id}", tags=["Books"], summary="Get one book with id", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_session)):
    db_book = crud.get_single_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.get("/books/", tags=["Books"], summary="Get all books", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

# DELETE
@app.delete("/authors/{author_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Authors"], summary="Delete author")
def delete_author(author_id: int, db: Session = Depends(get_session)):
    if not crud.delete_author(db, author_id=author_id):
        raise HTTPException(status_code=404, detail="Author not found")
    return {"ok": True}

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Books"], summary="Delete book")
def delete_book(book_id: int, db: Session = Depends(get_session)):
    if not crud.delete_book(db, book_id=book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
