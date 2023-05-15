from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from custom_dialogs.custom_message_dialog import CustomMessageDialog
from custom_widgets.book_custom_widget import BookCustomWidget

from generate_uis.select_book_for_note_ui import Ui_SelectBookForNoteWindow
from models.book import BookModel, BookStorage



class SelectBookToUpdateNote(QMainWindow, Ui_SelectBookForNoteWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.book_storage = BookStorage()
        self.construct_list_widget(self.book_storage.get_ten_last_books())
        self.connect_signals_to_slots()
        self.parent = parent

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
        self.search_book_line_edit.textChanged.connect(self.on_search_book_line_edit_text_changed)
        self.confirm_button.clicked.connect(self.on_confirm_button_clicked)

    def on_search_book_line_edit_text_changed(self):
        """Méthode qui permet de gérer le changement de texte du champ de texte pour rechercher un livre présent dans nos livres enregistrer"""
        list_books = self.book_storage.get_books_thanks_to_a_search(self.search_book_line_edit.text())
        self.construct_list_widget(list_books)

    def on_confirm_button_clicked(self):
        """Méthode qui permet de gérer le click du button confirmer"""
        try:
            current_list_widget_item_selected: QListWidgetItem = self.list_books_list_widget.currentItem()
            book_custom_widget_selected: BookCustomWidget = self.list_books_list_widget.itemWidget(current_list_widget_item_selected)
            self._book_selected = book_custom_widget_selected.book_model
            self.parent.book_selected_to_update = book_custom_widget_selected.book_model
            self.close()
        except AttributeError:
            self.close()