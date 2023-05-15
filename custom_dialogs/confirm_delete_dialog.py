from PySide6.QtWidgets import QDialog, QLabel
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation, QPoint

from custom_widgets.book_custom_widget import BookCustomWidget
from custom_widgets.note_custom_widget import NoteCustomWidget
from generate_uis.confirm_delete_dialog_ui import Ui_ConfirmDeleteDialog

from res import res


class ConfirmDeleteDialog(QDialog, Ui_ConfirmDeleteDialog):
    """ConfirmDeleteDialog"""
    def __init__(self, title: str, model, message, parent=None):
        """
        ConfirmDeleteBookDialog's constructor
        Args:
            title (str): title of the dialog
            book_delete (BookModel): The book to delete
            parent (_type_, optional): The Dialog's parent. Defaults to None.
        """
        super().__init__(parent)
        try:
            custom = NoteCustomWidget(model)
        except AttributeError:
            custom = BookCustomWidget(model)
        self.setupUi(self)
        self.top_label.setText(message)
        self.horizontalLayout.addWidget(custom)
        self.setWindowTitle(title)
        self.is_yes_to_delete: bool = False
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Method that connect signals to slots"""
        self.yes_button.clicked.connect(self.on_yes_button_clicked)
        self.no_button.clicked.connect(self.on_no_button_clicked)

    def on_yes_button_clicked(self):
        """Method that manage yes button clicked signal"""
        self.is_yes_to_delete = True
        self.close()

    def on_no_button_clicked(self):
        """Method that manage no button clicked signal"""
        self.close()