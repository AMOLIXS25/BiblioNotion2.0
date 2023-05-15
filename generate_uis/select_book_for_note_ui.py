# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_book_for_note_ui.ui'
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

class Ui_SelectBookForNoteWindow(object):
    def setupUi(self, SelectBookForNoteWindow):
        if not SelectBookForNoteWindow.objectName():
            SelectBookForNoteWindow.setObjectName(u"SelectBookForNoteWindow")
        SelectBookForNoteWindow.resize(589, 271)
        self.centralwidget = QWidget(SelectBookForNoteWindow)
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


        self.verticalLayout.addLayout(self.horizontalLayout)

        SelectBookForNoteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectBookForNoteWindow)

        QMetaObject.connectSlotsByName(SelectBookForNoteWindow)
    # setupUi

    def retranslateUi(self, SelectBookForNoteWindow):
        SelectBookForNoteWindow.setWindowTitle(QCoreApplication.translate("SelectBookForNoteWindow", u"MainWindow", None))
        self.search_book_line_edit.setPlaceholderText(QCoreApplication.translate("SelectBookForNoteWindow", u"Rechercher un livre...", None))
        self.confirm_button.setText(QCoreApplication.translate("SelectBookForNoteWindow", u"Confirmer", None))
    # retranslateUi

