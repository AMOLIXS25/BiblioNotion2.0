# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_book_view_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from res import res

class Ui_ApiBookWindow(object):
    def setupUi(self, ApiBookWindow):
        if not ApiBookWindow.objectName():
            ApiBookWindow.setObjectName(u"ApiBookWindow")
        ApiBookWindow.resize(558, 377)
        self.centralwidget = QWidget(ApiBookWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_a_book_line_edit = QLineEdit(self.centralwidget)
        self.search_a_book_line_edit.setObjectName(u"search_a_book_line_edit")

        self.horizontalLayout.addWidget(self.search_a_book_line_edit)

        self.run_search_button = QPushButton(self.centralwidget)
        self.run_search_button.setObjectName(u"run_search_button")
        icon = QIcon()
        icon.addFile(u":/images/images/icon_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.run_search_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.run_search_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.books_find_in_api_list_widget = QListWidget(self.centralwidget)
        self.books_find_in_api_list_widget.setObjectName(u"books_find_in_api_list_widget")

        self.verticalLayout.addWidget(self.books_find_in_api_list_widget)

        self.register_book_in_library_button = QPushButton(self.centralwidget)
        self.register_book_in_library_button.setObjectName(u"register_book_in_library_button")

        self.verticalLayout.addWidget(self.register_book_in_library_button)

        ApiBookWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ApiBookWindow)

        QMetaObject.connectSlotsByName(ApiBookWindow)
    # setupUi

    def retranslateUi(self, ApiBookWindow):
        ApiBookWindow.setWindowTitle(QCoreApplication.translate("ApiBookWindow", u"Enregistrer un nouveau livre", None))
        self.title.setText(QCoreApplication.translate("ApiBookWindow", u"Enregistrer un livre", None))
        self.search_a_book_line_edit.setPlaceholderText(QCoreApplication.translate("ApiBookWindow", u"Rechercher un livre...", None))
        self.run_search_button.setText("")
        self.register_book_in_library_button.setText(QCoreApplication.translate("ApiBookWindow", u"Valider", None))
    # retranslateUi

