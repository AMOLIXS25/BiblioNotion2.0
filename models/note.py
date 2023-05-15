from contextlib import closing
from dataclasses import dataclass, field
import sqlite3

from models.book import BookModel

from datetime import date

@dataclass
class NoteModel:
    """Note classe model"""
    title: str
    content: str
    date: str = field(default=date.today().strftime("%d/%m/%Y"))
    id: int = field(default=-1)

class NoteStorage:
    """Classe qui permet d'éffectuer des actions sur le modèle note"""
    def __init__(self) -> None:
        """NoteStorage constructeur"""
        self.database: sqlite3.Connection = sqlite3.connect("data.db")
        self.create_table()

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.database.cursor()

    def create_table(self):
        """Méthode qui créer la table Note si elle n'existe pas"""
        pass

    def commit(self) -> None:
        """Méthode qui applique tous les changements dans la bdd"""
        self.database.commit()

    def get_ten_last_notes(self) -> list[NoteModel]:
        """
        Méthode qui permet de récupérer seulement les 10 dernières note de la table T_Notes
        :return: La liste des dixs dernières notes
        """
        sql_request: str = """SELECT * FROM T_Notes order by rowid desc limit 10"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request)
            result_of_the_request.row_factory = lambda cursor, row: NoteModel(
                id=row[0],
                title=row[1],
                content=row[2],
                date=row[3]
            )
            return result_of_the_request.fetchall()
        
    def get_book_associate_to_a_note(self, note_id: int):
        """Méthode qui permet de récupérer le livre associé à une note"""
        sql_request: str = """
        SELECT pk_b_id, b_title, b_cover, b_authors, b_status, b_types, b_pages, b_isbn,
        b_published_date, b_evaluation from T_Notes INNER JOIN T_Books ON T_Notes.fk_n_book = T_Books.pk_b_id where pk_n_id = ?
        """
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [note_id])
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
            return result_of_the_request.fetchone()
        
    def get_notes_thanks_to_a_search(self, search: str): 
        """Méthode qui permet de rechercher des notes grâce à une recherche"""
        search = f"%{search}%"
        sql_request: str = """
        SELECT pk_n_id, n_title, n_content, n_date FROM T_Notes LEFT JOIN T_Books ON T_Notes.fk_n_book = T_Books.pk_b_id WHERE (n_title LIKE ?) OR 
        (n_content LIKE ?) OR (n_date LIKE ?) OR (b_title LIKE ?)
        """
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [search, search, search, search])
            result_of_the_request.row_factory = lambda cursor, row: NoteModel(
                id=row[0],
                title=row[1],
                content=row[2],
                date=row[3]
            )
            return result_of_the_request.fetchall()

    def insert_a_note(self, new_note: NoteModel, book_id: BookModel = -1):
        """
        Méthode qui permet d'insérer une nouvelle note dans la table T_Notes
        :param new_note: La nouvelle note à insérer dans la table T_Notes
        :param book: Le livre là ou il faut insérer la note
        """
        sql_request: str = """INSERT INTO T_Notes(n_title, n_content, n_date, fk_n_book) VALUES (?, ?, ?, ?)"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [new_note.title, new_note.content, new_note.date, book_id])
            self.commit()

    def update_note(self, old_note_id, new_note, new_book_id):
        """Méthode qui permet de mettre à jours une note"""
        sql_request = """UPDATE T_Notes SET n_title = ?, n_content = ?, fk_n_book = ? WHERE pk_n_id = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [
                new_note.title,
                new_note.content,
                new_book_id,
                old_note_id
            ])
            self.commit()
        
    def delete_a_note(self, note_id):
        """Méthode qui permet de supprimer une note"""
        sql_request: str = """DELETE FROM T_Notes WHERE pk_n_id = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [note_id])
            self.commit()

    def get_number_of_notes_associate_to_the_books(self, book_id):
        """Méthode qui permet de récupérer le nombre de notes associées à un livre"""
        sql_request: str = """SELECT COUNT(*) FROM T_Notes LEFT JOIN T_Books ON T_Notes.fk_n_book = T_Books.pk_b_id WHERE pk_b_id = ?"""
        with closing(self.cursor) as cursor:
            res = cursor.execute(sql_request, [book_id])
            return res.fetchone()[0]
        
    def get_all_notes_associate_to_a_book(self, book_id):
        """Méthode qui permet de récupérer toutes les notes associé à un livre"""
        sql_request: str = """SELECT pk_n_id, n_title, n_content, n_date FROM T_Notes LEFT JOIN T_Books ON T_Notes.fk_n_book = T_Books.pk_b_id WHERE pk_b_id = ?"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [book_id])
            result_of_the_request.row_factory = lambda cursor, row: NoteModel(
                id=row[0],
                title=row[1],
                content=row[2],
                date=row[3]
            )
            return result_of_the_request.fetchall()