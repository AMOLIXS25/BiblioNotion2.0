# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_note_view_ui.ui'
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
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_RegisterNoteWindow(object):
    def setupUi(self, RegisterNoteWindow):
        if not RegisterNoteWindow.objectName():
            RegisterNoteWindow.setObjectName(u"RegisterNoteWindow")
        RegisterNoteWindow.resize(582, 516)
        self.centralwidget = QWidget(RegisterNoteWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_line_edit = QLineEdit(self.centralwidget)
        self.title_line_edit.setObjectName(u"title_line_edit")

        self.verticalLayout.addWidget(self.title_line_edit)

        self.content_text_edit = QPlainTextEdit(self.centralwidget)
        self.content_text_edit.setObjectName(u"content_text_edit")

        self.verticalLayout.addWidget(self.content_text_edit)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setVisible(False)

        self.verticalLayout.addWidget(self.error_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.register_button = QPushButton(self.centralwidget)
        self.register_button.setObjectName(u"register_button")

        self.horizontalLayout.addWidget(self.register_button)

        self.import_button = QPushButton(self.centralwidget)
        self.import_button.setObjectName(u"import_button")

        self.horizontalLayout.addWidget(self.import_button)

        self.quit_button = QPushButton(self.centralwidget)
        self.quit_button.setObjectName(u"quit_button")

        self.horizontalLayout.addWidget(self.quit_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        RegisterNoteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterNoteWindow)

        QMetaObject.connectSlotsByName(RegisterNoteWindow)
    # setupUi

    def retranslateUi(self, RegisterNoteWindow):
        RegisterNoteWindow.setWindowTitle(QCoreApplication.translate("RegisterNoteWindow", u"MainWindow", None))
        self.title_line_edit.setPlaceholderText(QCoreApplication.translate("RegisterNoteWindow", u"Titre de la note \u00e0 cr\u00e9e", None))
        self.content_text_edit.setPlainText("")
        self.content_text_edit.setPlaceholderText(QCoreApplication.translate("RegisterNoteWindow", u"Contenu de la note \u00e0 cr\u00e9e", None))
        self.error_label.setText(QCoreApplication.translate("RegisterNoteWindow", u"TextLabel", None))
        self.register_button.setText(QCoreApplication.translate("RegisterNoteWindow", u"Enregistrer", None))
        self.import_button.setText(QCoreApplication.translate("RegisterNoteWindow", u"Importer", None))
        self.quit_button.setText(QCoreApplication.translate("RegisterNoteWindow", u"Fermer", None))
    # retranslateUi

