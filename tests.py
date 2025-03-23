import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        assert collector.get_book_genre('Новая книга') == ''

    def test_books_with_age_rating_not_in_children_list(self):
        collector = BooksCollector()
        collector.add_new_book('Страх и ужас')
        collector.set_book_genre('Страх и ужас', 'Ужасы')
        collector.add_new_book('Веселая история')
        collector.set_book_genre('Веселая история', 'Комедии')
        assert 'Страх и ужас' not in collector.get_books_for_children()
        assert 'Веселая история' in collector.get_books_for_children()

    @pytest.mark.parametrize("book_name", ["", "A" * 41])
    def test_add_new_book_invalid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Неправильный жанр')
        assert collector.get_book_genre('Книга') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Детективная история')
        collector.set_book_genre('Детективная история', 'Детективы')
        assert 'Детективная история' in collector.get_books_with_specific_genre('Детективы')

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        collector.delete_book_from_favorites('Любимая книга')
        assert 'Любимая книга' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']
