# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_register_book_dialog.ui'
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

class Ui_ConfirmRegisterBookDialog(object):
    def setupUi(self, ConfirmRegisterBookDialog):
        if not ConfirmRegisterBookDialog.objectName():
            ConfirmRegisterBookDialog.setObjectName(u"ConfirmRegisterBookDialog")
        ConfirmRegisterBookDialog.resize(501, 150)
        self.horizontalLayout = QHBoxLayout(ConfirmRegisterBookDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout1 = QVBoxLayout()
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.label = QLabel(ConfirmRegisterBookDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout1.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.verticalLayout1)

        self.ok_button = QPushButton(ConfirmRegisterBookDialog)
        self.ok_button.setObjectName(u"ok_button")

        self.verticalLayout_2.addWidget(self.ok_button, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(ConfirmRegisterBookDialog)

        QMetaObject.connectSlotsByName(ConfirmRegisterBookDialog)
    # setupUi

    def retranslateUi(self, ConfirmRegisterBookDialog):
        ConfirmRegisterBookDialog.setWindowTitle(QCoreApplication.translate("ConfirmRegisterBookDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ConfirmRegisterBookDialog", u"Le livre suivant \u00e0 bien \u00e9t\u00e9 enregistrer dans votre biblioth\u00e8que :", None))
        self.ok_button.setText(QCoreApplication.translate("ConfirmRegisterBookDialog", u"OK", None))
    # retranslateUi

