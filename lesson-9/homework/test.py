from libmanager.libmanager import LibManager
from libmanager.member import Member
from libmanager.book import Book


library = LibManager()

book1 = Book("Author1", "Title1", False)
book2 = Book("Author2", "Title2", False)
book3 = Book("Author3", "Title3", False)
book4 = Book("Author4", "Title4", False)
book5 = Book("Author5", "Title5", False)
book6 = Book("Author6", "Title6", False)
book7 = Book("Author7", "Title7", False)
book8 = Book("Author8", "Title8", False)

library.add_book(book1, book2, book3, book4, book5, book6, book7, book8)

member1 = Member("John Doe", [book1, book2])
member2 = Member("Kamoliddin Mehmonov", [book3, book4, book5])
member3 = Member("Bakirov Eldorbek", [book6])
member4 = Member("Xaydarov Feruz", [book7])
member5 = Member("Jo'raboyev Tursunpo'lat", [book8])


library.add_member(member1, member2, member3, member4, member5)

print("-"*20)
print("All members list")
print(library.list_members())

print("-"*20)
print("All borrowed books")
print(library.list_borrowed_books())

print("-"*20)
print("member1's borrowed books")
print(member1.borrowed_books)