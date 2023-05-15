from PySide6.QtWidgets import QWidget, QFileDialog
from custom_dialogs.confirm_auto_save_file_dialog import ConfirmAutoSaveFileDialog
from custom_dialogs.export_dialog import ExportDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog

from generate_uis.note_view_ui import Ui_ViewNoteWindow
from models.setting import SettingStorage
from pdf_manager import NotePDF


class NoteView(QWidget, Ui_ViewNoteWindow):
    """NoteView classe"""
    def __init__(self, note_model, note_list_view):
        """NoteView constructeur"""
        super().__init__()
        self.setupUi(self)
        self.note_model = note_model
        self.setting_storage = SettingStorage()
        self.title_label.setText(note_model.title)
        self.date_label.setText(note_model.date)
        self.content_plain_text_edit.setPlainText(note_model.content)
        self.note_list_view = note_list_view
        self.setWindowTitle(note_model.title)
        self.connect_signals_to_slots()

    def closeEvent(self, event) -> None:
        self.note_list_view.remove(self)

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux à leurs slots"""
        self.quit_button.clicked.connect(self.on_quit_button_clicked)
        self.export_button.clicked.connect(self.on_export_button_clicked)

    def on_export_button_clicked(self):
        """Méthode qui permet de gérer le click du button exporter"""
        export_dialog = ExportDialog()
        export_dialog.exec()
        if export_dialog.is_pdf:
            note_pdf = NotePDF(note_model=self.note_model)
            name_file = self.note_model.title.replace(" ", "_") + ".pdf"
            try:
                directory = str(QFileDialog.getExistingDirectory(self, 'Sauvegarder note')) + "/"
                path_to_save = f"{directory}{name_file}"
                note_pdf.output(path_to_save, "F")
                custom_message_dialog = CustomMessageDialog("Exportation réussie !", "Votre note a correctement été exportée en pdf !")
                custom_message_dialog.exec()
            except PermissionError:
                directory = self.setting_storage.get_export_pdf_note_path("default")
                confirm_auto_save_file_dialog = ConfirmAutoSaveFileDialog(f"Souhaitez exportée votre note automatiquement dans le dossier : {directory} ?")
                confirm_auto_save_file_dialog.exec()
                if confirm_auto_save_file_dialog.is_yes:
                    path_to_save = f"{directory}{name_file}"
                    note_pdf.output(path_to_save, "F")
                    custom_message_dialog = CustomMessageDialog("Exportation réussi", f"Votre note à été exportée dans le dossier par défaut : {directory}")
                    custom_message_dialog.exec()
            self.close()
        elif export_dialog.is_txt:
            name_file = self.note_model.title.replace(" ", "_") + ".txt"
            try:
                directory = str(QFileDialog.getExistingDirectory(self, 'Sauvegarder note')) + "/"
                path_to_save = f"{directory}{name_file}"
                with open(path_to_save, 'w') as f:
                    f.write(self.note_model.content)
                custom_message_dialog = CustomMessageDialog("Exportation réussie !", "Votre note a correctement été exportée en text !")
                custom_message_dialog.exec()
            except PermissionError:
                directory = self.setting_storage.get_export_txt_note_path("default")
                confirm_auto_save_file_dialog = ConfirmAutoSaveFileDialog(f"Souhaitez exportée votre note automatiquement dans le dossier : {directory} ?")
                confirm_auto_save_file_dialog.exec()
                if confirm_auto_save_file_dialog.is_yes:  
                    path_to_save = f"{directory}{name_file}"
                    with open(path_to_save, 'w') as f:
                        f.write(self.note_model.content)
                    custom_message_dialog = CustomMessageDialog("Exportation réussi", f"Votre note à été exportée dans le dossier par défaut : {directory}")
                    custom_message_dialog.exec()
            self.close()

    def on_quit_button_clicked(self):
        """Méthode qui permet de gérer le signal du button quitter"""
        self.close()