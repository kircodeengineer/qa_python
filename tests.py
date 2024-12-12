import pytest

from conftest import books_comedy_genre

books = [
            ['Автостопом по галактие', 'Фантастика'],
            ['Ловец снов', 'Ужасы'],
            ['Счастливое число Слевина', 'Детективы'],
            ['Утиный истории', 'Мультфильмы'],
            ['Бетховен', 'Комедии']
        ]

class TestBooksCollector:
    @pytest.mark.parametrize(
        'book, genre', books
    )
    def test_set_book_genre_existing_genre_can_be_set(self,books_collector, book, genre ):
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
        assert books_collector.books_genre[book] == genre

    @pytest.mark.parametrize(
        'book, genre', books
    )
    def test_get_book_genre_returns_added_book_with_existing_genre(self, books_collector, book, genre):
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
        assert books_collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre_for_added_books_with_existing_genre(self, comedy_books_collector):
        books_list = []
        genre = None
        for book, genre in books_comedy_genre:
            books_list.append(book)
        assert comedy_books_collector.get_books_with_specific_genre(genre) == books_list

    def test_get_book_genre_empty_books_genre(self, books_collector):
        assert len(books_collector.get_books_genre()) == 0

    def test_get_books_genre_add_cartoon_genre_returns_cartoon_genre(self, books_collector):
        book = 'Чудеса на виражах'
        genre = 'Мультфильмы'
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
        assert books_collector.get_books_genre() == {book:genre}

    def test_get_books_for_children_return_all_added_comedy_books(self, comedy_books_collector):
        assert comedy_books_collector.get_books_for_children() == [books_comedy_genre[0][0],
                                                                   books_comedy_genre[1][0],
                                                                   books_comedy_genre[2][0]]

    def test_add_book_in_favorites_after_add_one_book_favorites_contains_list_of_one_book(self, comedy_books_collector):
        comedy_books_collector.add_book_in_favorites(books_comedy_genre[0][0])
        assert comedy_books_collector.favorites == [books_comedy_genre[0][0]]

    def test_get_list_of_favorites_books_after_add_one_favorite_book_returns_list_with_one_added_book(self, comedy_books_collector):
        comedy_books_collector.add_book_in_favorites(books_comedy_genre[0][0])
        assert comedy_books_collector.get_list_of_favorites_books() == [books_comedy_genre[0][0]]

    def test_delete_book_from_favorites_after_adding_one_book_favorites_contains_empty_list(self, comedy_books_collector):
        comedy_books_collector.add_book_in_favorites(books_comedy_genre[0][0])
        comedy_books_collector.delete_book_from_favorites(books_comedy_genre[0][0])
        assert len(comedy_books_collector.favorites) == 0

    def test_get_books_with_specific_genre_without_add_returns_empty_list(self, books_collector):
        assert len(books_collector.get_books_with_specific_genre(books_comedy_genre[0][1])) == 0

    def test_get_books_for_children_after_add_books_all_genre_returns_only_children_books(self, books_collector):
        for book, genre in books:
            books_collector.add_new_book(book)
            books_collector.set_book_genre(book, genre)
        assert books_collector.get_books_for_children() == [books[0][0],
                                                            books[3][0],
                                                            books[4][0]]

    def test_add_new_book_just_added_book_has_no_genre(self, books_collector):
        books_collector.add_new_book(books[0][0])
        assert len(books_collector.books_genre[books[0][0]]) == 0

    def test_set_book_genre_not_existing_genre_cant_be_set(self,books_collector):
        book = "Звёздная пыль"
        genre = "Фэнтези"
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
        assert books_collector.books_genre[book] != genre

    def test_add_new_book_second_add_existing_book_no_replacing_genre(self, comedy_books_collector):
        comedy_books_collector.add_new_book(books_comedy_genre[0][0])
        assert comedy_books_collector.get_book_genre(books_comedy_genre[0][0]) == books_comedy_genre[0][1]

    @pytest.mark.parametrize(
        'book_wrong_len',
        ["",
         "12345678901234567890123456789012345678901"]
    )
    def test_add_new_book_wrong_book_len_no_book_in_books_collector(self, books_collector, book_wrong_len):
        books_collector.add_new_book(book_wrong_len)
        assert book_wrong_len not in books_collector.books_genre