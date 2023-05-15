from PySide6 import QtCore

import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QImage

from models.book import BookModel

from res import res

class BookCustomWidget(QWidget):
    """BookCustomWidget class"""
    def __init__(self, book_model: BookModel, parent=None):
        """
        Book Custom Widget's constructor
        :param book_model: book to create custom widget
        """
        self.book_model = book_model
        super(BookCustomWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.text_up_label = QLabel(self.book_model.title)
        self.text_down_label = QLabel(f"{self.book_model.published_date} - {self.book_model.authors}")
        self.textQVBoxLayout.addWidget(self.text_up_label)
        self.textQVBoxLayout.addWidget(self.text_down_label)
        self.main_layout = QHBoxLayout()
        self.thumbnail_label = QLabel()
        self.main_layout.addWidget(self.thumbnail_label, 0)
        self.main_layout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.main_layout)
        self.set_cover()

    def set_cover(self):
        """Method load the image url into the image label"""
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
        pixmap = pixmap.scaled(40, 40, QtCore.Qt.KeepAspectRatio)
        self.thumbnail_label.setPixmap(pixmap)
