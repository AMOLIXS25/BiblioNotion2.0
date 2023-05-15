# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_update_dialog.ui'
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
from res import res

class Ui_ConfirmUpdateDialog(object):
    def setupUi(self, ConfirmUpdateDialog):
        if not ConfirmUpdateDialog.objectName():
            ConfirmUpdateDialog.setObjectName(u"ConfirmUpdateDialog")
        ConfirmUpdateDialog.resize(576, 234)
        self.verticalLayout = QVBoxLayout(ConfirmUpdateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ConfirmUpdateDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(ConfirmUpdateDialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.old_book_frame = QFrame(self.frame_2)
        self.old_book_frame.setObjectName(u"old_book_frame")
        self.old_book_frame.setStyleSheet(u"")
        self.old_book_frame.setFrameShape(QFrame.StyledPanel)
        self.old_book_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.old_book_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.old_book_layout = QVBoxLayout()
        self.old_book_layout.setObjectName(u"old_book_layout")

        self.horizontalLayout_4.addLayout(self.old_book_layout)


        self.horizontalLayout.addWidget(self.old_book_frame)

        self.arrow_label = QLabel(self.frame_2)
        self.arrow_label.setObjectName(u"arrow_label")
        font1 = QFont()
        font1.setPointSize(20)
        self.arrow_label.setFont(font1)
        self.arrow_label.setPixmap(QPixmap(u":/images/images/arrow_right.png"))
        self.arrow_label.setScaledContents(False)
        self.arrow_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.arrow_label)

        self.new_book_frame = QFrame(self.frame_2)
        self.new_book_frame.setObjectName(u"new_book_frame")
        self.new_book_frame.setFrameShape(QFrame.StyledPanel)
        self.new_book_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.new_book_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.new_book_layout = QVBoxLayout()
        self.new_book_layout.setObjectName(u"new_book_layout")

        self.horizontalLayout_3.addLayout(self.new_book_layout)


        self.horizontalLayout.addWidget(self.new_book_frame)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(ConfirmUpdateDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.confirm_button = QPushButton(self.frame_3)
        self.confirm_button.setObjectName(u"confirm_button")

        self.horizontalLayout_2.addWidget(self.confirm_button)

        self.annul_button = QPushButton(self.frame_3)
        self.annul_button.setObjectName(u"annul_button")

        self.horizontalLayout_2.addWidget(self.annul_button)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(ConfirmUpdateDialog)

        QMetaObject.connectSlotsByName(ConfirmUpdateDialog)
    # setupUi

    def retranslateUi(self, ConfirmUpdateDialog):
        ConfirmUpdateDialog.setWindowTitle(QCoreApplication.translate("ConfirmUpdateDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ConfirmUpdateDialog", u"Livre modifi\u00e9 avec success  !", None))
        self.arrow_label.setText("")
        self.confirm_button.setText(QCoreApplication.translate("ConfirmUpdateDialog", u"Confirmer les modifications", None))
        self.annul_button.setText(QCoreApplication.translate("ConfirmUpdateDialog", u"Annuler les modifications", None))
    # retranslateUi

