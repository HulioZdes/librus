def find_by_title(books, keyword):

    keyword = keyword.lower()

    return [

        book

        for book in books

        if keyword in book.title.lower()

    ]


def find_by_author(books, keyword):

    keyword = keyword.lower()

    return [

        book

        for book in books

        if keyword in book.author.lower()

    ]
