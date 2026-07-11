class Book:

    def __init__(self, title, author, pages, rating):
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = rating

    def __str__(self):
        return (
            f"{self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages}\n"
            f"Rating: {self.rating}/5"
        )
