# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Feb 28 13:52:38 2015
# by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from app2methods import *

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(936, 572)

        # method to clear output text box for new information to be displayed
        def clear_screen():
            self.txt_display.clear()

        # scrape web page or web site depending on which radio button is checked, using url from input box
        def scrape():
            clear_screen()  # clear textual output box
            library_file = get_library_file()
            if self.rb_search_page.isChecked():
                display = scrape_url('{}'.format(self.txt_enter_url.text()), library_file)
            elif self.rb_search_site.isChecked():
                display = scrape_recursive('{}'.format(self.txt_enter_url.text()), 1, library_file)
            # if no matches
            if not display:
                self.txt_display.append('No Matches')
            # output if matches to images found
            else:
                for i in display:
                    self.txt_display.append(i)

        def search_flickr():
            clear_screen()  # clear textual output box
            number_of_images='{}'.format(self.le_no_of_images.text())
            category = '{}'.format(self.le_category.text())

            display = flickr_download(category,number_of_images, get_library_file())
            # if no matches
            if not display:
                self.txt_display.append('No Matches')
            # output if matches to images found
            else:
                for i in display:
                    self.txt_display.append(i)




        # close the interface
        def close_it():
            QtCore.QCoreApplication.instance().quit()

        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)

        # text field for url for scraping
        self.txt_enter_url = QtGui.QLineEdit(self.centralWidget)
        self.txt_enter_url.setObjectName(_fromUtf8("txt_enter_url"))
        self.horizontalLayout.addWidget(self.txt_enter_url)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setMargin(5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))

        # radio buttons for either scraping page or site
        self.rb_search_page = QtGui.QRadioButton(self.centralWidget)
        self.rb_search_page.setChecked(True)
        self.rb_search_page.setObjectName(_fromUtf8("rb_search_page"))
        self.verticalLayout_6.addWidget(self.rb_search_page)
        self.rb_search_site = QtGui.QRadioButton(self.centralWidget)
        self.rb_search_site.setObjectName(_fromUtf8("rb_search_site"))
        self.verticalLayout_6.addWidget(self.rb_search_site)
        self.horizontalLayout.addLayout(self.verticalLayout_6)

        # Search URL button
        self.btn_Search = QtGui.QPushButton(self.centralWidget)
        self.btn_Search.setObjectName(_fromUtf8("btn_Search"))
        self.horizontalLayout.addWidget(self.btn_Search)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked()")), scrape)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.le_no_of_images = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_no_of_images.sizePolicy().hasHeightForWidth())
        self.le_no_of_images.setSizePolicy(sizePolicy)
        self.le_no_of_images.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_4.addWidget(self.le_no_of_images)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.le_category = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_category.sizePolicy().hasHeightForWidth())
        self.le_category.setSizePolicy(sizePolicy)
        self.le_category.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_4.addWidget(self.le_category)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.btn_search_flickr = QtGui.QPushButton(self.centralWidget)
        self.btn_search_flickr.setObjectName(_fromUtf8("btn_search_flickr"))

        QtCore.QObject.connect(self.btn_search_flickr, QtCore.SIGNAL(_fromUtf8("clicked()")), search_flickr)

        self.verticalLayout_4.addWidget(self.btn_search_flickr)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)

        # Close Button
        self.btn_close = QtGui.QPushButton(self.centralWidget)
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        QtCore.QObject.connect(self.btn_close, QtCore.SIGNAL(_fromUtf8("clicked()")), close_it)
        self.verticalLayout_4.addWidget(self.btn_close)

        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.txt_display = QtGui.QTextEdit(self.centralWidget)
        self.txt_display.setReadOnly(True)
        self.txt_display.setObjectName(_fromUtf8("txt_display"))
        self.gridLayout.addWidget(self.txt_display, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 936, 25))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Application 2", None))
        self.label_3.setText(_translate("MainWindow", "Enter URL", None))
        self.rb_search_page.setText(_translate("MainWindow", "Search Page", None))
        self.rb_search_site.setText(_translate("MainWindow", "Search Site", None))
        self.btn_Search.setText(_translate("MainWindow", "Search", None))
        self.label_4.setText(_translate("MainWindow", "FLICKR", None))
        self.label.setText(_translate("MainWindow", "No. of Images", None))
        self.label_2.setText(_translate("MainWindow", "Image Category", None))
        self.btn_search_flickr.setText(_translate("MainWindow", "Search Flickr", None))
        self.btn_close.setText(_translate("MainWindow", "Close", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

