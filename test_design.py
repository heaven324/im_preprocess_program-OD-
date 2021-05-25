# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir

# My Module
import cv_func as cv


class Ui_MainWindow(object):
    def __init__(self):
        self.winx, self.winy = 1500, 960

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(self.winx, self.winy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # directory widget
        self.model = QtWidgets.QFileSystemModel(self.centralwidget)
        self.model.setRootPath(QDir.rootPath())
        self.treeWidget = QtWidgets.QTreeView(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 370, self.winy - 60))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setModel(self.model)
        self.treeWidget.setRootIndex(self.model.index(QDir.currentPath()))
        self.treeWidget.clicked.connect(self.image_event)
        self.dirc = QDir.currentPath() + '/'
        self.fname = ''
        
        
        # image widget  size : 1100x900
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, self.winx - 400, self.winy - 60))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 21))
        self.menubar.setObjectName("menubar")
        # tab1
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        
        # status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage(self.dirc)
        
        
        # QAction
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionopen.triggered.connect(self.MenuAction)
        self.menufile.addAction(self.actionopen)
        self.menubar.addAction(self.menufile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actionopen.setText(_translate("MainWindow", "select directory"))

    def MenuAction(self):
        self.fname = QtWidgets.QFileDialog.getExistingDirectory(None, 'Open directory', './')
        self.treeWidget.setRootIndex(self.model.index(self.fname))
        self.fname = self.fname + '/'
        
    def image_event(self, item):
        data = self.model.itemData(item)
        self.imed = cv.image_edit(self.fname + data[0])
        img, h, w, c = self.imed.im_load() # high, width, channel
        qimg = QtGui.QImage(img, w, h, w*c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.label.setPixmap(pixmap)
        if self.fname == '':
            self.statusbar.showMessage(self.dirc + data[0])
        else:
            self.statusbar.showMessage(self.fname + data[0])
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

