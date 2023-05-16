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
            cover="./books_cover/Gigi2.jpg",
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
    def book(self):
        book_model = BookModel(
            title="Harry potter",
            cover="./books_cover/Gigi2.jpg",
            authors="J.K Rowling",
            pages=14,
            isbn="9878465464",
            published_date="2003",
            id=5,
            types="fantastique",
            evaluation=3,
            status="Pas commencé"
        )
        yield book_model

    @pytest.fixture
    def book_storage(self):
        book_storage: BookStorage = BookStorage("test.db")
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
        sql_request = """SELECT COUNT(*) FROM T_Books"""
        book = BookModel(
            title="test_insert_a_book",
            cover="./books_cover/gg.jpg",
            authors="J.K Rowling",
            pages=14,
            isbn="5465498798745413513544",
            published_date="2003"
        )
        try:
            book_storage.insert_a_book(book)
            with closing(book_storage.cursor) as cursor:
                res = cursor.execute(sql_request)
                assert res.fetchone()[0] > 0
        except sqlite3.IntegrityError:
            pass
        except FileNotFoundError:
            pass

    def test_cover_has_been_created(self):
        """Méthode qui test si la couverture d'un livre se créer bien lorsque l'on créer le livre"""
        assert os.path.exists("books_cover/test_insert_a_book.jpg") == True

    def test_insert_multiple_books(self, book_storage):
        """Méthode qui permet de tester l'insertion de plusieurs livres dans la base de donnée"""
        sql_request = """SELECT COUNT(*) FROM T_Books"""
        books_to_insert = [
            BookModel(
                title="pistolet",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="ty",
                published_date="2003"
            ),
            BookModel(
                title="gigigi",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="ss",
                published_date="2003"
            ),
            BookModel(
                title="Harry JEAN",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="rfefsffsf",
                published_date="2003"
            ),
            BookModel(
                title="bo",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="87987978978979797",
                published_date="2003"
            ),
            BookModel(
                title="tristo",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="jneconnaisdpas",
                published_date="2003"
            ),
            BookModel(
                title="Ha",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="ouijedisoui",
                published_date="2003"
            ),
            BookModel(
                title="H",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="rololalala",
                published_date="2003"
            ),
            BookModel(
                title="potter",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="ppppppppppp",
                published_date="2003"
            ),
            BookModel(
                title="popopopop",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="zqdddqddqzdqdqdqdqddqdzqdqdqdsx",
                published_date="2003"
            ),
            BookModel(
                title="loli",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="lol",
                published_date="2003"
            ),
            BookModel(
                title="pistolsquat",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="ytuaioppmlpjkuhgyd",
                published_date="2003"
            ),
            BookModel(
                title="monkeydluffy",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="c'est le monkey",
                published_date="2003"
            ),
            BookModel(
                title="c'estlefalenpin",
                cover="./books_cover/gg.jpg",
                authors="J.K Rowling",
                pages=14,
                isbn="ouic'estlefalenpinop",
                published_date="2003"
            ),
        ]
        try:
            for book in books_to_insert:
                book_storage.insert_a_book(book)
            with closing(book_storage.cursor) as cursor:
                res = cursor.execute(sql_request)
                assert res.fetchone()[0] > 5
        except sqlite3.IntegrityError:
            pass
        except FileNotFoundError:
            pass
    
    def test_get_all_books(self, book_storage):
        """Méthode qui permet de tester la récupération de tous les livres"""
        get_books = book_storage.get_all_books()
        assert len(get_books) > 2
        
    def test_get_ten_last_books(self, book_storage):
        """Méthode qui test la méthode pour récupérer seulement les derniers livres"""
        get_books = book_storage.get_all_books()
        get_books.reverse()
        get_ten_last_books = book_storage.get_ten_last_books()
        assert get_books[:10] == get_ten_last_books

    def test_get_books_thanks_to_a_search(self, book_storage):
        """Méthode qui permet de tester la recherche d'un ou plusieurs livre(s)"""
        search = "pistol"
        books_list_test = [
            BookModel(
                title="pistolet",
                cover="./books_cover/pistolet.jpg",
                authors="J.K Rowling",
                pages=14,
                id=30,
                isbn="ty",
                published_date="2003"
            ),
            BookModel(
                title="pistolsquat",
                cover="./books_cover/pistolsquat.jpg",
                authors="J.K Rowling",
                pages=14,
                id=26,
                isbn="ytuaioppmlpjkuhgyd",
                published_date="2003"
            )
        ]
        get_books = book_storage.get_books_thanks_to_a_search(search)
        print(get_books)
        assert get_books == books_list_test

    def test_delete_a_book(self, book_storage):
        """Méthode qui permet de tester la suppression d'un livre"""
        book_to_delete = BookModel(
            title="c'estlefalenpin",
            cover="./books_cover/gg.jpg",
            authors="J.K Rowling",
            pages=14,
            id=28,
            isbn="ouic'estlefalenpinop",    
            published_date="2003"
        )
        book_storage.delete_a_book(book_to_delete)
        assert book_to_delete not in book_storage.get_all_books()

    def test_cover_has_been_deleted(self, book_storage):
        """Méthode qui test si la couverture du livre à bien été supprimé"""
        book_to_delete = BookModel(
            title="c'estlefalenpin",
            cover="books_cover/c'estlefalenpin.jpg",
            authors="J.K Rowling",
            pages=14,
            id=28,
            isbn="ouic'estlefalenpinop",    
            published_date="2003"
        )
        book_storage.delete_cover_file_associate_to_book_to_delete(book_to_delete)
        assert os.path.exists("books_cover/c'estlefalenpin.jpg") == False
    
    def test_update_book_cover(self, book_storage):
        """Méthode qui test la mise à jour d'un livre"""
        old_book = BookModel(
            title="monkeydluffy",
            cover="/books_cover/monkeydluffy.jpg",
            authors="J.K Rowling",
            pages=14,
            id=27,
            isbn="c'est le monkey",
            published_date="2003"
        )
        new_book = BookModel(
            title="monkeyluffy2.0",
            cover="./books_cover/monkeydluffy.jpg",
            authors="J.K Rowling",
            pages=500,
            id=27,
            isbn="c'est le monkey2.0",
            published_date="2005"
        )
        book_storage.update_book(old_book, new_book)
        assert new_book in book_storage.get_all_books()

    def test_update_book_cover(self):
        """Méthode qui test si la couverture se met bien à jours lorsqu'on met à jour un livre"""
        new_book = BookModel(
            title="monkeyluffy2.0",
            cover="./books_cover/monkeydluffy.jpg",
            authors="J.K Rowling",
            pages=500,
            id=27,
            isbn="c'est le monkey2.0",
            published_date="2005"
        )
        assert os.path.exists(new_book.cover) == True

    def test_get_number_of_books(self, book_storage):
        """Méthode qui test si la méthode pour renvoyer le nombre de livre fonctionne"""
        assert book_storage.get_number_of_books() == 13