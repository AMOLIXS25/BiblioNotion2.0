# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_reset_settings_dialog_ui.ui'
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

class Ui_ConfirmResetSettingsDialog(object):
    def setupUi(self, ConfirmResetSettingsDialog):
        if not ConfirmResetSettingsDialog.objectName():
            ConfirmResetSettingsDialog.setObjectName(u"ConfirmResetSettingsDialog")
        ConfirmResetSettingsDialog.resize(530, 132)
        self.verticalLayout = QVBoxLayout(ConfirmResetSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ConfirmResetSettingsDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_button = QPushButton(ConfirmResetSettingsDialog)
        self.yes_button.setObjectName(u"yes_button")

        self.horizontalLayout.addWidget(self.yes_button)

        self.no_button = QPushButton(ConfirmResetSettingsDialog)
        self.no_button.setObjectName(u"no_button")

        self.horizontalLayout.addWidget(self.no_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ConfirmResetSettingsDialog)

        QMetaObject.connectSlotsByName(ConfirmResetSettingsDialog)
    # setupUi

    def retranslateUi(self, ConfirmResetSettingsDialog):
        ConfirmResetSettingsDialog.setWindowTitle(QCoreApplication.translate("ConfirmResetSettingsDialog", u"Confirmation restauration", None))
        self.label.setText(QCoreApplication.translate("ConfirmResetSettingsDialog", u"\u00cates-vous sur de vouloirs restaur\u00e9s vos param\u00e8tres par d\u00e9faut ?", None))
        self.yes_button.setText(QCoreApplication.translate("ConfirmResetSettingsDialog", u"Oui", None))
        self.no_button.setText(QCoreApplication.translate("ConfirmResetSettingsDialog", u"Non", None))
    # retranslateUi

