class Library:

    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def show(self):

        print("=" * 35)
        print("BOOK COLLECTION")
        print("=" * 35)

        for book in self.books:
            print(book)
            print()
