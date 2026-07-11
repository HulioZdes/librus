def show_statistics(books):

    total_pages = sum(book.pages for book in books)

    average_rating = (
        sum(book.rating for book in books)
        / len(books)
    )

    print("-" * 35)
    print(f"Books: {len(books)}")
    print(f"Average Rating: {average_rating:.2f}")
    print(f"Total Pages: {total_pages}")
