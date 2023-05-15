# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_note_view_ui.ui'
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

class Ui_UpdateNoteWindow(object):
    def setupUi(self, UpdateNoteWindow):
        if not UpdateNoteWindow.objectName():
            UpdateNoteWindow.setObjectName(u"UpdateNoteWindow")
        UpdateNoteWindow.resize(559, 514)
        self.centralwidget = QWidget(UpdateNoteWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_line_edit = QLineEdit(self.centralwidget)
        self.title_line_edit.setObjectName(u"title_line_edit")
        self.title_line_edit.setDragEnabled(False)
        self.title_line_edit.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.title_line_edit)

        self.content_plaintext_edit = QPlainTextEdit(self.centralwidget)
        self.content_plaintext_edit.setObjectName(u"content_plaintext_edit")

        self.verticalLayout.addWidget(self.content_plaintext_edit)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.hide()

        self.verticalLayout.addWidget(self.error_label)

        self.move_note_to_another_book_button = QPushButton(self.centralwidget)
        self.move_note_to_another_book_button.setObjectName(u"move_note_to_another_book_button")

        self.verticalLayout.addWidget(self.move_note_to_another_book_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.quit_button = QPushButton(self.centralwidget)
        self.quit_button.setObjectName(u"quit_button")

        self.horizontalLayout.addWidget(self.quit_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        UpdateNoteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UpdateNoteWindow)

        QMetaObject.connectSlotsByName(UpdateNoteWindow)
    # setupUi

    def retranslateUi(self, UpdateNoteWindow):
        UpdateNoteWindow.setWindowTitle("")
#if QT_CONFIG(tooltip)
        UpdateNoteWindow.setToolTip(QCoreApplication.translate("UpdateNoteWindow", u"ertyuio", None))
#endif // QT_CONFIG(tooltip)
        self.error_label.setText("")
        self.move_note_to_another_book_button.setText(QCoreApplication.translate("UpdateNoteWindow", u"D\u00e9placer la note dans un autre live", None))
        self.save_button.setText(QCoreApplication.translate("UpdateNoteWindow", u"Appliquer les modifications", None))
        self.quit_button.setText(QCoreApplication.translate("UpdateNoteWindow", u"Quitter", None))
    # retranslateUi

