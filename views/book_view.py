import os
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtCore

import requests
from custom_dialogs.confirm_auto_save_file_dialog import ConfirmAutoSaveFileDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog
from custom_dialogs.export_dialog import ExportDialog

from generate_uis.book_view_ui import Ui_ViewBookWindow
from models.book import BookModel
from models.note import NoteStorage
from models.setting import SettingStorage
from pdf_manager import BookNotesPDF


class BookView(QWidget, Ui_ViewBookWindow):
    """BookView"""
    def __init__(self, book_model: BookModel, book_list_view):
        super().__init__()
        self.setupUi(self)
        self.book_list_view = book_list_view
        self.book_model: BookModel = book_model
        self.note_storage = NoteStorage()
        self.set_cover()
        self.setting_storage = SettingStorage()
        self.all_note_associate_to_books = self.note_storage.get_all_notes_associate_to_a_book(self.book_model.id)
        self.setWindowTitle(book_model.title)
        self.book_title_label.setText(book_model.title)
        self.book_pages_label.setText(str(book_model.pages))
        self.book_authors_label.setText(book_model.authors)
        self.book_types_label.setText(book_model.types)
        self.book_status_label.setText(book_model.status)
        self.book_isbn_label.setText(book_model.isbn)
        self.set_evaluation()
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux à leurs slots"""
        self.quit_button.clicked.connect(self.on_quit_button_clicked)
        self.export_book_button.clicked.connect(self.on_export_button_clicked)

    def closeEvent(self, event) -> None:
        self.book_list_view.remove(self)

    def set_cover(self):
        """Method that load the image of the book model"""
        pixmap: QPixmap
        if self.book_model.cover == "":
            pixmap = QPixmap(u":/images/images/no_cover.jpg")
        elif "books.google.com" in self.book_model.cover:
            cover_image = QImage()
            # Je construis mon image à partir des données de l'image récupérer via l'url internet.
            cover_image.loadFromData(requests.get(self.book_model.cover).content)
            pixmap = QPixmap(cover_image)
        else:
            pixmap = QPixmap(self.book_model.cover)
            # Je redimensionne mon image tous en gardant le ratio de mon image.
        pixmap = pixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio)
        self.book_picture_label.setPixmap(pixmap)

    def set_evaluation(self):
        """Method that set the status book label"""
        if self.book_model.evaluation == -1:
            self.book_eval_label.setText("Pas encore évalué !")
        else:
            self.book_eval_label.setText(str(self.book_model.evaluation))

    def on_export_button_clicked(self):
        """Méthode qui permet de gérer le signal de click du button exporter"""
        if self.note_storage.get_number_of_notes_associate_to_the_books(self.book_model.id) == 0:
            custom_message_dialog = CustomMessageDialog(title="Pas assez de notes", message="Le livre doit posséder au moin une note afin d'être exporté !")
            custom_message_dialog.exec()
        else:
            export_dialog = ExportDialog()
            export_dialog.exec()
            if export_dialog.is_pdf:
                book_notes_pdf = BookNotesPDF(book_model=self.book_model, all_notes_of_the_book=self.all_note_associate_to_books)
                name_file = self.book_model.title.replace(" ", "_") + "_notes" + ".pdf"
                try:
                    directory = str(QFileDialog.getExistingDirectory(self, 'Sauvegarder notes du livre')) + "/"
                    path_to_save = f"{directory}{name_file}"
                    book_notes_pdf.output(path_to_save, "F")
                    custom_message_dialog = CustomMessageDialog("Exportation réussie !", "Les notes ont correctement été exportée en pdf !")
                    custom_message_dialog.exec()
                except PermissionError:
                    directory = self.setting_storage.get_export_pdf_note_path("default")
                    if os.path.exists(directory) == False:
                        os.mkdir(directory)
                    confirm_auto_save_file_dialog = ConfirmAutoSaveFileDialog(f"Souhaitez exportée vos notes automatiquement dans le dossier : {directory} ?")
                    confirm_auto_save_file_dialog.exec()
                    if confirm_auto_save_file_dialog.is_yes:
                        path_to_save = f"{directory}{name_file}"
                        book_notes_pdf.output(path_to_save, "F")
                        custom_message_dialog = CustomMessageDialog("Exportation réussi", f"Les notes ont correctement été exportées dans le dossier par défaut : {directory}")
                        custom_message_dialog.exec()
            elif export_dialog.is_txt:
                name_file = self.book_model.title.replace(" ", "_") + "_notes" + ".txt"
                try:
                    directory = str(QFileDialog.getExistingDirectory(self, 'Sauvegarder notes du livre')) + "/"
                    path_to_save = f"{directory}{name_file}"
                    with open(path_to_save, 'w') as f:
                        for note in self.all_note_associate_to_books:
                            f.write(f"•{note.title.title()}\n\n")
                            f.write(f"{note.content}\n\n")
                            f.write("=====================================================\n\n")
                    custom_message_dialog = CustomMessageDialog("Exportation réussie !", "Les notes ont correctement été exportée en text !")
                    custom_message_dialog.exec()
                except PermissionError:
                    directory = self.setting_storage.get_export_txt_note_path("default")
                    if os.path.exists(directory) == False:
                        os.mkdir(directory)
                    confirm_auto_save_file_dialog = ConfirmAutoSaveFileDialog(f"Souhaitez exportée vos notes automatiquement dans le dossier : {directory} ?")
                    confirm_auto_save_file_dialog.exec()
                    if confirm_auto_save_file_dialog.is_yes:  
                        path_to_save = f"{directory}{name_file}"
                        with open(path_to_save, 'w') as f:
                            for note in self.all_note_associate_to_books:
                                f.write(f"•{note.title.title()}\n\n")
                                f.write(f"{note.content}\n\n")
                                f.write("=====================================================\n\n")
                        custom_message_dialog = CustomMessageDialog("Exportation réussi", f"Les notes ont correctement été exportée dans le dossier par défaut : {directory}")
                        custom_message_dialog.exec()
                self.close()


    def on_quit_button_clicked(self):
        """Méthode qui permet de gérer le signal du click du button quitter"""
        self.close()
