# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manual_register_book_view_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)
from res import res

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(726, 381)
        self.centralwidget = QWidget(RegisterWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.title)

        self.book_cover_label = QLabel(self.centralwidget)
        self.book_cover_label.setObjectName(u"book_cover_label")

        self.verticalLayout_4.addWidget(self.book_cover_label, 0, Qt.AlignLeft)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")

        self.verticalLayout.addWidget(self.title_label)

        self.title_line_edit = QLineEdit(self.frame)
        self.title_line_edit.setObjectName(u"title_line_edit")

        self.verticalLayout.addWidget(self.title_line_edit)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.author_line_edit = QLineEdit(self.frame)
        self.author_line_edit.setObjectName(u"author_line_edit")

        self.verticalLayout.addWidget(self.author_line_edit)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.status_combo_box = QComboBox(self.frame)
        self.status_combo_box.addItem("")
        self.status_combo_box.addItem("")
        self.status_combo_box.addItem("")
        self.status_combo_box.setObjectName(u"status_combo_box")

        self.verticalLayout.addWidget(self.status_combo_box)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.page_number_spin_box = QSpinBox(self.frame)
        self.page_number_spin_box.setObjectName(u"page_number_spin_box")
        self.page_number_spin_box.setMaximum(10000)

        self.verticalLayout.addWidget(self.page_number_spin_box)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.isbn_line_edit = QLineEdit(self.frame_2)
        self.isbn_line_edit.setObjectName(u"isbn_line_edit")

        self.verticalLayout_2.addWidget(self.isbn_line_edit)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.published_date_line_edit = QLineEdit(self.frame_2)
        self.published_date_line_edit.setObjectName(u"published_date_line_edit")
        self.published_date_line_edit.setReadOnly(False)
        self.published_date_line_edit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.published_date_line_edit.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.published_date_line_edit)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.eval_spin_box = QSpinBox(self.frame_2)
        self.eval_spin_box.setObjectName(u"eval_spin_box")
        self.eval_spin_box.setMaximum(10)

        self.verticalLayout_2.addWidget(self.eval_spin_box)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.hide()

        self.verticalLayout_4.addWidget(self.error_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.register_a_new_book_button = QPushButton(self.centralwidget)
        self.register_a_new_book_button.setObjectName(u"register_a_new_book_button")

        self.horizontalLayout_3.addWidget(self.register_a_new_book_button)

        self.import_book_button = QPushButton(self.centralwidget)
        self.import_book_button.setObjectName(u"import_book_button")
        icon = QIcon()
        icon.addFile(u":/images/images/icon_epub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_book_button.setIcon(icon)
        self.import_book_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.import_book_button)

        self.use_api_button = QPushButton(self.centralwidget)
        self.use_api_button.setObjectName(u"use_api_button")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/smart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.use_api_button.setIcon(icon1)
        self.use_api_button.setIconSize(QSize(20, 20))
        self.use_api_button.setFlat(False)

        self.horizontalLayout_3.addWidget(self.use_api_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("RegisterWindow", u"Enregistrer un livre", None))
        self.book_cover_label.setText(QCoreApplication.translate("RegisterWindow", u"TextLabel", None))
        self.title_label.setText(QCoreApplication.translate("RegisterWindow", u"Titre", None))
        self.label_3.setText(QCoreApplication.translate("RegisterWindow", u"Auteur(s)", None))
        self.label_4.setText(QCoreApplication.translate("RegisterWindow", u"Status de lecture", None))
        self.status_combo_box.setItemText(0, QCoreApplication.translate("RegisterWindow", u"Pas commenc\u00e9", None))
        self.status_combo_box.setItemText(1, QCoreApplication.translate("RegisterWindow", u"En cours de lecture", None))
        self.status_combo_box.setItemText(2, QCoreApplication.translate("RegisterWindow", u"Termin\u00e9", None))

        self.label_5.setText(QCoreApplication.translate("RegisterWindow", u"Nombre de pages", None))
        self.label_6.setText(QCoreApplication.translate("RegisterWindow", u"ISBN", None))
        self.isbn_line_edit.setText("")
        self.label_7.setText(QCoreApplication.translate("RegisterWindow", u"Date de publication", None))
        self.label_8.setText(QCoreApplication.translate("RegisterWindow", u"Evaluation du livre", None))
        self.error_label.setText(QCoreApplication.translate("RegisterWindow", u"TextLabel", None))
        self.register_a_new_book_button.setText(QCoreApplication.translate("RegisterWindow", u"Enregistrer le nouveau livre", None))
        self.import_book_button.setText(QCoreApplication.translate("RegisterWindow", u"Importer un epub", None))
        self.use_api_button.setText(QCoreApplication.translate("RegisterWindow", u"Importer depuis internet", None))
    # retranslateUi

