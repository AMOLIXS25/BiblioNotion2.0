# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library_notes_view_ui.ui'
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

class Ui_LibraryNoteWindow(object):
    def setupUi(self, LibraryNoteWindow):
        if not LibraryNoteWindow.objectName():
            LibraryNoteWindow.setObjectName(u"LibraryNoteWindow")
        LibraryNoteWindow.resize(707, 343)
        self.verticalLayout = QVBoxLayout(LibraryNoteWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_frame = QFrame(LibraryNoteWindow)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_note_line_edit = QLineEdit(self.search_frame)
        self.search_note_line_edit.setObjectName(u"search_note_line_edit")

        self.horizontalLayout_2.addWidget(self.search_note_line_edit)

        self.clear_button = QPushButton(self.search_frame)
        self.clear_button.setObjectName(u"clear_button")
        icon = QIcon()
        icon.addFile(u":/images/images/icon_clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon)
        self.clear_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.clear_button)

        self.verticalLayout.addWidget(self.search_frame)

        self.list_notes_list_widget = QListWidget(LibraryNoteWindow)
        self.list_notes_list_widget.setObjectName(u"list_notes_list_widget")

        self.verticalLayout.addWidget(self.list_notes_list_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.update_note_button = QPushButton(LibraryNoteWindow)
        self.update_note_button.setObjectName(u"update_note_button")

        self.horizontalLayout.addWidget(self.update_note_button)

        self.delete_note_button = QPushButton(LibraryNoteWindow)
        self.delete_note_button.setObjectName(u"delete_note_button")

        self.horizontalLayout.addWidget(self.delete_note_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.register_a_new_note_button = QPushButton(LibraryNoteWindow)
        self.register_a_new_note_button.setObjectName(u"register_a_new_note_button")

        self.verticalLayout.addWidget(self.register_a_new_note_button)


        self.retranslateUi(LibraryNoteWindow)

        QMetaObject.connectSlotsByName(LibraryNoteWindow)
    # setupUi

    def retranslateUi(self, LibraryNoteWindow):
        LibraryNoteWindow.setWindowTitle(QCoreApplication.translate("LibraryNoteWindow", u"Form", None))
        self.search_note_line_edit.setPlaceholderText(QCoreApplication.translate("LibraryNoteWindow", u"Rechercher une note...", None))
        self.clear_button.setText("")
        self.update_note_button.setText(QCoreApplication.translate("LibraryNoteWindow", u"Modifier", None))
        self.delete_note_button.setText(QCoreApplication.translate("LibraryNoteWindow", u"Supprimer", None))
        self.register_a_new_note_button.setText(QCoreApplication.translate("LibraryNoteWindow", u"Enregistrer une nouvelle note", None))
    # retranslateUi

