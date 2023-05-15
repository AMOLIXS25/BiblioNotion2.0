
from PySide6.QtWidgets import QDialog

from custom_widgets.book_custom_widget import BookCustomWidget
from custom_widgets.note_custom_widget import NoteCustomWidget
from generate_uis.confirm_register_book_dialog_ui import Ui_ConfirmRegisterBookDialog


class ConfirmRegisterDialog(QDialog, Ui_ConfirmRegisterBookDialog):
    """Confirm Register Dialog"""
    def __init__(self, model, text: str, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        try:
            book_custom_widget: BookCustomWidget = BookCustomWidget(model)
            self.verticalLayout1.addWidget(book_custom_widget)
        except:
            note_custom_widget = NoteCustomWidget(model)
            self.verticalLayout1.addWidget(note_custom_widget)
        self.label.setText(text)
        self.ok_button.clicked.connect(self.on_ok_button_clicked)

    def on_ok_button_clicked(self):
        """Method that manage ok button clicked signal"""
        self.close()