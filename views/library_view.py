"""
Module that manage the LibraryScreen of the application
author: amolixs
"""
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QListWidgetItem, QApplication

from PySide6.QtGui import QCursor

from PySide6.QtCore import Qt
from custom_dialogs.confirm_delete_dialog import ConfirmDeleteDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog
from custom_widgets.book_custom_widget import BookCustomWidget
from generate_uis.library_view_ui import Ui_LibraryWindow
from models.book import BookStorage
from models.note import NoteStorage
from views.book_view import BookView
from views.register_book_view import RegisterBookView
from views.update_book_view import UpdateBookView

class LibraryView(QWidget, Ui_LibraryWindow):
    """LibraryView classe"""
    def __init__(self, library_note_view):
        """Library View classe constructeur"""
        super().__init__()
        self.book_storage: BookStorage = BookStorage()
        self.manual_register_book_view = RegisterBookView(parent=self)
        self.update_book_view = UpdateBookView(parent=self, library_note_view=library_note_view)
        self.book_list_view = []
        self.setWindowTitle("Bibliothèque")
        self.setupUi(self)
        self.note_storage = NoteStorage()
        self.library_note_view = library_note_view
        self.clear_button.hide()
        self.connect_signals_to_slots()
        self.construct_list_widget(self.book_storage.get_ten_last_books())

    def construct_list_widget(self, list_books):
        """Méthode qui permet de construire la liste de widgets"""
        self.list_books_list_widget.clear()
        for book in list_books:
            new_book_custom_widget: BookCustomWidget = BookCustomWidget(book, parent=self)
            list_widget_item: QListWidgetItem = QListWidgetItem(self.list_books_list_widget)
            list_widget_item.setSizeHint(new_book_custom_widget.sizeHint())
            self.list_books_list_widget.addItem(list_widget_item)
            self.list_books_list_widget.setItemWidget(list_widget_item, new_book_custom_widget)

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux à leurs slots"""
        self.register_a_new_book_button.clicked.connect(self.on_register_a_new_book_button_clicked)
        self.search_book_line_edit.textChanged.connect(self.on_search_book_line_edit_text_changed)
        self.delete_book_button.clicked.connect(self.on_delete_book_button_clicked)
        self.update_book_button.clicked.connect(self.on_update_book_button_clicked)
        self.list_books_list_widget.itemDoubleClicked.connect(self.on_list_widget_item_double_clicked)
        self.clear_button.clicked.connect(self.on_clear_button_clicked)

    def on_register_a_new_book_button_clicked(self):
        """Méthode qui permet de gérer le click du button enregistrer un nouveau livre"""
        if not self.manual_register_book_view.isVisible():
            self.manual_register_book_view.show()

    def on_search_book_line_edit_text_changed(self):
        """Méthode qui permet de gérer le changement de texte du champ de texte pour rechercher un livre présent dans nos livres enregistrer"""
        if len(self.search_book_line_edit.text()) != 0:
            self.clear_button.show()
        else:
            self.clear_button.hide()
        if self.search_book_line_edit.text() == "shellyadepetitssourcils":
            custom_message_dialog = CustomMessageDialog("Easter Egg", "Shelly je t'aime")
            custom_message_dialog.exec()
        list_books = self.book_storage.get_books_thanks_to_a_search(self.search_book_line_edit.text())
        self.construct_list_widget(list_books)

    def on_delete_book_button_clicked(self):
        """Méthode qui permet de gérer le click du button supprimer un livre"""
        try:
            current_list_widget_item_selected: QListWidgetItem = self.list_books_list_widget.currentItem()
            book_custom_widget_selected: BookCustomWidget = self.list_books_list_widget.itemWidget(current_list_widget_item_selected)
            confirm_delete_book_dialog: ConfirmDeleteDialog = ConfirmDeleteDialog(
                model=book_custom_widget_selected.book_model, 
                title="Confirmation de suppression", 
                parent=self,
                message="Souhaitez-vous réelement supprimer le livre suivant ? : "
            )
            confirm_delete_book_dialog.exec()
            if confirm_delete_book_dialog.is_yes_to_delete:
                self.book_storage.delete_a_book(book_custom_widget_selected.book_model)
                self.book_storage.delete_cover_file_associate_to_book_to_delete(book_custom_widget_selected.book_model)
                self.construct_list_widget(self.book_storage.get_ten_last_books())
                self.library_note_view.construct_list_widget(self.note_storage.get_ten_last_notes())
        except AttributeError:
            custom_message_dialog = CustomMessageDialog("Erreur", "Veuillez sélectionner un livre à supprimer !")
            custom_message_dialog.exec()

    def on_update_book_button_clicked(self):
        """Méthode qui permet de gérer le click du button modifier un livre"""
        try:
            current_list_widget_item_selected: QListWidgetItem = self.list_books_list_widget.currentItem()
            book_custom_widget_selected: BookCustomWidget = self.list_books_list_widget.itemWidget(current_list_widget_item_selected)
            self.update_book_view.book_to_update = book_custom_widget_selected.book_model
            self.update_book_view.fill_fields()
            if not self.update_book_view.isVisible():
                self.update_book_view.show()
        except AttributeError:
            custom_message_dialog = CustomMessageDialog(title="Erreur", message="Veuillez sélectionner un livre à modifié !")
            custom_message_dialog.exec()

    def on_list_widget_item_double_clicked(self, item):
        """Méthode qui permet de gérer le double click lorsque l'on double click sur un livre afin d'obtenir des détails sur celui-ci"""
        book_custom_widget: BookCustomWidget = self.list_books_list_widget.itemWidget(item)
        book_view = BookView(book_model=book_custom_widget.book_model, book_list_view=self.book_list_view)
        self.book_list_view.append(book_view)
        for book_view in self.book_list_view:
            book_view.show()

    def on_clear_button_clicked(self):
        """Méthode qui permet de nettoyer le texte de la recherche"""
        self.search_book_line_edit.clear()