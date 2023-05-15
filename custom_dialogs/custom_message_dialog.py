from PySide6.QtWidgets import QDialog

from generate_uis.custom_message_dialog_ui import Ui_CustomMessageDialog

class CustomMessageDialog(QDialog, Ui_CustomMessageDialog):
    def __init__(self, title: str, message: str, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.label.setText(message)
        self.setWindowTitle(title)
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Method that connect all signals to slots"""
        self.ok_button.clicked.connect(self.close)