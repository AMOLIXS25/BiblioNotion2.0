# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view_ui.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)
from res import res
from views.library_notes_view import LibraryNotesView
from views.library_view import LibraryView
from views.setting_view import SettingView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 464)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 55))
        self.header_frame.setMaximumSize(QSize(16777215, 55))
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_button = QPushButton(self.frame)
        self.slide_menu_button.setObjectName(u"slide_menu_button")
        self.slide_menu_button.setMinimumSize(QSize(0, 30))
        self.slide_menu_button.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        self.slide_menu_button.setIcon(icon)
        self.slide_menu_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.slide_menu_button)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.header_title_label = QLabel(self.frame_3)
        self.header_title_label.setObjectName(u"header_title_label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.header_title_label.setFont(font)
        self.header_title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.header_title_label)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QCustomSlideMenu(self.frame_2)
        self.slide_menu.setObjectName(u"slide_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slide_menu.sizePolicy().hasHeightForWidth())
        self.slide_menu.setSizePolicy(sizePolicy2)
        self.slide_menu.setMinimumSize(QSize(200, 0))
        self.slide_menu.setMaximumSize(QSize(200, 400))
        self.slide_menu.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.slide_menu)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.slide_menu_content_frame = QFrame(self.slide_menu)
        self.slide_menu_content_frame.setObjectName(u"slide_menu_content_frame")
        sizePolicy1.setHeightForWidth(self.slide_menu_content_frame.sizePolicy().hasHeightForWidth())
        self.slide_menu_content_frame.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.slide_menu_content_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.library_button = QPushButton(self.slide_menu_content_frame)
        self.library_button.setObjectName(u"library_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.library_button.sizePolicy().hasHeightForWidth())
        self.library_button.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        icon1.addFile(u":/images/images/icon_book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.library_button.setIcon(icon1)
        self.library_button.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.library_button)

        self.notes_button = QPushButton(self.slide_menu_content_frame)
        self.notes_button.setObjectName(u"notes_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/icon_note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notes_button.setIcon(icon2)
        self.notes_button.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.notes_button)

        self.settings_button = QPushButton(self.slide_menu_content_frame)
        self.settings_button.setObjectName(u"settings_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon3)
        self.settings_button.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.settings_button)

        self.quit_button = QPushButton(self.slide_menu_content_frame)
        self.quit_button.setObjectName(u"quit_button")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/icon_logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quit_button.setIcon(icon4)
        self.quit_button.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.quit_button)


        self.horizontalLayout_6.addWidget(self.slide_menu_content_frame)


        self.horizontalLayout.addWidget(self.slide_menu)

        self.main_content_frame = QFrame(self.frame_2)
        self.main_content_frame.setObjectName(u"main_content_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.main_content_frame.sizePolicy().hasHeightForWidth())
        self.main_content_frame.setSizePolicy(sizePolicy4)
        self.horizontalLayout_4 = QHBoxLayout(self.main_content_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.notes_page = LibraryNotesView()
        self.main_pages_container = QCustomStackedWidget(self.main_content_frame)
        self.main_pages_container.setObjectName(u"main_pages_container")
        self.library_page = LibraryView(library_note_view=self.notes_page)
        self.library_page.setObjectName(u"library_page")
        self.main_pages_container.addWidget(self.library_page)
        self.notes_page.setObjectName(u"notes_page")
        self.main_pages_container.addWidget(self.notes_page)
        self.settings_page = SettingView()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_3 = QVBoxLayout(self.settings_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.main_pages_container.addWidget(self.settings_page)
        self.quit_page = QWidget()
        self.quit_page.setObjectName(u"quit_page")
        self.label_4 = QLabel(self.quit_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 170, 67, 17))
        self.main_pages_container.addWidget(self.quit_page)

        self.horizontalLayout_4.addWidget(self.main_pages_container)


        self.horizontalLayout.addWidget(self.main_content_frame)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.main_pages_container.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.slide_menu_button.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.header_title_label.setText(QCoreApplication.translate("MainWindow", u"BiblioNotion", None))
        self.library_button.setText(QCoreApplication.translate("MainWindow", u"Biblioth\u00e8que", None))
        self.notes_button.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tre", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quit Page", None))
    # retranslateUi

