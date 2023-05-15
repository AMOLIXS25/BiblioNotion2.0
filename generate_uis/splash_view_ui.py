# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_view_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QProgressBar,
    QSizePolicy,
    QWidget,
)
from models.setting import SettingStorage
from res import res


class Ui_SplashScreenWindow(object):
    def setupUi(self, SplashScreenWindow):
        self.setting_storage = SettingStorage()
        if not SplashScreenWindow.objectName():
            SplashScreenWindow.setObjectName("SplashScreenWindow")
        SplashScreenWindow.resize(336, 406)
        self.centralwidget = QWidget(SplashScreenWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName("title_label")
        self.title_label.setGeometry(QRect(110, 240, 131, 21))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.title_label.setFont(font)
        self.loading_progress_bar = QProgressBar(self.centralwidget)
        self.loading_progress_bar.setObjectName("loading_progress_bar")
        self.loading_progress_bar.setGeometry(QRect(20, 320, 291, 20))
        self.loading_progress_bar.setValue(24)
        self.loading_label = QLabel(self.centralwidget)
        self.loading_label.setObjectName("loading_label")
        self.loading_label.setGeometry(QRect(120, 350, 111, 17))
        self.icon_image = QLabel(self.centralwidget)
        self.icon_image.setObjectName("icon_image")
        self.icon_image.setGeometry(QRect(50, 10, 241, 241))
        if self.setting_storage.get_theme("default") == "Défaut":
            self.icon_image.setPixmap(QPixmap(":/images/images/icon_splash_screen.png"))
        elif self.setting_storage.get_theme("default") == "Purple Drop":
            self.icon_image.setPixmap(QPixmap(":/images/images/icon_splash_screen_purple.png"))
        SplashScreenWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreenWindow)

        QMetaObject.connectSlotsByName(SplashScreenWindow)

    # setupUi

    def retranslateUi(self, SplashScreenWindow):
        SplashScreenWindow.setWindowTitle(
            QCoreApplication.translate("SplashScreenWindow", "MainWindow", None)
        )
        self.title_label.setText(
            QCoreApplication.translate("SplashScreenWindow", "BiblioNotion", None)
        )
        self.loading_label.setText(
            QCoreApplication.translate("SplashScreenWindow", "Chargement ...", None)
        )
        self.icon_image.setText("")

    # retranslateUi
