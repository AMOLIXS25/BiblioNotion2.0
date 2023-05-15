from PySide6.QtWidgets import QMainWindow
from custom_dialogs.confirm_update_dialog import ConfirmUpdateDialog

from generate_uis.update_note_view_ui import Ui_UpdateNoteWindow
from models.book import BookModel
from models.note import NoteModel, NoteStorage
from views.select_book_to_update_note import SelectBookToUpdateNote


class UpdateNoteView(QMainWindow, Ui_UpdateNoteWindow):
    """UpdateNoteView classe"""
    def __init__(self, note_model: NoteModel, parent=None):
        """UpdateNoteView constructeur"""
        super().__init__()
        self.setupUi(self)
        self.note_model = note_model
        self.fill_fields()
        self.note_storage = NoteStorage()
        self.book_associate_to_note = self.note_storage.get_book_associate_to_a_note(self.note_model.id)
        self._book_selected_to_update: BookModel = None
        self.parent = parent
        self.select_book_to_update_note = SelectBookToUpdateNote(parent=self)
        self.connect_signals_to_slots()

    @property
    def book_selected_to_update(self):
        return self._book_selected_to_update
    
    @book_selected_to_update.setter
    def book_selected_to_update(self, value):
        self._book_selected_to_update = value

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter mes signaux à mes slots"""
        self.quit_button.clicked.connect(self.on_quit_button_clicked)
        self.save_button.clicked.connect(self.on_save_button_clicked)
        self.move_note_to_another_book_button.clicked.connect(self.on_move_note_to_another_book_button_clicked)

    def fill_fields(self):
        """Permet de préremplir les champs"""
        self.title_line_edit.setText(self.note_model.title)
        self.content_plaintext_edit.setPlainText(self.note_model.content)

    def check_validity_fields(self):
        """Méthode qui permet de vérifier si les champs entrée sont valide ou non"""
        error_message: str = ""
        fields_validate: bool = True
        if len(self.title_line_edit.text()) == 0:
            error_message += "Veuillez rentrée le titre de la note. \n"
            fields_validate = False
            self.appliquate_error_style(self.title_line_edit)
        elif len(self.title_line_edit.text()) > 25:
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

    ############################
    # SLOTS
    ############################

    def on_quit_button_clicked(self):
        """Méthode qui gère le signal du button quitter"""
        self.close()

    def on_save_button_clicked(self):
        """Méthode qui permet de gérer le signal du button pour sauvegarder les modifications"""
        new_title = self.title_line_edit.text()
        new_content = self.content_plaintext_edit.toPlainText()
        new_note = NoteModel(title=new_title, content=new_content)
        if self.check_validity_fields():
            confirm_update_dialog = ConfirmUpdateDialog(self.note_model, new_note, "Souhaitez-vous réelement appliqué les modifications ?")
            confirm_update_dialog.exec()
            if not confirm_update_dialog.is_yes_to_update:
                return
            self.close()
            try:
                if self.book_selected_to_update.id != self.book_associate_to_note:
                    new_book_id = self.book_selected_to_update.id
            except AttributeError:
                if self.book_associate_to_note != None:
                    new_book_id = self.book_associate_to_note.id
                else:
                    new_book_id = -1
            self.note_storage.update_note(self.note_model.id, new_note, new_book_id)
            self.parent.construct_list_widget(self.note_storage.get_ten_last_notes())
    
    def on_move_note_to_another_book_button_clicked(self):
        """Méthode qui permet de gérer le signal du clique du button afin de sélectionner un nouveau livre"""
        if not self.select_book_to_update_note.isVisible():
            self.select_book_to_update_note.show()