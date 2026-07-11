from library import Library
from sample_data import books
from statistics import show_statistics
from search import find_by_title

library = Library()

for book in books:
    library.add(book)

library.show()

show_statistics(library.books)

print("\nSearch Results:\n")

results = find_by_title(
    library.books,
    "Python"
)

for book in results:
    print(book)
    print()
