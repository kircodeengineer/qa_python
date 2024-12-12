import pytest

from main import BooksCollector

@pytest.fixture(scope='function')
def books_collector():
    return BooksCollector()

books_comedy_genre = [
    ['Назад в будущее 1', 'Комедии'],
    ['Назад в будущее 2', 'Комедии'],
    ['Назад в будущее 3', 'Комедии'],
]
@pytest.fixture(scope='function')
def comedy_books_collector(books_collector):
    for book, genre in books_comedy_genre:
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
    return books_collector