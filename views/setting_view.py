from PySide6.QtWidgets import QWidget, QFileDialog
from custom_dialogs.confirm_custom_dialog import ConfirmCustomDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog

from generate_uis.setting_view_ui import Ui_SettingWindow
from models.setting import Setting, SettingStorage

import os
import sys


class SettingView(QWidget, Ui_SettingWindow):
    """Setting view class"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_signals_to_slots()
        self.setting_storage = SettingStorage()
        self.fill_fields()

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux au slots"""
        self.save_button.clicked.connect(self.on_save_button_clicked)
        self.restore_button.clicked.connect(self.on_restore_button_clicked)
        self.path_directory_pdf.clicked.connect(self.on_path_directory_pdf_clicked)
        self.path_directory_txt.clicked.connect(self.on_path_directory_txt_clicked)
        self.path_directory_cover.clicked.connect(self.on_path_directory_cover_clicked)
        self.theme_combobox.currentTextChanged.connect(self.on_theme_combobox_current_text_changed)

    def fill_fields(self):
        """Méthode qui permet de remplir les champs en fonctions de se qui se trouve dans la db"""
        current_setting: Setting = self.setting_storage.get_all_settings("default")
        self.path_directory_pdf.setText(current_setting.export_pdf_note_path)
        self.path_directory_txt.setText(current_setting.export_txt_note_path)
        self.path_directory_cover.setText(current_setting.books_cover_folder_path)
        self.theme_combobox.setCurrentText(current_setting.theme)

    def on_save_button_clicked(self):
        """Méthode qui permet de gérer le signal de click du button sauvegarder"""
        theme: str = self.theme_combobox.currentText()
        current_theme: str = self.setting_storage.get_theme("default")
        new_setting = Setting(
            name="default", 
            theme=theme, 
            export_pdf_note_path=self.path_directory_pdf.text(),
            export_txt_note_path=self.path_directory_txt.text(),
            books_cover_folder_path=self.path_directory_cover.text()
        )
        confirm_custom_dialog = ConfirmCustomDialog("Confirmation sauvegarde", "Etes-vous sur de vouloir sauvegarder les parametres ?")
        confirm_custom_dialog.exec()
        if confirm_custom_dialog.is_yes:
            custom_message_dialog = CustomMessageDialog("Confirmation de sauvegarde", "Vos paramètres ont correctement été sauvegarder")
            custom_message_dialog.exec()
            self.setting_storage.update_all_settings(new_setting.name, new_setting)
            if theme != current_theme:
                os.execv(sys.executable, [sys.executable] + sys.argv)

    def on_restore_button_clicked(self):
        """Méthode qui permet de gérer le click du button pour restaurer les paramètres par defaut"""
        confirm_custom_dialog = ConfirmCustomDialog("Confirmation restauration", "Etes-vous sur de vouloir rétablir les parametres par défaut ?")
        confirm_custom_dialog.exec()
        if confirm_custom_dialog.is_yes:
            self.reset_all_fields()

    def test_if_directory_selected_is_correct(self, path_directory) -> bool:
        try:
            path_to_save = f"{path_directory}test"
            with open(path_to_save, 'w') as f:
                pass
            os.remove(path_to_save)
            return True
        except PermissionError:
            return False

    def reset_all_fields(self):
        """Méthode qui permet de remettre à zéro tous les champs"""
        setting = Setting(name="default")
        self.theme_combobox.setCurrentText(setting.theme)
        self.path_directory_pdf.setText(setting.export_pdf_note_path)
        self.path_directory_txt.setText(setting .export_txt_note_path)
        self.path_directory_cover.setText(setting.books_cover_folder_path)

    def on_path_directory_pdf_clicked(self):
        new_pdf_directory = str(QFileDialog.getExistingDirectory(self, 'Nouveau dossier pdf')) + "/"
        while not self.test_if_directory_selected_is_correct(new_pdf_directory):
            if new_pdf_directory == "/":
                new_pdf_directory = self.path_directory_pdf.text()
                break
            custom_message_box = CustomMessageDialog("Erreur", "Veuillez sélectionner un dossier valide !")
            custom_message_box.exec()
            new_pdf_directory = str(QFileDialog.getExistingDirectory(self, 'Nouveau dossier pdf')) + "/"
        self.path_directory_pdf.setText(new_pdf_directory)

    def on_path_directory_txt_clicked(self):
        new_txt_directory = str(QFileDialog.getExistingDirectory(self, 'Nouveau dossier txt')) + "/"
        while not self.test_if_directory_selected_is_correct(new_txt_directory):
            if new_txt_directory == "/":
                new_txt_directory = self.path_directory_txt.text()
                break
            custom_message_box = CustomMessageDialog("Erreur", "Veuillez sélectionner un dossier valide !")
            custom_message_box.exec()
            new_txt_directory = str(QFileDialog.getExistingDirectory(self, 'Nouveau dossier txt')) + "/"
        self.path_directory_txt.setText(new_txt_directory)

    def on_path_directory_cover_clicked(self):
        new_cover_directory = str(QFileDialog.getExistingDirectory(self, 'Nouveau dossier pour les couverture')) + "/"
        while not self.test_if_directory_selected_is_correct(new_cover_directory):
            if new_cover_directory == "/":
                new_cover_directory = self.path_directory_cover.text()
                break
            custom_message_box = CustomMessageDialog("Erreur", "Veuillez sélectionner un dossier valide !")
            custom_message_box.exec()
            new_cover_directory = str(QFileDialog.getExistingDirectory(self, 'Nouveau dossier pour les couverture')) + "/"
        self.path_directory_cover.setText(new_cover_directory)

    def on_theme_combobox_current_text_changed(self):
        theme_selected = self.theme_combobox.currentText()
        current_theme = self.setting_storage.get_theme("default")
        if theme_selected != current_theme:
            self.reload_label.setText("Relancement de l'application nécessaire")
        else:
            self.reload_label.setText("")