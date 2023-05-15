# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_view_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from res import res

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        if not SettingWindow.objectName():
            SettingWindow.setObjectName(u"SettingWindow")
        SettingWindow.resize(552, 342)
        self.verticalLayout = QVBoxLayout(SettingWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SettingWindow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.theme_combobox = QComboBox(SettingWindow)
        icon = QIcon()
        icon.addFile(u":/images/images/icon_splash_screen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.theme_combobox.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/icon_elixir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.theme_combobox.addItem(icon1, "")
        self.theme_combobox.setObjectName(u"theme_combobox")

        self.horizontalLayout_2.addWidget(self.theme_combobox)

        self.reload_label = QLabel(SettingWindow)
        self.reload_label.setObjectName(u"reload_label")

        self.horizontalLayout_2.addWidget(self.reload_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(SettingWindow)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.path_directory_txt = QPushButton(SettingWindow)
        self.path_directory_txt.setObjectName(u"path_directory_txt")

        self.verticalLayout.addWidget(self.path_directory_txt, 0, Qt.AlignLeft)

        self.label_3 = QLabel(SettingWindow)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.path_directory_pdf = QPushButton(SettingWindow)
        self.path_directory_pdf.setObjectName(u"path_directory_pdf")

        self.verticalLayout.addWidget(self.path_directory_pdf, 0, Qt.AlignLeft)

        self.label_4 = QLabel(SettingWindow)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.path_directory_cover = QPushButton(SettingWindow)
        self.path_directory_cover.setObjectName(u"path_directory_cover")

        self.verticalLayout.addWidget(self.path_directory_cover, 0, Qt.AlignLeft)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_button = QPushButton(SettingWindow)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.restore_button = QPushButton(SettingWindow)
        self.restore_button.setObjectName(u"restore_button")

        self.horizontalLayout.addWidget(self.restore_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SettingWindow)

        QMetaObject.connectSlotsByName(SettingWindow)
    # setupUi

    def retranslateUi(self, SettingWindow):
        SettingWindow.setWindowTitle(QCoreApplication.translate("SettingWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("SettingWindow", u"Changez theme de l'application : ", None))
        self.theme_combobox.setItemText(0, QCoreApplication.translate("SettingWindow", u"D\u00e9faut", None))
        self.theme_combobox.setItemText(1, QCoreApplication.translate("SettingWindow", u"Purple Drop", None))

        self.reload_label.setText(QCoreApplication.translate("SettingWindow", u"", None))
        self.label_2.setText(QCoreApplication.translate("SettingWindow", u"Changez chemin du dossier par defaut pour l'exportation d'une note en texte :", None))
        self.path_directory_txt.setText(QCoreApplication.translate("SettingWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("SettingWindow", u"Changez chemin du dossier par defaut pour l'exportation d'une note en pdf :", None))
        self.path_directory_pdf.setText(QCoreApplication.translate("SettingWindow", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("SettingWindow", u"Changez le chemin du dossier par d\u00e9faut des couvertures de livres :", None))
        self.path_directory_cover.setText(QCoreApplication.translate("SettingWindow", u"PushButton", None))
        self.save_button.setText(QCoreApplication.translate("SettingWindow", u"Sauvegarder", None))
        self.restore_button.setText(QCoreApplication.translate("SettingWindow", u"Restaurer", None))
    # retranslateUi

