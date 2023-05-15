import sqlite3
from PySide6.QtWidgets import QMainWindow, QFileDialog


from custom_dialogs.confirm_register_dialog import ConfirmRegisterDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog

from generate_uis.register_note_view_ui import Ui_RegisterNoteWindow
from models.book import BookModel
from models.note import NoteModel, NoteStorage

from datetime import date


class RegisterNoteView(QMainWindow, Ui_RegisterNoteWindow):
    """RegisterNoteView classe"""
    def __init__(self, parent=None):
        """RegisterNoteView constructeur"""
        super().__init__()
        self.setupUi(self)
        self._book_to_register_note: BookModel = None
        self.note_storage = NoteStorage()
        self.connect_signals_to_slots()
        self.parent = parent

    @property
    def book_to_register_note(self):
        return self._book_to_register_note
    
    @book_to_register_note.setter
    def book_to_register_note(self, value):
        self._book_to_register_note = value
        self.setWindowTitle(self._book_to_register_note.title)

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter tous les signaux à leurs slots"""
        self.register_button.clicked.connect(self.on_register_button_clicked)
        self.import_button.clicked.connect(self.on_import_button_clicked)
        self.quit_button.clicked.connect(self.on_quit_button_clicked)

    def check_validity_fields(self):
        """Méthode qui permet de vérifier si les champs entrée sont valide ou non"""
        error_message: str = ""
        fields_validate: bool = True
        if len(self.title_line_edit.text()) == 0:
            error_message += "Veuillez rentrée le titre de la note. \n"
            fields_validate = False
            self.appliquate_error_style(self.title_line_edit)
        elif len(self.title_line_edit.text()) > 100:
            error_message += "Titre de la note trop long. \n"
            fields_validate = False
            self.appliquate_error_style(self.title_line_edit)
        self.error_label.setText(error_message)
        if len(self.error_label.text()) != 0:
            self.error_label.show()
        else:
            self.title_line_edit.setStyleSheet("")
            self.error_label.hide()
        return fields_validate
    
    def appliquate_error_style(self, line_edit):
        line_edit.setStyleSheet("""
            border: 1px solid #DE5E5E;
            border-radius: 3px;
        """)

    def on_register_button_clicked(self):
        """Méthode qui permet de gérer le click du button enregistrer"""
        title_note = self.title_line_edit.text()
        content_note = self.content_text_edit.toPlainText()
        new_note_to_register = NoteModel(
            title=title_note,
            content=content_note,
        )
        if self.check_validity_fields():
            self.note_storage.database = sqlite3.connect("data.db")
            try:
                self.note_storage.insert_a_note(new_note_to_register, self._book_to_register_note.id)
                confirm_register_book_dialog = ConfirmRegisterDialog(new_note_to_register, "La note suivante à bien été enregistrée : ")
                confirm_register_book_dialog.exec()
                self.parent.construct_list_widget(self.note_storage.get_ten_last_notes())
            except sqlite3.IntegrityError:
                self.note_storage.database.close()
                custom_message_dialog = CustomMessageDialog("Erreur", "La note que vous essayez d'enregistrer fait déjà partie de votre bibliothèque de notes !")
                custom_message_dialog.exec()
            except AttributeError:
                try:
                    self.note_storage.insert_a_note(new_note_to_register)
                    confirm_register_book_dialog = ConfirmRegisterDialog(new_note_to_register, "La note suivante à bien été enregistrée : ")
                    confirm_register_book_dialog.exec()
                    self.parent.construct_list_widget(self.note_storage.get_ten_last_notes())
                except sqlite3.IntegrityError:
                    self.note_storage.database.close()
                    custom_message_dialog = CustomMessageDialog("Erreur", "La note que vous essayez d'enregistrer fait déjà partie de votre bibliothèque de notes !")
                    custom_message_dialog.exec()

    def on_quit_button_clicked(self):
        """Méthode qui permet de gérer le click du button fermer"""
        self.close()
        
    def on_import_button_clicked(self):
        """Méthode qui permet de gérer le click du button import"""
        try:
            note_file_name = QFileDialog.getOpenFileName(self, "Choisir une note")
            with open(note_file_name[0]) as f:
                self.content_text_edit.clear()
                self.content_text_edit.appendPlainText(f.read())
        except FileNotFoundError:
            return
