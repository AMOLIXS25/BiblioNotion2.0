from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QWidget, QListWidgetItem, QApplication
from custom_dialogs.confirm_delete_dialog import ConfirmDeleteDialog
from custom_dialogs.custom_message_dialog import CustomMessageDialog

from custom_widgets.note_custom_widget import NoteCustomWidget

from generate_uis.library_notes_view_ui import Ui_LibraryNoteWindow
from models.book import BookStorage
from models.note import NoteStorage
from views.note_view import NoteView
from views.register_note_view import RegisterNoteView
from views.select_book_to_register_note_view import SelectBookToRegisterNoteView
from views.update_note_view import UpdateNoteView


class LibraryNotesView(QWidget, Ui_LibraryNoteWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.note_storage = NoteStorage()
        self.book_storage = BookStorage()
        self.register_note_view = RegisterNoteView()
        self.construct_list_widget(self.note_storage.get_ten_last_notes())
        self.select_book_to_register_note = None
        self.update_note_view = None
        self.connect_signals_to_slots()
        self.clear_button.hide()
        self.note_list_view = []

    def connect_signals_to_slots(self):
        """Méthode qui permet de connecter les signaux à leurs slots"""
        self.register_a_new_note_button.clicked.connect(self.on_register_a_new_note_button_clicked)
        self.delete_note_button.clicked.connect(self.on_delete_a_note_button_clicked)
        self.search_note_line_edit.textChanged.connect(self.on_search_note_line_edit_text_changed)
        self.list_notes_list_widget.itemDoubleClicked.connect(self.on_list_notes_list_widget_item_double_clicked)
        self.update_note_button.clicked.connect(self.on_update_note_button_clicked)
        self.clear_button.clicked.connect(self.on_clear_button_clicked)

    def construct_list_widget(self, list_notes):
        """Méthode qui permet de construire la liste de widgets"""
        self.list_notes_list_widget.clear()
        for note in list_notes:
            book_assiocate = self.note_storage.get_book_associate_to_a_note(note.id)
            new_note_custom_widget: NoteCustomWidget = NoteCustomWidget(note, book_assiocate)
            list_widget_item: QListWidgetItem = QListWidgetItem(self.list_notes_list_widget)
            list_widget_item.setSizeHint(new_note_custom_widget.sizeHint())
            self.list_notes_list_widget.addItem(list_widget_item)
            self.list_notes_list_widget.setItemWidget(list_widget_item, new_note_custom_widget)

    def on_register_a_new_note_button_clicked(self):
        """Méthode qui permet de gérer le signal du button pour créer une nouvelle note"""
        if self.book_storage.get_number_of_books() == 0:
            self.register_note_view = RegisterNoteView(parent=self)
            self.register_note_view.show()
        else:   
            self.select_book_to_register_note = SelectBookToRegisterNoteView(parent=self)
            self.select_book_to_register_note.show()

    def on_delete_a_note_button_clicked(self):
        """Méthode qui permet de gérer le click du button supprimer une note"""
        try:
            current_list_widget_item_selected: QListWidgetItem = self.list_notes_list_widget.currentItem()
            note_custom_widget_selected: NoteCustomWidget = self.list_notes_list_widget.itemWidget(current_list_widget_item_selected)
            confirm_delete_book_dialog: ConfirmDeleteDialog = ConfirmDeleteDialog(
                model=note_custom_widget_selected.note_model, 
                title="Confirmation de suppression",
                parent=self,
                message="Souhaitez-vous réelement supprimer la note suivante ? : "
            )
            confirm_delete_book_dialog.exec()
            if confirm_delete_book_dialog.is_yes_to_delete:
                self.note_storage.delete_a_note(note_custom_widget_selected.note_model.id)    
                self.construct_list_widget(self.note_storage.get_ten_last_notes())
        except AttributeError:
            custom_message_dialog = CustomMessageDialog(title="Erreur", message="Veuillez sélectionner une note à supprimé !")
            custom_message_dialog.exec()

    def on_search_note_line_edit_text_changed(self):
        """Méthode qui permet de gérer l'événement de changement de texte pour rechercher une note"""
        if len(self.search_note_line_edit.text()) != 0:
            self.clear_button.show()
        else:
            self.clear_button.hide()
        list_notes = self.note_storage.get_notes_thanks_to_a_search(self.search_note_line_edit.text())
        self.construct_list_widget(list_notes)

    def on_list_notes_list_widget_item_double_clicked(self, item):
        """Méthode qui permet de gérer le double click lorsque l'on clique sur une note dans la liste de note"""
        note_custom_widget = self.list_notes_list_widget.itemWidget(item)
        note_view = NoteView(note_model=note_custom_widget.note_model, note_list_view=self.note_list_view)
        self.note_list_view.append(note_view)
        for note_view in self.note_list_view:
            note_view.show()

    def on_clear_button_clicked(self):
        """Méthode qui permet de nettoyer le texte de la recherche"""
        self.search_note_line_edit.clear()

    def on_update_note_button_clicked(self):
        """Méthode qui permet de gérer le signal du button mettre à jour"""
        try:
            current_list_item = self.list_notes_list_widget.currentItem()
            current_note_widget = self.list_notes_list_widget.itemWidget(current_list_item)
            self.update_note_view = UpdateNoteView(note_model=current_note_widget.note_model, parent=self)
            self.update_note_view.show()
        except AttributeError:
            custom_message_dialog = CustomMessageDialog(title="Erreur", message="Veuillez sélectionner une note à modifiée !")
            custom_message_dialog.exec()