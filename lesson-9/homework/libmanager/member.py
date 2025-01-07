from .book import Book
from .errors import BookAlreadyBorrowedException, BookNotFoundException, MemberLimitExceededException

class Member:
    def __init__(self, name: str, borrowed_books: list[Book] = None) -> None:
        self.name = name
        self._borrowed_books = []
        if borrowed_books:
            self.borrowed_books = borrowed_books
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name

    @property
    def borrowed_books(self) -> list:
        return self._borrowed_books
    
    @borrowed_books.setter
    def borrowed_books(self, borrowed_books: list) -> None:
        if not isinstance(borrowed_books, list):
            raise TypeError("Borrowed books must be a list")
        for book in borrowed_books:
            if book.is_borrowed:
                raise BookAlreadyBorrowedException("Book is already borrowed")
            book.is_borrowed = True
        self._borrowed_books.extend(borrowed_books)

    def borrow_book(self, book: Book) -> None:
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed")
        book.is_borrowed = True
        self.borrowed_books.append(book)
    
    def return_book(self, book: Book) -> None:
        if book not in self.borrowed_books:
            raise BookNotFoundException("Book not found")
        book.is_borrowed = False
        self.borrowed_books.remove(book)
    
    def __str__(self) -> str:
        return f"Member({self.name})"
    
    def __repr__(self):
        return f"Member({self.name})"

