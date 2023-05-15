from PySide6.QtWidgets import QDialog

from generate_uis.confirm_auto_save_file_dialog_ui import Ui_ConfirmAutoSaveFIleDialog


class ConfirmAutoSaveFileDialog(QDialog, Ui_ConfirmAutoSaveFIleDialog):
    def __init__(self, message: str):
        super().__init__()
        self.setupUi(self)
        self._is_yes: bool = None
        self.message_label.setText(message)
        self.connect_signals_to_slots()

    @property
    def is_yes(self):
        return self._is_yes

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux à leurs slots"""
        self.yes_button.clicked.connect(self.on_yes_button_clicked)
        self.no_button.clicked.connect(self.on_no_button_clicked)

    def on_yes_button_clicked(self):
        """Méthode qui permet de gérer le signal du button yes"""
        self._is_yes = True
        self.close()

    def on_no_button_clicked(self):
        """Méthode qui permet de gérer le signal du button no"""
        self._is_yes = False
        self.close()