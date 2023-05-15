from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6 import QtGui

from custom_dialogs.quit_dialog import QuitDialog
from generate_uis.main_view_ui import Ui_MainWindow

from Custom_Widgets.Widgets import loadJsonStyle

from models.setting import SettingStorage

from res import res


class MainView(QMainWindow, Ui_MainWindow):
    """MainView classe"""

    def __init__(self):
        """MainView classe constructeur"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("")
        self.setting_storage = SettingStorage()
        if self.setting_storage.get_theme("default") == "Défaut":
            self.setWindowIcon(QtGui.QIcon(u":/images/images/icon_splash_screen.png"))
        else:
            self.setWindowIcon(QtGui.QIcon(u":/images/images/icon_splash_screen_purple.png"))
        if self.setting_storage.get_theme("default") == "Défaut":
            self.__active_button_style: str = """
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
                border-left: 2px solid rgb(254, 206, 47);
                background-color: #292929;
            """
        elif self.setting_storage.get_theme("default") == "Purple Drop":
            self.__active_button_style: str = """
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
                border-left: 2px solid rgb(198, 120, 221);
                background-color: #292929;
            """
        self.__slide_menu_buttons: list[QPushButton] = [
            self.library_button,
            self.notes_button,
            self.settings_button,
            self.quit_button
        ]
        self.library_button.setStyleSheet(self.__active_button_style)
        self.connect_signals_to_slots()
        loadJsonStyle(self, self)

    def set_active_style_on_slide_menu_button_clicked(self, button_clicked: QPushButton):
        """Méthode qui permet de définir un style sur le button du slide menu actif

        Args:
            button_clicked (QPushButton): Le button qui à été cliquer depuis le SlideMenu 
        """
        for button in self.__slide_menu_buttons:
            if button.objectName() == button_clicked.objectName():
                button.setStyleSheet(self.__active_button_style)
            else:
                button.setStyleSheet("")

    def connect_signals_to_slots(self):
        """Méthode qui connecte les slots à leurs signaux"""
        self.library_button.clicked.connect(self.on_library_button_clicked)
        self.settings_button.clicked.connect(self.on_settings_button_clicked)
        self.notes_button.clicked.connect(self.on_notes_button_clicked)
        self.quit_button.clicked.connect(self.on_quit_button_clicked)

    ##################
    # MES SLOTS
    ##################

    def on_library_button_clicked(self):
        """Méthode qui gère le click du button bibliothèque"""
        self.set_active_style_on_slide_menu_button_clicked(self.library_button)

    def on_notes_button_clicked(self):
        """Méthode qui gère le click du button notes"""
        self.set_active_style_on_slide_menu_button_clicked(self.notes_button)

    def on_settings_button_clicked(self):
        """Méthode qui gère le click du button paramètres"""
        self.set_active_style_on_slide_menu_button_clicked(self.settings_button)

    def on_quit_button_clicked(self):
        """Méthode qui gère le click du button quitter"""
        self.set_active_style_on_slide_menu_button_clicked(self.quit_button)
        quit_dialog: QuitDialog = QuitDialog()
        quit_dialog.exec()