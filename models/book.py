from dataclasses import dataclass, field
import os
import shutil
import sqlite3
import asyncio

from typing import Any

from requests import Response

from contextlib import closing

import requests

from models.setting import SettingStorage


@dataclass
class BookModel:
    """Book classe model"""
    title: str
    cover: str
    authors: str
    pages: int
    isbn: str
    published_date: str
    id: int = field(default=-1)
    types: str = field(default="")
    evaluation: int = field(default=-1)
    status: str = field(default="Pas commencé")


class BookStorage:
    """Classe qui permet d'effectuer des actions sur le modèle book"""
    def __init__(self, name_of_database="data.db"):
        """BookStorage constructeur"""
        self.database: sqlite3.Connection = sqlite3.connect(name_of_database)
        self.create_table()

    @property
    def cursor(self) -> sqlite3.Cursor:
        try:
            return self.database.cursor()
        except Exception:
            raise Exception

    def commit(self) -> None:
        """Méthode qui applique tous les changements dans la bdd"""
        self.database.commit()

    def create_table(self):
        """Méthode qui créer la table T_Books"""
        sql_request = """CREATE TABLE IF NOT EXISTS "T_Books" (
	    "pk_b_id"	INTEGER NOT NULL,
	    "b_title"	TEXT UNIQUE,
	    "b_cover"	TEXT,
	    "b_authors"	TEXT,
	    "b_status"	TEXT,
	    "b_types"	TEXT,
	    "b_pages"	INTEGER,
	    "b_isbn"	TEXT UNIQUE,
	    "b_published_date"	TEXT,
	    "b_evaluation"	INTEGER,
	    PRIMARY KEY("pk_b_id" AUTOINCREMENT)
        );"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request)
            self.commit()

    def insert_a_book(self, new_book: BookModel):
        """
        Méthode qui permet d'insérer un nouveau livre dans la table T_Books
        :param new_book: Le nouveau à insérer dans la table T_Books
        """
        sql_request: str = "INSERT INTO T_Books(b_title, b_cover, b_authors, b_status, b_types, b_pages, b_isbn, b_published_date, b_evaluation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        new_book.cover = self.save_cover(new_book.title, new_book.cover)
        new_book = (new_book.title, new_book.cover, new_book.authors, new_book.status, new_book.types, new_book.pages, new_book.isbn, new_book.published_date, new_book.evaluation)
        try:
            with closing(self.cursor) as cursor:
                self.cursor.execute(
                        sql_request,
                        new_book)
                self.commit()
        except sqlite3.IntegrityError:
            print("[+] Erreur d'intégritée géré")

    def save_cover(self, book_name: str, path_cover_to_save):
        setting_storage = SettingStorage()
        picture_name_to_save = book_name.replace(" ", "_") + ".jpg"
        books_cover_folder: str = setting_storage.get_books_folder_cover_path("default")
        new_save_path_cover: str = f"{books_cover_folder}{picture_name_to_save}"
        if path_cover_to_save == "":
            return ""
        if "books.google.com" in path_cover_to_save:
            try:
                with open(new_save_path_cover, "bw") as file:
                    file.write(requests.get(path_cover_to_save).content)
            except FileNotFoundError:
                os.mkdir(books_cover_folder)
                with open(new_save_path_cover, "bw") as file:
                    file.write(requests.get(path_cover_to_save).content)
        else:
            try:
                shutil.copyfile(path_cover_to_save, new_save_path_cover)
            except shutil.SameFileError as e:
                print(e)
        return new_save_path_cover

    def get_all_books(self) -> list[BookModel]:
        """
        Méthode qui permet de récupérer tous les livres de la table T_Books
        :return: La liste de tous les livres.
        """
        sql_request: str = """SELECT * FROM T_Books"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request)
            result_of_the_request.row_factory = lambda cursor, row: BookModel(
                id=row[0],
                title=row[1],
                cover=row[2],
                authors=row[3],
                status=row[4],
                types=row[5],
                pages=row[6],
                isbn=row[7],
                published_date=row[8],
                evaluation=row[9]
            )
            return result_of_the_request.fetchall()

    def get_ten_last_books(self) -> list[BookModel]:
        """
        Méthode qui permet de récupérer seulement les 10 derniers livres de la table T_Books
        :return: La liste des dixs derniers livres
        """
        sql_request: str = """SELECT * FROM T_Books order by rowid desc limit 10"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request)
            result_of_the_request.row_factory = lambda cursor, row: BookModel(
                id=row[0],
                title=row[1],
                cover=row[2],
                authors=row[3],
                status=row[4],
                types=row[5],
                pages=row[6],
                isbn=row[7],
                published_date=row[8],
                evaluation=row[9]
            )
            return result_of_the_request.fetchall()

    def get_books_thanks_to_a_search(self, search: str) -> list[BookModel]: 
        """
        Méthode qui permet de récupérer tous les livres qui correspondes à la recherche de l'utilisateur
        :param search: le texte de recherche de l'utilisateur
        :return: La liste de livre trouvés
        """
        search = f"%{search}%"
        sql_request: str = """SELECT * FROM T_Books WHERE (b_title LIKE ?) OR (b_authors LIKE ?) order by rowid desc"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [search, search])
            result_of_the_request.row_factory = lambda cursor, row: BookModel(
                id=row[0],
                title=row[1],
                cover=row[2],
                authors=row[3],
                status=row[4],
                types=row[5],
                pages=row[6],
                isbn=row[7],
                published_date=row[8],
                evaluation=row[9]
            )
            return result_of_the_request.fetchall()

    def delete_a_book(self, book_to_delete: BookModel):
        """
        Méthode qui permet de supprimer un livre de la table T_Books
        :param book_to_delete: Le livre à supprimer
        :return: 
        """
        sql_request: str = """DELETE FROM T_Books WHERE pk_b_id = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [book_to_delete.id])
            self.commit()

    def delete_cover_file_associate_to_book_to_delete(self, book_to_delete: BookModel):
        """Méthode qui permet de supprimer la couverture associé au livre que l'on souhaite supprimer"""
        if book_to_delete.cover != "":
            os.remove(book_to_delete.cover)

    def update_book(self, old_book: BookModel, new_book: BookModel):
        """Permet de mettre un livre à jour"""
        new_book.cover = self.update_book_cover(old_book=old_book, new_book=new_book)
        sql_request: str = """
        UPDATE T_Books SET b_title = ?, 
        b_cover = ?, 
        b_authors = ?,  
        b_status = ?,
        b_types = ?,
        b_pages = ?,
        b_isbn = ?,
        b_published_date = ?,
        b_evaluation = ?
        WHERE pk_b_id = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [
                new_book.title,
                new_book.cover,
                new_book.authors,
                new_book.status,
                new_book.types,
                new_book.pages,
                new_book.isbn,
                new_book.published_date,
                new_book.evaluation,
                old_book.id                                                 
            ])
            self.commit()

    def update_book_cover(self, old_book, new_book):
        """Méthode qui permet de mettre à jour la couverture d'un livre"""
        if old_book.cover != new_book.cover and old_book.title == new_book.title:
            print("Premier cas")
            self.delete_cover_file_associate_to_book_to_delete(old_book)
            return self.save_cover(new_book.title, new_book.cover)
        elif old_book.cover != new_book.cover and old_book.title != new_book.title:
            print("Deuxième cas")
            self.delete_cover_file_associate_to_book_to_delete(old_book)
            return self.save_cover(new_book.title, new_book.cover)
        elif old_book.cover == new_book.cover and old_book.title != new_book.title:
            print("Troisème cas")
            new_cover = self.save_cover(new_book.title, new_book.cover)
            self.delete_cover_file_associate_to_book_to_delete(old_book)
            return new_cover
        else:
            return old_book.cover
        
    def get_number_of_books(self):
        """Méthode qui permet de renvoyer le nombre totale de livres"""
        sql_request: str = """SELECT COUNT(*) FROM T_Books"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request)
            return result_of_the_request.fetchone()[0]


class BookApi():
    """Classe qui permet de gérer le côté backend api des livres"""
    def __init__(self):
        """BookApi constructeur"""
        # Ma liste de livre que je vais créer grâce au livre réupérer depuis l'api
        self.books_get_with_api: list[BookModel] = []

    @staticmethod
    def test_connexion_to_api() -> bool:
        """Méthode qqi permet de tester la connexion vers l'api"""
        url_api: str = f"https://www.googleapis.com/books/v1/volumes?q=test&maxResults=3&key" \
                       f"=AIzaSyBZESW5evO0JkTqVTNS8xYzfWFwD8mNqpI"
        try:
            requests.get(url_api)
        except requests.ConnectionError as ex:
            return False
        return True

    def get_json_data_from_url(self, search_text: str) -> Any:
        """
        Méthode qui va permettre de récupérer les données json grâce à une recherche(celle de l'utilisateur qui recherche un livre)
        :param search_text: Le texte qui permet de rechercher des livres spécifiques
        :return data_json: Les données json récupérer depuis la requête
        """
        url_api: str = f"https://www.googleapis.com/books/v1/volumes?q={search_text}&maxResults=20&key" \
                       f"=AIzaSyBZESW5evO0JkTqVTNS8xYzfWFwD8mNqpI"
        res = Response = requests.get(url_api)
        # Je transforme ma réponse en string au format objet(json)
        data_json = res.json()
        return data_json       

    def construct_list_books(self, data_json):
        """
        Méthode qui permet de construire ma liste de livres grâce aux données récupérer depuis l'api
        :param data_json: Données Json
        """
        # Je vide la liste de livre à chaque construction d'une nouvelle liste c'est à dire une nouvelle recherche.
        self.books_get_with_api.clear()
        for item in data_json['items']:
            published_date: str = ""
            title: str = ""
            cover: str = ""
            pages: int = 0
            isbn: str = ""
            authors: str = ""
            # Je gère les différentes erreurs au cas ou des données depuis l'api serait inexistantes
            try:
                title = item['volumeInfo']['title']
            except KeyError:
                print("[!] Erreur aucun titre trouvé !")
            try:
                cover = item['volumeInfo']['imageLinks']['smallThumbnail']
            except KeyError:
                print("[!] Erreur aucun couverture trouvé")
            try:
                pages = int(item['volumeInfo']['pageCount'])
            except:
                print("[!] Erreur aucun nombre de pages trouvées !")
            try:
                isbn = item['volumeInfo']["industryIdentifiers"][0]['identifier']
            except:
                print("[!] Erreur aucun isbn trouvé !")
            try:
                published_date = item['volumeInfo']['publishedDate']
            except KeyError:
                print("[!] Erreur aucune date de publication trouvé !")
            try:
                for author in item['volumeInfo']['authors']:
                    if len(item['volumeInfo']['authors']) != 1:
                        authors += f"{author}, "
                    else:
                        authors += f"{author}"
            except KeyError:
                print("[!] Erreur aucun auteur trouvé !")
            new_book: BookModel = BookModel(title=title, cover=cover, authors=authors,
                                            pages=pages, isbn=isbn, published_date=published_date, types="")
            self.books_get_with_api.append(new_book)