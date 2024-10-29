# Library Management System

# parent class 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def displayInfo(self):
        return f"Title: {self.title}, Author: {self.author}"
    
#  Child / derived class inheriting parent class   
class LibraryBook(Book):
        def __init__(self, title, author, isbn,copies_available):
            super().__init__(title, author)
            self.isbn = isbn
            self.copies_available = copies_available
        def borrow_a_book(self):
            if self.copies_available > 0:
                self.copies_available -=1
                return f'Borrowed {self.title}, copies left {self.copies_available}'
            else:
                return f'No of Titles {self.title} available '
        def return_a_book(self):
             self.copies_available +=1

             return f'{self.title} returned, copies available {self.copies_available}' 

book1 = LibraryBook("River between", 'Margret Ogola', 12345, 18)

print(book1.displayInfo())
print(book1.borrow_a_book())
print(book1.return_a_book())



        