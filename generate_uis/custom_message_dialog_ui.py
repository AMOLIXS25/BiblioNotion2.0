# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_message_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_CustomMessageDialog(object):
    def setupUi(self, CustomMessageDialog):
        if not CustomMessageDialog.objectName():
            CustomMessageDialog.setObjectName(u"CustomMessageDialog")
        CustomMessageDialog.resize(353, 119)
        self.verticalLayout = QVBoxLayout(CustomMessageDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CustomMessageDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.ok_button = QPushButton(CustomMessageDialog)
        self.ok_button.setObjectName(u"ok_button")

        self.verticalLayout.addWidget(self.ok_button, 0, Qt.AlignHCenter)


        self.retranslateUi(CustomMessageDialog)

        QMetaObject.connectSlotsByName(CustomMessageDialog)
    # setupUi

    def retranslateUi(self, CustomMessageDialog):
        CustomMessageDialog.setWindowTitle(QCoreApplication.translate("CustomMessageDialog", u"Erreur", None))
        self.label.setText(QCoreApplication.translate("CustomMessageDialog", u"Veuillez s\u00e9lectionner un livre \u00e0 enregistrer  !", None))
        self.ok_button.setText(QCoreApplication.translate("CustomMessageDialog", u"OK", None))
    # retranslateUi

