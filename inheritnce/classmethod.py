class Library():
    total_books=0
    @classmethod
    def add_books(cls,count):
        cls.total_books += count
        print(f"The total books in the store are: {cls.total_books}")
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
class Book(Library):
    def book_info(self):
        print(f"The book {self.title} has the author {self.author}")
        Library.add_books(1)
        
b=Book("Peace","Binamra")
b.book_info()
b2=Book("War","John")
b2.book_info()
      
