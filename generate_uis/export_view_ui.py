# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_view_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from res import res

class Ui_ExportWindow(object):
    def setupUi(self, ExportWindow):
        if not ExportWindow.objectName():
            ExportWindow.setObjectName(u"ExportWindow")
        ExportWindow.resize(236, 162)
        self.verticalLayout = QVBoxLayout(ExportWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pdf_frame = QFrame(ExportWindow)
        self.pdf_frame.setObjectName(u"pdf_frame")
        self.pdf_frame.setFrameShape(QFrame.StyledPanel)
        self.pdf_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.pdf_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.pdf_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.pdf_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/images/images/icon_pdf.png"))

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.pdf_frame)

        self.txt_frame = QFrame(ExportWindow)
        self.txt_frame.setObjectName(u"txt_frame")
        self.txt_frame.setFrameShape(QFrame.StyledPanel)
        self.txt_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.txt_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.txt_frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.txt_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/images/images/icon_txt.png"))

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.txt_frame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.quit_button = QPushButton(ExportWindow)
        self.quit_button.setObjectName(u"quit_button")

        self.verticalLayout.addWidget(self.quit_button)


        self.retranslateUi(ExportWindow)

        QMetaObject.connectSlotsByName(ExportWindow)
    # setupUi

    def retranslateUi(self, ExportWindow):
        ExportWindow.setWindowTitle(QCoreApplication.translate("ExportWindow", u"Exportation", None))
        self.label.setText(QCoreApplication.translate("ExportWindow", u"PDF", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("ExportWindow", u"TXT", None))
        self.label_5.setText("")
        self.quit_button.setText(QCoreApplication.translate("ExportWindow", u"Quitter", None))
    # retranslateUi

