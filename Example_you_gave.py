from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Optional
from uuid import UUID, uuid4

app = FastAPI()

class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    pages: int
    language: str


class Bookcreate(BaseModel):
    title: str
    author: str
    year: int
    pages: int
    language: str

class BookUpdate(BaseModel):
    title: str
    pages: int
    language: str

class Books(BaseModel):
    books: List[Book]

class Response(BaseModel):
    message: Optional[str] = None
    has_error: bool = None
    error_message: Optional[str] = None
    data: Optional[Book | Books] = None

books: dict[str, Book] = {}

@app.get("/")
def home():
    return {"messae": "Hello from the books API"}

@app.get("/books")
def get_book():
    return books

@app.get("/books{id}")
def get_book_by_id(id: UUID):
    book = books.get(str(id))
    if not book:
        return {"error": "Book not found"}
    return book 

@app.post("/books")
def add_book(book_in: Bookcreate):
    book = Book(
        id=str(uuid4()),
        **book_in.model_dump()
    )
    books[book.id] = book
    return Response(message="Book added successfuly", data=book)

@app.put("/book{id}")
def update_book(id: UUID, book_in: BookUpdate):
    book = books.get(str(id))
    if not book:
        return {"error": "book not found"}
    
    book.title = book_in.title
    book.pages = book_in.pages
    book.language = book_in.language

    return Response(message="Book updated successfully")