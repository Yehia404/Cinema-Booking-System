# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customerShowMovies.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.titleLabel)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 776, 380))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.moviesList = QVBoxLayout()
        self.moviesList.setObjectName(u"moviesList")

        self.verticalLayout_4.addLayout(self.moviesList)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.rateBtn = QPushButton(self.centralwidget)
        self.rateBtn.setObjectName(u"rateBtn")
        font1 = QFont()
        font1.setPointSize(9)
        self.rateBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.rateBtn)

        self.signoutBtn = QPushButton(self.centralwidget)
        self.signoutBtn.setObjectName(u"signoutBtn")
        self.signoutBtn.setFont(font1)

        self.verticalLayout_2.addWidget(self.signoutBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Movies", None))
        self.rateBtn.setText(QCoreApplication.translate("MainWindow", u"Rate", None))
        self.signoutBtn.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
    # retranslateUi

