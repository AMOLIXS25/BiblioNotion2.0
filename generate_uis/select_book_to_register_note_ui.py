# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_book_to_register_note_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_SelectBookToRegisterNoteWindow(object):
    def setupUi(self, SelectBookToRegisterNoteWindow):
        if not SelectBookToRegisterNoteWindow.objectName():
            SelectBookToRegisterNoteWindow.setObjectName(u"SelectBookToRegisterNoteWindow")
        SelectBookToRegisterNoteWindow.resize(589, 271)
        self.centralwidget = QWidget(SelectBookToRegisterNoteWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_book_line_edit = QLineEdit(self.centralwidget)
        self.search_book_line_edit.setObjectName(u"search_book_line_edit")

        self.verticalLayout.addWidget(self.search_book_line_edit)

        self.list_books_list_widget = QListWidget(self.centralwidget)
        self.list_books_list_widget.setObjectName(u"list_books_list_widget")

        self.verticalLayout.addWidget(self.list_books_list_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirm_button = QPushButton(self.centralwidget)
        self.confirm_button.setObjectName(u"confirm_button")

        self.horizontalLayout.addWidget(self.confirm_button)

        self.no_select_book_button = QPushButton(self.centralwidget)
        self.no_select_book_button.setObjectName(u"no_select_book_button")

        self.horizontalLayout.addWidget(self.no_select_book_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        SelectBookToRegisterNoteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectBookToRegisterNoteWindow)

        QMetaObject.connectSlotsByName(SelectBookToRegisterNoteWindow)
    # setupUi

    def retranslateUi(self, SelectBookToRegisterNoteWindow):
        SelectBookToRegisterNoteWindow.setWindowTitle(QCoreApplication.translate("SelectBookToRegisterNoteWindow", u"MainWindow", None))
        self.search_book_line_edit.setPlaceholderText(QCoreApplication.translate("SelectBookToRegisterNoteWindow", u"Rechercher un livre...", None))
        self.confirm_button.setText(QCoreApplication.translate("SelectBookToRegisterNoteWindow", u"Confirmer", None))
        self.no_select_book_button.setText(QCoreApplication.translate("SelectBookToRegisterNoteWindow", u"Ne pas s\u00e9lectionner de livre", None))
    # retranslateUi

