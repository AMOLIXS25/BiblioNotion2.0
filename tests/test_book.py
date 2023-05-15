from contextlib import closing
import sqlite3
import pytest

from models.book import BookModel, BookStorage

from os.path import exists
import os


class TestBookModel:
    """TestBookModel class"""
    def test_book_constructor_with_all_parameters(self):
        """Méthod qui permet de tester le constructeur du BookModel en passant tous les paramètres"""
        book_model = BookModel(
            title="Harry potter",
            cover="./books/cover/test.jpeg",
            authors="J.K Rowling",
            pages=14,
            isbn="9878465464",
            published_date="2003",
            id=5,
            types="fantastique",
            evaluation=3,
            status="Pas commencé"
        )
        assert(
            book_model.title == "Harry potter" and
            book_model.cover == "./books/cover/test.jpeg" and
            book_model.authors == "J.K Rowling" and
            book_model.pages == 14 and
            book_model.isbn == "9878465464" and
            book_model.published_date == "2003" and
            book_model.id == 5 and
            book_model.types == "fantastique" and
            book_model.evaluation == 3,
            book_model.status == "Pas commencé"
        )

    def test_book_constructor_with_default_parameters(self):
        """Méthode qui test la construction d'un livre avec les paramètres par défauts"""
        book_model = BookModel(
            title="Harry potter",
            cover="./books/cover/test.jpeg",
            authors="J.K Rowling",
            pages=14,
            isbn="9878465464",
            published_date="2003"
        )
        assert(
            book_model.title == "Harry potter" and
            book_model.cover == "./books/cover/test.jpeg" and
            book_model.authors == "J.K Rowling" and
            book_model.pages == 14 and
            book_model.isbn == "9878465464" and
            book_model.published_date == "2003" and
            book_model.id == -1 and
            book_model.types == "" and
            book_model.evaluation == -1,
            book_model.status == "Pas commencé"
        )


class TestBookStorage:
    """TestBookStorage class"""
    @pytest.fixture
    def book_storage(self):
        book_storage = BookStorage("test.db")
        yield book_storage

    def test_if_connection_to_the_database_is_etablished(self, book_storage):
        """Méthode qui permet de tester si la connection à la base de  données s'étable correctement"""
        assert exists("test.db") == True

    def test_books_table_has_correctly_been_created(self, book_storage):
        """Méthode qui permet de tester si la table livre à correctement été créer"""
        sql_request = """SELECT COUNT(*) FROM T_Books"""
        try:
            with closing(book_storage.cursor) as cursor:
                res = cursor.execute(sql_request)
        except sqlite3.OperationalError:
            # Je relève une erreur de test si il y a une operationnal error
            assert False

    def test_insert_a_book(self, book_storage):
        """Méthode qui permet de tester l'insertion d'un livre dans la base de donnée"""
        pass
    
        
