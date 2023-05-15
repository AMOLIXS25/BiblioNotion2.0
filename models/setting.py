

from contextlib import closing
from dataclasses import dataclass, field
import sqlite3

@dataclass
class Setting:
    """Model de classe Setting"""
    name: str
    export_pdf_note_path: str = field(default="./export/pdf/")
    export_txt_note_path: str = field(default="./export/txt/")
    display_popup_no_connection: bool = field(default=True)
    books_cover_folder_path: str = field(default="./books_cover/")
    theme: str = field(default="Défaut")


class SettingStorage:
    """Classe qui permet de gérer le modèle Setting"""
    def __init__(self) -> None:
        self.database: sqlite3.Connection = sqlite3.connect("data.db")
        self.create_table()
        if self.get_number_of_settings() == 0:
            setting = Setting("default")
            self.insert_a_settings(setting)

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.database.cursor()

    def commit(self) -> None:
        """Méthode qui applique tous les changements dans la bdd"""
        self.database.commit()

    def create_table(self) -> None:
        """Méthode qui permet de créer de A à Z la table Setting"""
        sql_request: str = """CREATE TABLE IF NOT EXISTS "T_Settings" (
	        "pk_s_id"	INTEGER UNIQUE,
	        "s_name"	TEXT,
	        "s_books_folder_cover_path"	TEXT,
	        "s_theme"	TEXT,
	        "s_export_pdf_note_path"	TEXT,
	        "s_export_txt_note_path"	TEXT,
            "s_display_popup_no_connection"	INTEGER,
	        PRIMARY KEY("pk_s_id" AUTOINCREMENT));"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request)
            self.commit()

    def insert_a_settings(self, setting: Setting) -> None:
        """Insert a new setting in the database"""
        sql_request: str = """INSERT INTO T_Settings (s_name, s_books_folder_cover_path, s_theme, s_export_pdf_note_path, s_export_txt_note_path, s_display_popup_no_connection) VALUES (?, ?, ?, ?, ?, ?)"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [setting.name, setting.books_cover_folder_path, setting.theme, setting.export_pdf_note_path, setting.export_txt_note_path, setting.display_popup_no_connection])
            self.commit()

    def get_number_of_settings(self) -> int:
        """Méthode qui permet de renvoyer le nombre de settings enregistrer dans la table"""
        sql_request: str = """SELECT COUNT(*) FROM T_Settings"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request)
            return result_of_the_request.fetchone()[0]

    def get_display_popup_no_connection(self, name_of_setting: str) -> bool:
        """Méthode qui permet de renvoyer le boolean pour afficher ou non la popup du départ"""
        sql_request: str = """SELECT s_display_popup_no_connection FROM T_Settings WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [name_of_setting])
            return result_of_the_request.fetchone()[0]
        
    def get_books_folder_cover_path(self, name_of_setting: str):
        """Méthode qui permet de renvoyer le chemin ou placer la couverture des livres sauvegarder"""
        sql_request: str = """SELECT s_books_folder_cover_path FROM T_Settings WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [name_of_setting])
            return str(result_of_the_request.fetchone()[0])
        
    def get_theme(self, name_of_setting: str):
        """Méthode qui permet de renvoyer le theme actuel de l'application"""
        sql_request: str = """SELECT s_theme FROM T_Settings WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [name_of_setting])
            return result_of_the_request.fetchone()[0]
        
    def get_export_pdf_note_path(self, name_of_setting: str):
        """Méthode qui permet de renvoyer le chemin du dossier pour l'export des note actuel de l'application en pdf"""
        sql_request: str = """SELECT s_export_pdf_note_path FROM T_Settings WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [name_of_setting])
            return result_of_the_request.fetchone()[0]
        
    def get_export_txt_note_path(self, name_of_setting: str):
        """Méthode qui permet de renvoyer le chemin du dossier pour l'export des notes actuel de l'application en text"""
        sql_request: str = """SELECT s_export_txt_note_path FROM T_Settings WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [name_of_setting])
            return result_of_the_request.fetchone()[0]

    def get_all_settings(self, name_of_setting: str):
        """Méthode qui permet de renvoyer tous les settings de la db"""
        sql_request: str = """SELECT * FROM T_Settings WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            result_of_the_request = cursor.execute(sql_request, [name_of_setting])
            result_of_the_request.row_factory = lambda cursor, row: Setting(
                name=row[1],
                books_cover_folder_path=row[2],
                theme=row[3],
                export_pdf_note_path=row[4],
                export_txt_note_path=row[5],
                display_popup_no_connection=row[6]
            )
            return result_of_the_request.fetchone()

    def update_display_popup_no_connection(self, name_of_setting: str, update_display_popup_no_connection: bool) -> bool:
        """Méthode qui permet de mettre à jour le boolean pour l'affichage ou non de la popup de non connexion"""
        sql_request: str = """UPDATE T_Settings SET s_display_popup_no_connection = ? WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [update_display_popup_no_connection, name_of_setting])
            self.commit()

    def update_all_settings(self, name_of_setting_to_update: str, new_setting: Setting):
        """Méthode qui permet de mettre à jour l'enregistrement du setting dans la db"""
        sql_request: str = """UPDATE T_Settings SET s_theme = ?, s_export_pdf_note_path = ?, s_export_txt_note_path = ?, s_books_folder_cover_path = ? WHERE s_name = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql_request, [new_setting.theme, new_setting.export_pdf_note_path, new_setting.export_txt_note_path, new_setting.books_cover_folder_path, name_of_setting_to_update])
            self.commit()