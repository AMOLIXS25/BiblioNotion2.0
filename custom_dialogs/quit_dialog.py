import sys

from PySide6.QtWidgets import QDialog

from generate_uis.quit_dialog_ui import Ui_QuitDialog


from Custom_Widgets.Widgets import iconify


class QuitDialog(QDialog, Ui_QuitDialog):
    """Quit Dialog classe"""
    def __init__(self, parent=None):
        """QuitDialog constructor"""
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Confirmation quitter")
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Méthode qui connecte les signaux à leurs slots"""
        self.yes_button.clicked.connect(self.on_yes_button_clicked)
        self.no_button.clicked.connect(self.on_no_button_clicked)

    def on_yes_button_clicked(self):
        """Méthode qui gère le click du button oui"""
        # Je ferme le widget parent qui à ouvert initialement la QDialog
        sys.exit()

    def on_no_button_clicked(self):
        """Méthode qui gère le click du button non"""
        # Je ferme la QDialog elle même
        self.close()
