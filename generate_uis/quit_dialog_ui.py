# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quit_dialog_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_QuitDialog(object):
    def setupUi(self, QuitDialog):
        if not QuitDialog.objectName():
            QuitDialog.setObjectName(u"QuitDialog")
        QuitDialog.resize(440, 253)
        self.verticalLayout = QVBoxLayout(QuitDialog)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_container = QFrame(QuitDialog)
        self.top_container.setObjectName(u"top_container")
        self.top_container.setFrameShape(QFrame.StyledPanel)
        self.top_container.setFrameShadow(QFrame.Raised)
        self.aski_quit_label = QLabel(self.top_container)
        self.aski_quit_label.setObjectName(u"aski_quit_label")
        self.aski_quit_label.setGeometry(QRect(10, 10, 401, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aski_quit_label.sizePolicy().hasHeightForWidth())
        self.aski_quit_label.setSizePolicy(sizePolicy)
        self.aski_quit_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.top_container)

        self.bottom_container = QFrame(QuitDialog)
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


        self.verticalLayout.addWidget(self.bottom_container)


        self.retranslateUi(QuitDialog)

        QMetaObject.connectSlotsByName(QuitDialog)
    # setupUi

    def retranslateUi(self, QuitDialog):
        QuitDialog.setWindowTitle(QCoreApplication.translate("QuitDialog", u"Dialog", None))
        self.aski_quit_label.setText(QCoreApplication.translate("QuitDialog", u"\u00cates-vous sur de vouloirs quitt\u00e9s le logiciel ?", None))
        self.yes_button.setText(QCoreApplication.translate("QuitDialog", u"Oui", None))
        self.no_button.setText(QCoreApplication.translate("QuitDialog", u"Non", None))
    # retranslateUi

