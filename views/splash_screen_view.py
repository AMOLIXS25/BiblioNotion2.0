from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QMainWindow, QApplication
from custom_dialogs.no_connection_dialog import NoConnectionDialog

from generate_uis.splash_view_ui import Ui_SplashScreenWindow
from models.book import BookApi
from models.setting import Setting, SettingStorage
from views.main_view import MainView


class SplashScreenView(QMainWindow, Ui_SplashScreenWindow):
    """SplashScreenView classe"""
    def __init__(self):
        """SplashScreenView Constructeur"""
        super().__init__()
        self.setupUi(self)
        self.__main_view: MainView = None
        self.__counter_loading: int = 40
        # Je créer mon timer
        self.__timer: QTimer = QTimer()
        self.start_loader()
        self.__counter_loading_max: int = 100
        # Permet de faire en sorte que ma fenêtre ne possède pas la barre du haut des fenêtre classique
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.center_splash_screen()

    def center_splash_screen(self):
        """Méthode qui permet de centrer mon splashscreen à l'écran"""
        available_screen_size: QRect = QScreen.availableGeometry(QApplication.primaryScreen())
        pos_center_x: float = (available_screen_size.width() - self.width()) / 2
        pos_center_y: float = (available_screen_size.height() - self.height()) / 2
        self.move(pos_center_x, pos_center_y)

    def loading(self):
        """Méthode qui permet d'incrémenter le loader pour la progressBar"""
        self.loading_progress_bar.setValue(self.__counter_loading)
        if self.__counter_loading >= self.__counter_loading_max:
            self.__timer.stop()
            self.close()
            self.launch_no_connection_dialog()
            self.launch_main_view()
        self.__counter_loading += 1

    def start_loader(self):
        """Méthode qui permet de lancer le loader pour la progressBar"""
        # Je connecte la minuterie de mon timer à ma method loading qui va incrémenter la ProgressBar
        self.__timer.timeout.connect(self.loading)
        # Je démarre et j'incrémente mon timer toutes les 30 millisecondes
        self.__timer.start(30)


    def launch_main_view(self):
        """Méthode qui permet de lancer la vue principal"""
        if self.__main_view == None:
            self.__main_view = MainView()
            self.__main_view.show()
        else:
            self.__main_view = None


    def launch_no_connection_dialog(self):
        """Méthode qui permet de lancer le test de l'api"""
        setting_storage = SettingStorage()
        if not BookApi.test_connexion_to_api() and setting_storage.get_display_popup_no_connection("default"):
            no_connection_dialog = NoConnectionDialog()
            no_connection_dialog.exec()