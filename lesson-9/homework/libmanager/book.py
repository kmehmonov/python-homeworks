class Book:
    def __init__(self, author, title, is_borrowed=False):
        self.author = author
        self.title = title
        self.is_borrowed = is_borrowed

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        if not author:
            raise ValueError("Author cannot be empty")
        self._author = author

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not title:
            raise ValueError("Title cannot be empty")
        self._title = title

    @property
    def is_borrowed(self):
        return self._is_borrowed
    
    @is_borrowed.setter
    def is_borrowed(self, is_borrowed):
        if not isinstance(is_borrowed, bool):
            raise TypeError("is_borrowed must be a boolean")
        self._is_borrowed = is_borrowed
    
    def __str__(self):
        return f"Book({self.title} by {self.author})"
    
    def __repr__(self):
        return f"Book({self.title} by {self.author})"
        