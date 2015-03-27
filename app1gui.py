# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Feb 25 19:09:55 2015
# by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui

from app1methods import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # returns the result of adding a single image to the interface
        def return_result():
            text = add_file()
            self.scrollAreaWidgetContents.append(text)

        # close the interface
        def close_it():
            QtCore.QCoreApplication.instance().quit()

        # returns the result of adding a directory to the interface
        def return_dir_result():
            text = add_directory()
            for i in text:
                self.scrollAreaWidgetContents.append(i)

        # return the result of removing an image to the interface
        def return_delete_image():
            text = delete_image()
            self.scrollAreaWidgetContents.append(text)

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setGeometry(100, 100, 800, 400)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QTextEdit()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 514, 288))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout = QtGui.QVBoxLayout()

        # add image to library button
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_add_image = QtGui.QPushButton(self.centralWidget)
        self.btn_add_image.setObjectName(_fromUtf8("btn_add_image"))
        # add image and display result to gui
        QtCore.QObject.connect(self.btn_add_image, QtCore.SIGNAL(_fromUtf8("clicked()")), return_result)

        # add delete image from library button
        self.verticalLayout.addWidget(self.btn_add_image)
        self.btn_del_image = QtGui.QPushButton(self.centralWidget)
        self.btn_del_image.setObjectName(_fromUtf8("btn_del_image"))
        QtCore.QObject.connect(self.btn_del_image, QtCore.SIGNAL(_fromUtf8("clicked()")), return_delete_image)
        self.verticalLayout.addWidget(self.btn_del_image)

        # add an entire directory to a library
        self.btn_add_directory = QtGui.QPushButton(self.centralWidget)
        self.btn_add_directory.setObjectName(_fromUtf8("btn_add_directory"))
        # add directory to library and display result to gui
        QtCore.QObject.connect(self.btn_add_directory, QtCore.SIGNAL(_fromUtf8("clicked()")), return_dir_result)
        self.verticalLayout.addWidget(self.btn_add_directory)

        # close button
        self.btn_close = QtGui.QPushButton(self.centralWidget)
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        QtCore.QObject.connect(self.btn_close, QtCore.SIGNAL(_fromUtf8("clicked()")), close_it)
        self.verticalLayout.addWidget(self.btn_close)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 658, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Library", None))
        self.btn_add_image.setText(_translate("MainWindow", "Add Image", None))
        self.btn_del_image.setText(_translate("MainWindow", "Delete Image", None))
        self.btn_add_directory.setText(_translate("MainWindow", "Add Directory", None))
        self.btn_close.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

