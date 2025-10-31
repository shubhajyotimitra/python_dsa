# library class system solution day38
class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
    def addBook(self,book):
        self.books.append(book)
        self.noBooks = len(self.books) 
    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are:")
        for book in self.books:
            print(f"- {book}")
        
l1 = Library()      
l1.addBook("Python Basics")
l1.addBook("Data Science with Python")  
l1.addBook("Machine Learning")
l1.showInfo()
    
