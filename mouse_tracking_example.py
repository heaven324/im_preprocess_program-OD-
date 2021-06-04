# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:28:14 2021

@author: heaven

source : 
https://davey.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python-GUI-%EA%B5%AC%ED%98%84-PyQt5-Mouse-Tracking-%EC%9D%B4%EB%B2%A4%ED%8A%B8?category=838740

"""

import sys
from PyQt5.QtWidgets import *

class Mouse_Location_Tracking(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.statusbar = self.statusBar()
        
        
        self.setMouseTracking(False)
        
        self.setGeometry(500, 200, 500, 400)
        self.show()
        
    def mouseMoveEvent(self, event):
        MouseTracking_Location = "Tracking For Mouse Location ; x axis={0},y axis={1}, global x, y axis={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
        self.statusbar.showMessage(MouseTracking_Location)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Mouse_Location_Tracking()
    sys.exit(app.exec_())
   