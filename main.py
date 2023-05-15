import sys

from PySide6.QtWidgets import QApplication
from models.setting import SettingStorage

from views.splash_screen_view import SplashScreenView

def load_css(css_file_name: str, app: QApplication):
    """
    Méthode qui permet de charger mon style css à l'intérieur de mon application
    :param css_file_name: le nom du fichier css à chargé
    :param app: l'application ou il faut chargé le style css
    """
    with open(css_file_name, "r") as f:
        style: str = f.read()
        app.setStyleSheet(style)


if __name__ == "__main__":
    setting_storage = SettingStorage()
    # Je lance ma boucle d'événement en passant les paramètres de la console
    app: QApplication = QApplication(sys.argv)
    splash_view: SplashScreenView = SplashScreenView()
    splash_view.show()
    if setting_storage.get_theme("default") == "Défaut":
        load_css("styles/css/default.css", app)
    elif setting_storage.get_theme("default") == "Purple Drop":
        load_css("styles/css/purple_drop.css", app)
    app.exec()

