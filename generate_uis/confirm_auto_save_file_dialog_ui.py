# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_auto_save_file_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ConfirmAutoSaveFIleDialog(object):
    def setupUi(self, ConfirmAutoSaveFIleDialog):
        if not ConfirmAutoSaveFIleDialog.objectName():
            ConfirmAutoSaveFIleDialog.setObjectName(u"ConfirmAutoSaveFIleDialog")
        ConfirmAutoSaveFIleDialog.resize(446, 147)
        self.verticalLayout = QVBoxLayout(ConfirmAutoSaveFIleDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message_label = QLabel(ConfirmAutoSaveFIleDialog)
        self.message_label.setObjectName(u"message_label")

        self.verticalLayout.addWidget(self.message_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_button = QPushButton(ConfirmAutoSaveFIleDialog)
        self.yes_button.setObjectName(u"yes_button")

        self.horizontalLayout.addWidget(self.yes_button)

        self.no_button = QPushButton(ConfirmAutoSaveFIleDialog)
        self.no_button.setObjectName(u"no_button")

        self.horizontalLayout.addWidget(self.no_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ConfirmAutoSaveFIleDialog)

        QMetaObject.connectSlotsByName(ConfirmAutoSaveFIleDialog)
    # setupUi

    def retranslateUi(self, ConfirmAutoSaveFIleDialog):
        ConfirmAutoSaveFIleDialog.setWindowTitle(QCoreApplication.translate("ConfirmAutoSaveFIleDialog", u"Dialog", None))
        self.message_label.setText(QCoreApplication.translate("ConfirmAutoSaveFIleDialog", u"TextLabel", None))
        self.yes_button.setText(QCoreApplication.translate("ConfirmAutoSaveFIleDialog", u"Oui", None))
        self.no_button.setText(QCoreApplication.translate("ConfirmAutoSaveFIleDialog", u"Non", None))
    # retranslateUi

