
import sys
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QMovie

from generate_uis.no_connection_dialog_ui import Ui_NoConnectionDialog
from models.setting import SettingStorage

from res import res


class NoConnectionDialog(QDialog, Ui_NoConnectionDialog):
    """NoConnectionDialog classe"""
    def __init__(self):
        """NoConnectionDialog classe constructeur"""
        super().__init__()
        self.setupUi(self)
        self.connect_signals_to_slots()
        self.set_gif()
        self.__setting_storage = SettingStorage()

    def set_gif(self):
        """Méthode qui permet de mettre en place le gif"""
        movie = QMovie(u":/images/images/no_connection.gif")
        self.gif_label.setMovie(movie)
        movie.start()

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signals au slots"""
        self.yes_button.clicked.connect(self.on_yes_button_clicked)
        self.no_button.clicked.connect(self.on_no_button_clicked)

    def on_no_button_clicked(self):
        """Méthode qui permet de gérer le signal de click sur le button no"""
        if self.checkBox.isChecked():
            self.__setting_storage.update_display_popup_no_connection("default", False)
        sys.exit()

    def on_yes_button_clicked(self):
        """Méthode qui permet de gérer le signal de click sur le button yes"""
        if self.checkBox.isChecked():
            self.__setting_storage.update_display_popup_no_connection("default", False)
        self.close()
