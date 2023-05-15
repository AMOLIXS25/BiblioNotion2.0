# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'no_connection_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from res import res

class Ui_NoConnectionDialog(object):
    def setupUi(self, NoConnectionDialog):
        if not NoConnectionDialog.objectName():
            NoConnectionDialog.setObjectName(u"NoConnectionDialog")
        NoConnectionDialog.resize(535, 326)
        self.verticalLayout = QVBoxLayout(NoConnectionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_container = QFrame(NoConnectionDialog)
        self.top_container.setObjectName(u"top_container")
        self.top_container.setFrameShape(QFrame.StyledPanel)
        self.top_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.top_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.aski_quit_label = QLabel(self.top_container)
        self.aski_quit_label.setObjectName(u"aski_quit_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aski_quit_label.sizePolicy().hasHeightForWidth())
        self.aski_quit_label.setSizePolicy(sizePolicy)
        self.aski_quit_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.aski_quit_label)


        self.verticalLayout.addWidget(self.top_container)

        self.frame = QFrame(NoConnectionDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gif_label = QLabel(self.frame)
        self.gif_label.setObjectName(u"gif_label")
        self.gif_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.gif_label)


        self.verticalLayout.addWidget(self.frame)

        self.checkBox = QCheckBox(NoConnectionDialog)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.bottom_container = QFrame(NoConnectionDialog)
        self.bottom_container.setObjectName(u"bottom_container")
        self.bottom_container.setFrameShape(QFrame.StyledPanel)
        self.bottom_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottom_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_no_button_container = QFrame(self.bottom_container)
        self.yes_no_button_container.setObjectName(u"yes_no_button_container")
        self.yes_no_button_container.setMaximumSize(QSize(300, 16777215))
        self.yes_no_button_container.setFrameShape(QFrame.StyledPanel)
        self.yes_no_button_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.yes_no_button_container)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.yes_button = QPushButton(self.yes_no_button_container)
        self.yes_button.setObjectName(u"yes_button")

        self.horizontalLayout_2.addWidget(self.yes_button)

        self.no_button = QPushButton(self.yes_no_button_container)
        self.no_button.setObjectName(u"no_button")

        self.horizontalLayout_2.addWidget(self.no_button)


        self.horizontalLayout.addWidget(self.yes_no_button_container)


        self.verticalLayout.addWidget(self.bottom_container, 0, Qt.AlignBottom)


        self.retranslateUi(NoConnectionDialog)

        QMetaObject.connectSlotsByName(NoConnectionDialog)
    # setupUi

    def retranslateUi(self, NoConnectionDialog):
        NoConnectionDialog.setWindowTitle(QCoreApplication.translate("NoConnectionDialog", u"Dialog", None))
        self.aski_quit_label.setText(QCoreApplication.translate("NoConnectionDialog", u"Vous n'\u00eates pas connect\u00e9 \u00e0 internet certaines fonctionnalit\u00e9es \n"
" avanc\u00e9es du logiciel  ne seront pas accessibles \n"
" souhaitez-vous tous de m\u00eame continuer ?", None))
        self.gif_label.setText(QCoreApplication.translate("NoConnectionDialog", u"TextLabel", None))
        self.checkBox.setText(QCoreApplication.translate("NoConnectionDialog", u"Ne plus me demander", None))
        self.yes_button.setText(QCoreApplication.translate("NoConnectionDialog", u"Oui", None))
        self.no_button.setText(QCoreApplication.translate("NoConnectionDialog", u"Non", None))
    # retranslateUi

