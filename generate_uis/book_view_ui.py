# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_view_ui.ui'
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

class Ui_ViewBookWindow(object):
    def setupUi(self, ViewBookWindow):
        if not ViewBookWindow.objectName():
            ViewBookWindow.setObjectName(u"ViewBookWindow")
        ViewBookWindow.resize(503, 272)
        self.verticalLayout = QVBoxLayout(ViewBookWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.book_picture_label = QLabel(ViewBookWindow)
        self.book_picture_label.setObjectName(u"book_picture_label")

        self.verticalLayout.addWidget(self.book_picture_label)

        self.book_title_label = QLabel(ViewBookWindow)
        self.book_title_label.setObjectName(u"book_title_label")

        self.verticalLayout.addWidget(self.book_title_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.book_authors_label = QLabel(ViewBookWindow)
        self.book_authors_label.setObjectName(u"book_authors_label")

        self.horizontalLayout.addWidget(self.book_authors_label)

        self.book_types_label = QLabel(ViewBookWindow)
        self.book_types_label.setObjectName(u"book_types_label")

        self.horizontalLayout.addWidget(self.book_types_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame = QFrame(ViewBookWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(ViewBookWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.book_isbn_label = QLabel(ViewBookWindow)
        self.book_isbn_label.setObjectName(u"book_isbn_label")

        self.horizontalLayout_5.addWidget(self.book_isbn_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.book = QLabel(ViewBookWindow)
        self.book.setObjectName(u"book")

        self.horizontalLayout_4.addWidget(self.book)

        self.book_pages_label = QLabel(ViewBookWindow)
        self.book_pages_label.setObjectName(u"book_pages_label")

        self.horizontalLayout_4.addWidget(self.book_pages_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(ViewBookWindow)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.book_status_label = QLabel(ViewBookWindow)
        self.book_status_label.setObjectName(u"book_status_label")

        self.horizontalLayout_3.addWidget(self.book_status_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(ViewBookWindow)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.book_eval_label = QLabel(ViewBookWindow)
        self.book_eval_label.setObjectName(u"book_eval_label")

        self.horizontalLayout_2.addWidget(self.book_eval_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.export_book_button = QPushButton(ViewBookWindow)
        self.export_book_button.setObjectName(u"export_book_button")

        self.horizontalLayout_6.addWidget(self.export_book_button)

        self.quit_button = QPushButton(ViewBookWindow)
        self.quit_button.setObjectName(u"quit_button")

        self.horizontalLayout_6.addWidget(self.quit_button)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(ViewBookWindow)

        QMetaObject.connectSlotsByName(ViewBookWindow)
    # setupUi

    def retranslateUi(self, ViewBookWindow):
        ViewBookWindow.setWindowTitle("")
        self.book_picture_label.setText(QCoreApplication.translate("ViewBookWindow", u"Image", None))
        self.book_title_label.setText(QCoreApplication.translate("ViewBookWindow", u"Titre du livre sel", None))
        self.book_authors_label.setText(QCoreApplication.translate("ViewBookWindow", u"TextLabel", None))
        self.book_types_label.setText("")
        self.label.setText(QCoreApplication.translate("ViewBookWindow", u"ISBN : ", None))
        self.book_isbn_label.setText(QCoreApplication.translate("ViewBookWindow", u"TextLabel", None))
        self.book.setText(QCoreApplication.translate("ViewBookWindow", u"Nombre de pages : ", None))
        self.book_pages_label.setText(QCoreApplication.translate("ViewBookWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("ViewBookWindow", u"Etat : ", None))
        self.book_status_label.setText(QCoreApplication.translate("ViewBookWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("ViewBookWindow", u"Evaluation : ", None))
        self.book_eval_label.setText(QCoreApplication.translate("ViewBookWindow", u"TextLabel", None))
        self.export_book_button.setText(QCoreApplication.translate("ViewBookWindow", u"Exporter les notes du livre", None))
        self.quit_button.setText(QCoreApplication.translate("ViewBookWindow", u"Quitter", None))
    # retranslateUi

