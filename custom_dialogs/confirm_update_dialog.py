from PySide6.QtWidgets import QDialog

from custom_widgets.book_custom_widget import BookCustomWidget
from custom_widgets.note_custom_widget import NoteCustomWidget
from generate_uis.confirm_update_dialog_ui import Ui_ConfirmUpdateDialog
from models.book import BookModel


class ConfirmUpdateDialog(QDialog, Ui_ConfirmUpdateDialog):
    """Confirm Register Book Dialog"""
    def __init__(self, old_model, new_model, message, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.label.setText(message)
        try:
            old_book_custom_widget: BookCustomWidget = BookCustomWidget(old_model)
            new_book_custom_widget: BookCustomWidget = BookCustomWidget(new_model)
            self.old_book_layout.addWidget(old_book_custom_widget)
            self.new_book_layout.addWidget(new_book_custom_widget)
        except:
            old_note_custom_widget: NoteCustomWidget = NoteCustomWidget(old_model)
            new_note_custom_widget: NoteCustomWidget = NoteCustomWidget(new_model)
            self.old_book_layout.addWidget(old_note_custom_widget)
            self.new_book_layout.addWidget(new_note_custom_widget)
        self.is_yes_to_update: bool = False
        self.connect_signals_to_slots()

    @property
    def is_yes_to_update(self) -> bool:
        return self._is_yes_to_update
    
    @is_yes_to_update.setter
    def is_yes_to_update(self, value):
        self._is_yes_to_update = value

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter tous les signaux à leurs slots"""
        self.confirm_button.clicked.connect(self.on_confirm_button_clicked)
        self.annul_button.clicked.connect(self.on_annul_button_clicked)

    def on_confirm_button_clicked(self):
        self.is_yes_to_update = True
        self.close()

    def on_annul_button_clicked(self):
        self.close()