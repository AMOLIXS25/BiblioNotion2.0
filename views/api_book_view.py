"""Module that manage Register book Screen"""
from time import sleep
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QApplication, QListWidget
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

from custom_dialogs.custom_message_dialog import CustomMessageDialog
from custom_widgets.book_custom_widget import BookCustomWidget
from generate_uis.api_book_view_ui import Ui_ApiBookWindow
from models.book import BookApi, BookStorage

import threading

class ApiBookView(QMainWindow, Ui_ApiBookWindow):
    """Register Book Screen class"""
    def __init__(self, parent=None):
        """Register Book Screen's constructor"""
        super().__init__()
        self.setupUi(self)
        self.connect_signals_to_slots()
        self.model: BookStorage = BookStorage()
        self.parent = parent

    def connect_signals_to_slots(self):
        """Connect all signals to slots"""
        self.run_search_button.clicked.connect(self.on_run_search_button_clicked)
        self.register_book_in_library_button.clicked.connect(self.on_register_book_in_library_button_clicked)

    def on_run_search_button_clicked(self):
        if self.search_a_book_line_edit.text() != "":
            self.books_find_in_api_list_widget.clear()
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            # Je construit ma liste de livre depuis grâce au donnée récupérer depuis l'api
            book_api = BookApi()
            book_api.construct_list_books(book_api.get_json_data_from_url(self.search_a_book_line_edit.text()))
            # Pour chaque livre je créer mon custom widget qui lui est associé
            for book in book_api.books_get_with_api:
                new_book_custom_widget: BookCustomWidget = BookCustomWidget(book)
                list_widget_item: QListWidgetItem = QListWidgetItem(self.books_find_in_api_list_widget)
                list_widget_item.setSizeHint(new_book_custom_widget.sizeHint())
                self.books_find_in_api_list_widget.addItem(list_widget_item)
                self.books_find_in_api_list_widget.setItemWidget(list_widget_item, new_book_custom_widget)
            QApplication.restoreOverrideCursor()
        else:
            custom_message_dialog: CustomMessageDialog = CustomMessageDialog("Erreur", "Veuillez rechercher un livre !")
            custom_message_dialog.exec()

    def on_register_book_in_library_button_clicked(self):
        """Method that manage the register book click"""
        try:
            current_list_widget_item_selected: QListWidgetItem = self.books_find_in_api_list_widget.currentItem()
            book_custom_widget_selected: BookCustomWidget = self.books_find_in_api_list_widget.itemWidget(current_list_widget_item_selected)
            # J'insère le livre associé au custom_widget sélectionner dans la bdd
            # book_custom_widget_selected.book_model.cover = BookApi.save_cover_into_file(book_custom_widget_selected.book_model.cover, book_custom_widget_selected.book_model.title)
            # self.model.insert_a_book(book_custom_widget_selected.book_model)
            # confirm_register_book_dialog: ConfirmRegisterBookDialog = ConfirmRegisterBookDialog(book_register=book_custom_widget_selected.book_model, text="Le livre suivant à bien été renregistré dans votre bibliothèque : ", parent=self)
            # confirm_register_book_dialog.exec()
            book_model_to_register = book_custom_widget_selected.book_model
            self.parent.fill_fields(
                cover_path=book_model_to_register.cover, 
                title=book_model_to_register.title, 
                authors=book_model_to_register.authors, 
                pages_number=book_model_to_register.pages,
                published_date=book_model_to_register.published_date,
                isbn=book_model_to_register.isbn
            )
            self.close()
        except AttributeError:
            custom_message_dialog = CustomMessageDialog("Erreur", "Veuillez sélectionner un livre à enregistrer !")
            custom_message_dialog.exec()
