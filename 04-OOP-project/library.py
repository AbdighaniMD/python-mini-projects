class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lenDict = {}

    def displayBook(self):
        print(f"{self.name}, we have following books in our library.")
        sno = 1
        for book in self.bookList:
            print(f"{sno}, {book}")
            sno += 1

    def lenBook(self, book, name):
        if book in self.bookList:
            if book not in self.lenDict:
                self.lenDict.update({book: name})
                print("Lender-Book database has been updated. Your can take the book now.")
            else:
                print(f"Book: is already being used by {self.lenDict[book]}")
        else:
            print(f"This book:-{book} is not relate to our database")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list.")

    def returnBook(self, book):
        if book in self.bookList:
            if book in self.lenDict:
                self.lenDict.pop(book)
                print(f"Ok Thank you, Book:-{book} is received")
        else:
            print(f"This book:{book} is not relate to our database.")