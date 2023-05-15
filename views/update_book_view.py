import sqlite3
import re
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QImage, QPixmap
from PySide6 import QtCore
import requests
from custom_dialogs.confirm_update_dialog import ConfirmUpdateDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog

from generate_uis.update_book_view_ui import Ui_UpdateBookWindow
from models.book import BookModel, BookStorage
from models.note import NoteStorage

class UpdateBookView(QMainWindow, Ui_UpdateBookWindow):
    def __init__(self, parent=None, library_note_view=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("")
        self.book_to_update: BookModel
        self.path_cover_to_save: str
        self.connect_signals_to_slots()
        self.book_storage = BookStorage()
        self.library_note_view = library_note_view
        self.note_storage = NoteStorage()
        self.parent = parent

    @property
    def book_to_update(self):
        return self._book_to_update
    
    @book_to_update.setter
    def book_to_update(self, value):
        self._book_to_update = value

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter tous les signaux à leurs slots"""
        self.save_update_button.clicked.connect(self.on_save_update_button_clicked)
        self.book_cover_label.mousePressEvent = self.on_book_cover_label_mouse_pressed

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
        elif len(self.title_line_edit.text()) > 25:
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
        elif not self.isbn_line_edit.text().isdigit():
            error_message += "•Veuillez renté un isbn valide \n"
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

    def fill_fields(self):
        """Méthode qui permet de préremplir les champs avec le livre déjà existant"""
        self.set_cover(self.book_to_update.cover)
        self.title_line_edit.setText(self.book_to_update.title)
        self.author_line_edit.setText(self.book_to_update.authors)
        # Définir la combobox
        self.status_combo_box.setCurrentText(self.book_to_update.status)
        self.page_number_spin_box.setValue(self.book_to_update.pages)
        self.isbn_line_edit.setText(self.book_to_update.isbn)
        self.published_date_line_edit.setText(self.book_to_update.published_date)
        self.eval_spin_box.setValue(self.book_to_update.evaluation)

    def appliquate_error_style(self, line_edit):
        line_edit.setStyleSheet("""
            border: 1px solid #DE5E5E;
            border-radius: 3px;
        """)

    def on_save_update_button_clicked(self):
        """Méthode qui permet de gérer le signal pour le button sauvegarder les modifications"""
        if self.check_validity_fields():
            try:
                new_book_to_insert = BookModel(
                    title=self.title_line_edit.text(),
                    cover=self.path_cover_to_save,
                    authors=self.author_line_edit.text(),
                    pages=self.page_number_spin_box.value(),
                    isbn=self.isbn_line_edit.text(),
                    published_date=self.published_date_line_edit.text(),
                    evaluation=self.eval_spin_box.value(),
                    status=str(self.status_combo_box.currentText())
                )
                self.close()
                confirm_update_dialog = ConfirmUpdateDialog(self.book_to_update, new_book_to_insert, "Le livre à été modfié avec success !")
                confirm_update_dialog.exec()
                if not confirm_update_dialog.is_yes_to_update:
                    return
                self.book_storage.update_book(old_book=self.book_to_update, new_book=new_book_to_insert)
                self.parent.construct_list_widget(self.book_storage.get_ten_last_books())
                self.library_note_view.construct_list_widget(self.note_storage.get_ten_last_notes())
            except sqlite3.IntegrityError:
                custom_message_dialog = CustomMessageDialog("Erreur", "Le livre que vous essayez de sauvegarder fait déjà partie de votre bibliothèque !", self)
                custom_message_dialog.exec()

    def on_book_cover_label_mouse_pressed(self, event):
        """Méthode qui permet de gérer le click du button pour définir une couverture au livre à enregistrer"""
        book_cover_name = QFileDialog.getOpenFileName(self, "Choisir une couverture", ".", "Tous les fichiers(*);;Fichiers png(*).png;;Fichiers jpg(*).jpg")
        # Je m'assure de ne jammais définir d'image vide, je définis l'image seulement si une image est sélectionner !
        if book_cover_name[0] != "":
            self.set_cover(book_cover_name[0])