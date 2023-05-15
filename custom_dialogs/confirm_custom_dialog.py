from PySide6.QtWidgets import QDialog

from generate_uis.confirm_reset_settings_dialog_ui import Ui_ConfirmResetSettingsDialog



class ConfirmCustomDialog(QDialog, Ui_ConfirmResetSettingsDialog):
    """ConfirmResetSettingsDialog classe"""
    def __init__(self, title:str, message: str):
        super().__init__()
        self._is_yes = False
        self.setupUi(self)
        self.connect_signals_to_slots()
        self.setWindowTitle(title)
        self.label.setText(message)

    @property
    def is_yes(self):
        return self._is_yes

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux à leurs slots"""
        self.yes_button.clicked.connect(self.on_yes_button_clicked)
        self.no_button.clicked.connect(self.close)

    def on_yes_button_clicked(self):
        """Méthode qui permet de gérer le signal du button yes"""
        self._is_yes = True
        self.close()