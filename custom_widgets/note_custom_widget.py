from PySide6 import QtCore

import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QImage
from custom_widgets.book_custom_widget import BookCustomWidget

from models.book import BookModel
from models.note import NoteModel

from res import res

class NoteCustomWidget(QWidget):
    """NoteCustomWidget classe"""
    def __init__(self, note_model: NoteModel, book_associate: BookModel = None):
        """
        Note Custom Widget's constructor
        :param note_model: note afin de créer le custom widget
        """
        super().__init__()
        self.note_model = note_model
        self.textQVBoxLayout = QVBoxLayout()
        self.text_up_label = QLabel(self.note_model.title)
        self.text_down_label = QLabel(f"{self.note_model.date}")
        self.textQVBoxLayout.addWidget(self.text_up_label)
        self.textQVBoxLayout.addWidget(self.text_down_label)
        self.main_layout = QHBoxLayout()
        self.thumbnail_label = QLabel()
        self.main_layout.addWidget(self.thumbnail_label, 0)
        self.main_layout.addLayout(self.textQVBoxLayout, 1)
        if book_associate != None:
            self.arrow_label = QLabel()
            arrow_pixmap = QPixmap(u":/images/images/arrow_right.png")
            arrow_pixmap = arrow_pixmap.scaled(20, 20, QtCore.Qt.KeepAspectRatio)
            self.arrow_label.setPixmap(arrow_pixmap)
            self.main_layout.addWidget(self.arrow_label, 1)
            book_custom_widget = BookCustomWidget(book_associate)
            self.main_layout.addWidget(book_custom_widget, 3)
        self.setLayout(self.main_layout)
        self.set_cover()

    def set_cover(self):
        """Méthode qui permet de charger l'image pour le widget customisé """
        pixmap = QPixmap(u":/images/images/icon_note_widget.png")
        pixmap = pixmap.scaled(40, 40, QtCore.Qt.KeepAspectRatio)
        self.thumbnail_label.setPixmap(pixmap)
