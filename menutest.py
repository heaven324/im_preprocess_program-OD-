# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menutest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 100))
        self.menubar.setObjectName("menubar")
        # tab1
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        # tab2
        self.menutjdgh = QtWidgets.QMenu(self.menubar)
        self.menutjdgh.setObjectName("menutjdgh")
        # tab3
        self.menuzz = QtWidgets.QMenu(self.menubar)
        self.menuzz.setObjectName("menuzz")
        MainWindow.setMenuBar(self.menubar)
        
        # status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # action
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        
        self.actionselect = QtWidgets.QAction(MainWindow)
        self.actionselect.setObjectName("actionselect")
        
        self.actionwjddks = QtWidgets.QAction(MainWindow)
        self.actionwjddks.setObjectName("actionwjddks")
        
        self.actiontjdghwjddks = QtWidgets.QAction(MainWindow)
        self.actiontjdghwjddks.setObjectName("actiontjdghwjddks")
        
        self.actionqq = QtWidgets.QAction(MainWindow)
        self.actionqq.setObjectName("actionqq")
        
        self.actionaa = QtWidgets.QAction(MainWindow)
        self.actionaa.setObjectName("actionaa")
        
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionselect)
        self.menutjdgh.addAction(self.actionwjddks)
        self.menutjdgh.addAction(self.actiontjdghwjddks)
        self.menuzz.addAction(self.actionqq)
        self.menuzz.addAction(self.actionaa)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menutjdgh.menuAction())
        self.menubar.addAction(self.menuzz.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menutjdgh.setTitle(_translate("MainWindow", "tjdgh"))
        self.menuzz.setTitle(_translate("MainWindow", "zz"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionselect.setText(_translate("MainWindow", "select"))
        self.actionwjddks.setText(_translate("MainWindow", "wjddks"))
        self.actiontjdghwjddks.setText(_translate("MainWindow", "tjdghwjddks"))
        self.actionqq.setText(_translate("MainWindow", "qq"))
        self.actionaa.setText(_translate("MainWindow", "aa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

