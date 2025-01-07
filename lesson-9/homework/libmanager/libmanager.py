from .book import Book
from .member import Member
from .errors import MemberNotFoundException, BookNotFoundException


class LibManager:
    def __init__(self) -> None:
        self.__books = []
        self.__members = []

    def add_book(self, *book: Book) -> None:
        self.__books.extend(book)
    
    def remove_book(self, book: Book) -> None:
        if book not in self.__books:
            raise BookNotFoundException("Book not found")
        self.__books.remove(book)

    def add_member(self, *member: list[Member]) -> None:
        if len(member) == 0:
            raise ValueError("No members provided")
        self.__members.extend(member)
    
    def remove_member(self, member: Member) -> None:
        if member not in self.__members:
            raise MemberNotFoundException("Member not found")
        self.__members.remove(member)
    
    def borrow_book(self, member: Member, book: Book) -> None:
        if member not in self.__members:
            raise MemberNotFoundException("Member not found")
        if book not in self.__books:
            raise BookNotFoundException("Book not found")
        member.borrow_book(book)
    
    def return_book(self, member: Member, book: Book) -> None:
        if member not in self.__members:
            raise MemberNotFoundException("Member not found")
        if book not in self.__books:
            raise BookNotFoundException("Book not found")
        member.return_book(book)
    
    def list_books(self) -> list:
        return self.__books
    
    def list_members(self) -> list:
        return self.__members
    
    def list_borrowed_books(self) -> list:
        return [book for book in self.__books if book.is_borrowed]
    
    def is_exist(self, item: Book | Member) -> bool:
        return item in self.__books or item in self.__members




