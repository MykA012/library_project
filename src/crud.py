from sqlalchemy.orm import Session
import models
import schemas


# POST
def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_books_list(db: Session, books_list: list[schemas.BookCreate]):
    db_books_list = [models.Book(**book.model_dump()) for book in books_list]
    for db_book in db_books_list:
        db.add(db_book)
    db.commit()
    return db_books_list

# GET
def get_single_author(db: Session, author_id: int):
    query = db.query(models.Author)
    return query.filter(models.Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(models.Author)
    return query.offset(skip).limit(limit).all()


def get_single_book(db:Session, book_id: int):
    query = db.query(models.Book)
    return query.filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(models.Book)
    return query.offset(skip).limit(limit).all()

# DELETE
def delete_author(db: Session, author_id: int):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not db_author:
        return False

    db.delete(db_author)
    db.commit()
    return True

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return False

    db.delete(db_book)
    db.commit()
    return True