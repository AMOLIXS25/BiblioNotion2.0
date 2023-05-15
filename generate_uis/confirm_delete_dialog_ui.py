# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_delete_dialog.ui'
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

class Ui_ConfirmDeleteDialog(object):
    def setupUi(self, ConfirmDeleteDialog):
        if not ConfirmDeleteDialog.objectName():
            ConfirmDeleteDialog.setObjectName(u"ConfirmDeleteDialog")
        ConfirmDeleteDialog.resize(542, 184)
        self.verticalLayout_2 = QVBoxLayout(ConfirmDeleteDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_v_layout = QVBoxLayout()
        self.top_v_layout.setObjectName(u"top_v_layout")
        self.top_label = QLabel(ConfirmDeleteDialog)
        self.top_label.setObjectName(u"top_label")

        self.top_v_layout.addWidget(self.top_label)


        self.verticalLayout_2.addLayout(self.top_v_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.bottom_h_layout = QHBoxLayout()
        self.bottom_h_layout.setObjectName(u"bottom_h_layout")
        self.yes_button = QPushButton(ConfirmDeleteDialog)
        self.yes_button.setObjectName(u"yes_button")

        self.bottom_h_layout.addWidget(self.yes_button)

        self.no_button = QPushButton(ConfirmDeleteDialog)
        self.no_button.setObjectName(u"no_button")

        self.bottom_h_layout.addWidget(self.no_button)


        self.verticalLayout_2.addLayout(self.bottom_h_layout)


        self.retranslateUi(ConfirmDeleteDialog)

        QMetaObject.connectSlotsByName(ConfirmDeleteDialog)
    # setupUi

    def retranslateUi(self, ConfirmDeleteDialog):
        ConfirmDeleteDialog.setWindowTitle(QCoreApplication.translate("ConfirmDeleteDialog", u"Dialog", None))
        self.top_label.setText(QCoreApplication.translate("ConfirmDeleteDialog", u"Souhaitez vous r\u00e9ellement supprimer le livre suivant : ", None))
        self.yes_button.setText(QCoreApplication.translate("ConfirmDeleteDialog", u"oui", None))
        self.no_button.setText(QCoreApplication.translate("ConfirmDeleteDialog", u"non", None))
    # retranslateUi

