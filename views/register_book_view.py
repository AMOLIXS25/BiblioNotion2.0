import os
import re
import sqlite3
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QImage, QPixmap

from PySide6 import QtCore

import requests

import ebooklib
from ebooklib import epub

import shutil
from custom_dialogs.confirm_register_dialog import ConfirmRegisterDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog

from generate_uis.register_book_view_ui import Ui_RegisterWindow
from models.book import BookApi, BookModel, BookStorage
from views.api_book_view import ApiBookView


class RegisterBookView(QMainWindow, Ui_RegisterWindow):
    """RegisterBookView classe"""
    def __init__(self, parent=None):
        """RegisterBookView classe constructeur"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("")
        self.set_cover()
        self.book_api_view = ApiBookView(parent=self)
        self.connect_signals_to_slots()
        self.path_cover_to_save: str
        self.book_storage = BookStorage()
        self.parent = parent

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter tous les signaux à leurs slots"""
        self.use_api_button.clicked.connect(self.on_use_api_button_clicked)
        self.book_cover_label.mousePressEvent = self.on_book_cover_label_mouse_pressed
        self.register_a_new_book_button.clicked.connect(self.on_register_a_new_book_button_clicked)
        self.import_book_button.clicked.connect(self.on_import_book_button_clicked)

    def fill_fields(self, cover_path: str = "", title: str = "", authors: str = "", pages_number: int = 0, isbn: str = "", published_date: str = ""):
        """Permet de remplir les champs du formulaire"""
        self.set_cover(cover_path)
        self.title_line_edit.setText(title)
        self.author_line_edit.setText(authors)
        self.page_number_spin_box.setValue(pages_number)
        self.published_date_line_edit.setText(published_date)
        self.isbn_line_edit.setText(isbn)

    def check_validity_fields(self):
        """Méthode qui permet de vérifier si les champs entrée sont valide ou non"""
        regex_date_fr = "^[0-9]{1,2}\\-[0-9]{1,2}\\-[0-9]{4}$"
        regex_date_eng = "^[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}$"
        regex_only_year = "^[0-9]{4}"
        date_regex_fr_validate: bool = True
        date_regex_eng_validate: bool = True
        date_regex_only_year_validate: bool = True
        error_message: str = ""
        fields_validate: bool = True
        if len(self.title_line_edit.text()) == 0:
            error_message += "•Veuillez rentrée le titre du livre. \n"
            fields_validate = False
            self.appliquate_error_style(self.title_line_edit)
        elif len(self.title_line_edit.text()) > 100:
            error_message += "•Titre du livre trop long. \n"
            fields_validate = False
            self.appliquate_error_style(self.title_line_edit)
        else:
            self.title_line_edit.setStyleSheet("")
        if len(self.author_line_edit.text()) == 0:
            error_message += "•Veuillez rentré le(s) auteur(s) du livre \n"
            fields_validate = False
            self.appliquate_error_style(self.author_line_edit)
        else:
            self.author_line_edit.setStyleSheet("")
        if len(self.isbn_line_edit.text()) == 0:
            error_message += "•Veuillez renté l'isbn du livre \n"
            fields_validate = False
            self.appliquate_error_style(self.isbn_line_edit)
        else:
            self.isbn_line_edit.setStyleSheet("")
        if len(self.published_date_line_edit.text()) == 0:
            error_message += "•Veuillez rentré la date de publication du livre \n"
            fields_validate = False
            self.appliquate_error_style(self.published_date_line_edit)
        else:
            self.published_date_line_edit.setStyleSheet("")
        if len(re.findall(regex_date_fr, self.published_date_line_edit.text())) == 0:
            date_regex_fr_validate = False
        if len(re.findall(regex_date_eng, self.published_date_line_edit.text())) == 0:
            date_regex_eng_validate = False
        if len(re.findall(regex_only_year, self.published_date_line_edit.text())) == 0:
            date_regex_only_year_validate = False
        if date_regex_fr_validate != True and date_regex_eng_validate != True and date_regex_only_year_validate != True:
            error_message += "•Veuillez rentré une date de publication du livre valide \n"
            self.appliquate_error_style(self.published_date_line_edit)
            fields_validate = False
        else:
            self.published_date_line_edit.setStyleSheet("")
        self.error_label.setText(error_message)
        if len(self.error_label.text()) != 0:
            self.error_label.show()
        else:
            self.error_label.hide()
        return fields_validate
    
    def appliquate_error_style(self, line_edit):
        line_edit.setStyleSheet("""
            border: 1px solid #DE5E5E;
            border-radius: 3px;
        """)

    def set_cover(self, cover: str = ""):
        """Méthode qui permet de définir la couverture"""
        pixmap: QPixmap
        if cover == "":
            pixmap = QPixmap(u":/images/images/no_cover.jpg")
        elif "books.google.com" in cover:
            cover_image = QImage()
            # Je construis mon image à partir des données de l'image récupérer via l'url internet.
            cover_image.loadFromData(requests.get(cover).content)
            pixmap = QPixmap(cover_image)
        else:
            pixmap = QPixmap(cover)
        # Je redimensionne mon image tous en gardant le ratio de mon image.
        self.path_cover_to_save = cover
        pixmap = pixmap.scaled(200, 120, QtCore.Qt.KeepAspectRatio)
        self.book_cover_label.setPixmap(pixmap)

    #########################
    # SLOTS
    #########################

    def on_book_cover_label_mouse_pressed(self, event):
        """Méthode qui permet de gérer le click du button pour définir une couverture au livre à enregistrer"""
        book_cover_name = QFileDialog.getOpenFileName(self, "Choisir une couverture", ".", "Tous les fichiers(*);;Fichiers png(*).png;;Fichiers jpg(*).jpg")
        # Je m'assure de ne jammais définir d'image vide, je définis l'image seulement si une image est sélectionner !
        if book_cover_name[0] != "":
            self.set_cover(book_cover_name[0])
    
    def on_use_api_button_clicked(self):
        """Méthode qui permet de gérer le click du button utiliser l'api"""
        if BookApi.test_connexion_to_api():
            if not self.book_api_view.isVisible():
                self.book_api_view.show()
        else:
            custom_message_dialog = CustomMessageDialog("Erreur internet", "Impossible d'acéder à cette fonctionnalité sans connexion internet !")
            custom_message_dialog.exec()

    def on_register_a_new_book_button_clicked(self):
        """Méthode qui permet de gérer l'événement de click du button enregistrer un nouveau livre"""
        book_to_register = BookModel(
                title=self.title_line_edit.text(),
                cover=self.path_cover_to_save,
                authors=self.author_line_edit.text(),
                pages=self.page_number_spin_box.value(),
                isbn=self.isbn_line_edit.text(),
                published_date=self.published_date_line_edit.text(),
                evaluation=self.eval_spin_box.value(),
                status=str(self.status_combo_box.currentText())
        )
        if self.check_validity_fields():
            self.book_storage.database = sqlite3.connect("data.db")
            try:
                self.book_storage.insert_a_book(book_to_register)
                confirm_register_book_dialog = ConfirmRegisterDialog(book_to_register, "Le livre suivant à bien été enregistré dans votre bibliothèque : ")
                confirm_register_book_dialog.exec()
                self.parent.construct_list_widget(self.book_storage.get_ten_last_books())
            except sqlite3.IntegrityError:
                self.book_storage.database.close()
                custom_message_dialog = CustomMessageDialog("Erreur", "Le livre que vous essayez d'enregistrer fait déjà partie de votre bibliothèque !", self)
                custom_message_dialog.exec()

    def on_import_book_button_clicked(self):
        """Méthode qui permet gérer le signal du button import"""
        try:
            epub_file_name = QFileDialog.getOpenFileName(self, "Choisir un livre(epub)")
            book = epub.read_epub(epub_file_name[0])
            title = book.get_metadata('DC', 'title')[0][0]
            isbn = book.get_metadata('DC', 'identifier')[0][0]
            cover_image_epub_path = "./cover_tmp.jpg"
            images = book.get_items_of_type(ebooklib.ITEM_IMAGE)
            for image in images:
                with open(cover_image_epub_path, "bw") as file:
                    file.write(image.get_content())
                    break
            number_of_pages = 0
            for item in book.get_items():
                number_of_pages += 1
            try:
                published_date = book.get_metadata('DC', 'date')[0][0]
                x = published_date.split("T")
                published_date = x[0]
            except IndexError:
                published_date = "00-00-0000"
            author = book.get_metadata('DC', 'creator')[0][0]
            self.fill_fields(
                title=title,
                isbn=isbn,
                authors=author,
                published_date=published_date,
                pages_number=number_of_pages,
                cover_path=cover_image_epub_path,
            )
            self.path_cover_to_save = cover_image_epub_path
        except FileNotFoundError:
            return
