class BookNotFoundException(Exception):
    pass

class MemberNotFoundException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass