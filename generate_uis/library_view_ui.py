# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library_view_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from res import res

class Ui_LibraryWindow(object):
    def setupUi(self, LibraryWindow):
        if not LibraryWindow.objectName():
            LibraryWindow.setObjectName(u"LibraryWindow")
        LibraryWindow.resize(707, 343)
        self.verticalLayout = QVBoxLayout(LibraryWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_frame = QFrame(LibraryWindow)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_book_line_edit = QLineEdit(self.search_frame)
        self.search_book_line_edit.setObjectName(u"search_book_line_edit")

        self.horizontalLayout_2.addWidget(self.search_book_line_edit)

        self.clear_button = QPushButton(self.search_frame)
        self.clear_button.setObjectName(u"clear_button")
        icon = QIcon()
        icon.addFile(u":/images/images/icon_clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon)
        self.clear_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.clear_button)


        self.verticalLayout.addWidget(self.search_frame)

        self.list_books_list_widget = QListWidget(LibraryWindow)
        self.list_books_list_widget.setObjectName(u"list_books_list_widget")

        self.verticalLayout.addWidget(self.list_books_list_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.update_book_button = QPushButton(LibraryWindow)
        self.update_book_button.setObjectName(u"update_book_button")

        self.horizontalLayout.addWidget(self.update_book_button)

        self.delete_book_button = QPushButton(LibraryWindow)
        self.delete_book_button.setObjectName(u"delete_book_button")

        self.horizontalLayout.addWidget(self.delete_book_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.register_a_new_book_button = QPushButton(LibraryWindow)
        self.register_a_new_book_button.setObjectName(u"register_a_new_book_button")

        self.verticalLayout.addWidget(self.register_a_new_book_button)


        self.retranslateUi(LibraryWindow)

        QMetaObject.connectSlotsByName(LibraryWindow)
    # setupUi

    def retranslateUi(self, LibraryWindow):
        LibraryWindow.setWindowTitle(QCoreApplication.translate("LibraryWindow", u"Form", None))
        self.search_book_line_edit.setPlaceholderText(QCoreApplication.translate("LibraryWindow", u"Rechercher...", None))
        self.clear_button.setText("")
        self.update_book_button.setText(QCoreApplication.translate("LibraryWindow", u"Modifier", None))
        self.delete_book_button.setText(QCoreApplication.translate("LibraryWindow", u"Supprimer", None))
        self.register_a_new_book_button.setText(QCoreApplication.translate("LibraryWindow", u"Enregistrer un nouveau livre", None))
    # retranslateUi

