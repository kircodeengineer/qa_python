# qa_python
Учебный проект курса Яндекс. Практикум

1. `test_set_book_genre_existing_genre_can_be_set` - добавляемым книгам присваивается жанр
2. `test_get_book_genre_returns_added_book_with_existing_genre` - названию книги возвращается жанр, существующий в БД
3. `test_get_books_with_specific_genre_for_added_books_with_existing_genre` - возвращается список книг заданного жанра, существующего в БД
4. `test_get_book_genre_empty_books_genre` - возвращается пустой список, при отсутствии добавленных книг
5. `test_get_books_genre_add_cartoon_genre_returns_cartoon_genre` - возвращается словарь книг заданного жанра
6. `test_add_book_in_favorites_after_add_one_book_favorites_contains_list_of_one_book` - в БД список любимых книг из одной добавленной книги
7. `test_get_list_of_favorites_books_after_add_one_favorite_book_returns_list_with_one_added_book` - возвращается список любимых книг из одной добавленной книги
8. `test_delete_book_from_favorites_after_adding_one_book_returns_empty_list` - в БД нет ранее добавленное любимой книги
9. `test_get_books_with_specific_genre_without_add_return_empty_list` - возвращается пустой список книг заданного жанра, существующего в БД, если таковых не было добавлено
10. `test_get_books_for_children_only_children_books` - книги с возрастным рейтингом отсутствуют в списке книг для детей
11. `test_add_new_book_just_added_book_has_no_genre` - у добавленной книги нет жанра
12. `test_set_book_genre_not_existing_genre_cant_be_set` - добавляемым книгам не присваивается несуществующий в БД жанр
13. `test_add_new_book_second_add_existing_book_no_replacing_genre` - повторное добавление книги не перезаписывает её жанр
14. `test_add_new_book_wrong_book_len_no_book_in_books_collector` - не добавляются книги 0 и 41 символ
