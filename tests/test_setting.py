from contextlib import closing
from os.path import exists
import sqlite3

import pytest
from models.setting import Setting, SettingStorage


class TestSetting:
    """TestSetting classe"""
    def test_setting_constructor_with_all_parameters(self):
        """Méthode qui permet de tester le constructeur de la classe setting en passant tous les paramètres"""
        setting = Setting(
            name="default",
            export_pdf_note_path="./",
            export_txt_note_path="./",
            display_popup_no_connection=False,
            books_cover_folder_path="./",
            theme="Purple"
        )
        assert(
            setting.name == "default" and
            setting.export_pdf_note_path == "./" and
            setting.export_txt_note_path == "./" and
            setting.display_popup_no_connection == False and
            setting.books_cover_folder_path == "./" and
            setting.theme == "Purple"
        )

    def test_setting_constructor_with_default_parameters(self):
        """Méthode qui test le constructeur de la classe setting avec les paramètres par défaut"""
        setting = Setting("default")
        assert(
            setting.name == "default" and
            setting.export_pdf_note_path == "./export/pdf/" and
            setting.export_txt_note_path == "./export/txt/" and
            setting.display_popup_no_connection == True and
            setting.books_cover_folder_path == "./books_cover/" and
            setting.theme == "Défaut"
        )


class TestSettingStorage:
    """Classe qui permet de tester la classe SettingStorage"""
    @pytest.fixture
    def setting_storage(self):
        setting_storage: SettingStorage = SettingStorage("test.db")
        yield setting_storage

    def test_if_connection_to_the_database_is_etablished(self):
        """Méthode qui permet de tester si la connection à la base de  données s'étable correctement"""
        assert exists("test.db") == True

    def test_setting_table_has_been_correctly_created(self, setting_storage):
        """Méthode qui permet de vérifier si la table setting a correctement été créer"""
        sql_request = """SELECT COUNT(*) FROM T_Settings"""
        try:
            with closing(setting_storage.cursor) as cursor:
                res = cursor.execute(sql_request)
        except sqlite3.OperationalError:
            # Je relève une erreur de test si il y a une operationnal error
            assert False
    
    def test_automatically_first_insert(self, setting_storage):
        """Méthode qui permet de tester l'insert automatique du premier setting"""
        sql_request = """SELECT * FROM T_Settings WHERE s_name = ?"""
        with closing(setting_storage.cursor) as cursor:
            res = cursor.execute(sql_request, ["default"])
            assert res.fetchone() != None
    
    def test_insert_another_setting(self, setting_storage):
        """Méthode qui va tester l'insertion d'un autre setting"""
        new_setting = Setting("New")
        setting_storage.insert_a_settings(new_setting)
        sql_request = """SELECT * FROM T_Settings WHERE s_name = ?"""
        with closing(setting_storage.cursor) as cursor: 
            res = cursor.execute(sql_request, ["New"])
            assert res.fetchone() != None

    def test_get_number_of_setting(self, setting_storage):
        """Méthode qui test la méthode pour renvoyer le bon nombre de setting"""
        assert setting_storage.get_number_of_settings() > 0

    def test_get_display_popup_no_connection(self, setting_storage):
        """Méthode qui test la méthode qui renvoie si il faut afficher ou non la popup de non connection"""
        assert setting_storage.get_display_popup_no_connection("default") == True

    def test_get_books_folder_cover_path(self, setting_storage):
        """Méthode qui test la méthode qui renvoie le dossier des couverture de livre"""
        assert setting_storage.get_books_folder_cover_path("default") == "./books_cover/"

    def test_get_theme(self, setting_storage):
        """Méthode qui permet de tester la méthode pour récupérer le theme"""
        assert setting_storage.get_theme("default") == "Défaut"

    def test_get_export_pdf_note_path(self, setting_storage):
        """Méthode qui test la méthode qui renvoie le dossier d'export des notes en pdf"""
        assert setting_storage.get_export_pdf_note_path("default") == "./export/pdf/"

    def test_get_export_txt_note_path(self, setting_storage):
        """Méthode qui test la méthode qui renvoie le chemin du dossier d'export des notes en txt"""
        assert setting_storage.get_export_txt_note_path("default") == "./export/txt/"

    def test_update_display_popup_no_connection(self, setting_storage):
        """Méthode qui test la méthode pour mettre à jour le boolean de la popup"""
        setting_storage.update_display_popup_no_connection("New", False)
        assert setting_storage.get_display_popup_no_connection("New") == False