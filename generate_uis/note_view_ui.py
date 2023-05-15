# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_view_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ViewNoteWindow(object):
    def setupUi(self, ViewNoteWindow):
        if not ViewNoteWindow.objectName():
            ViewNoteWindow.setObjectName(u"ViewNoteWindow")
        ViewNoteWindow.resize(505, 447)
        self.verticalLayout = QVBoxLayout(ViewNoteWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.title_label = QLabel(ViewNoteWindow)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(14)
        self.title_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.title_label)

        self.date_label = QLabel(ViewNoteWindow)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.date_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.content_plain_text_edit = QPlainTextEdit(ViewNoteWindow)
        self.content_plain_text_edit.setObjectName(u"content_plain_text_edit")
        self.content_plain_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.content_plain_text_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.export_button = QPushButton(ViewNoteWindow)
        self.export_button.setObjectName(u"export_button")

        self.horizontalLayout.addWidget(self.export_button)

        self.quit_button = QPushButton(ViewNoteWindow)
        self.quit_button.setObjectName(u"quit_button")

        self.horizontalLayout.addWidget(self.quit_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ViewNoteWindow)

        QMetaObject.connectSlotsByName(ViewNoteWindow)
    # setupUi

    def retranslateUi(self, ViewNoteWindow):
        ViewNoteWindow.setWindowTitle(QCoreApplication.translate("ViewNoteWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("ViewNoteWindow", u"TextLabel", None))
        self.date_label.setText(QCoreApplication.translate("ViewNoteWindow", u"TextLabel", None))
        self.export_button.setText(QCoreApplication.translate("ViewNoteWindow", u"Exporter", None))
        self.quit_button.setText(QCoreApplication.translate("ViewNoteWindow", u"Quitter", None))
    # retranslateUi

