# -*- coding: utf-8 -*-

"""
Module implementing Settings.
"""
import os
import sys
#print sys.getdefaultencoding()
from ctypes import *

from PySide import QtGui
from PySide.QtGui import *
from PySide import QtCore
from PySide.QtCore import Qt, QPoint, QTime, QTimer, QTextCodec
from PySide.QtCore import QTextDecoder, QByteArray
from PySide.QtGui import QApplication, QMainWindow, QTableWidgetItem, QKeyEvent, QTextCursor

from PySide.QtCore import Signal as pyqtSignal
from PySide.QtCore import Slot as pyqtSlot

from ui.Ui_designer_generated import Ui_Settings
from m.mydatawrapper import MyDataWrapper
class Settings(QDialog, Ui_Settings):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(Settings,self).__init__(parent)
        self.setupUi(self)      
        self.initData()
        self.initUi()
        
    def initUi(self):
        #QTimer.singleShot(0,self.searchWords,QtCore.SLOT(self.searchWords.setFocus()))
        self.tblPcsSet.setRowCount(self.maxRowCount);
        pass
        
    def initData(self):
        self.data = MyDataWrapper("hello world!")
        self.curRow = 0
        self.maxRowCount = 10
        pass
        
    @pyqtSlot()
    def on_btnAddPcsApp_clicked(self):
        newItem = QTableWidgetItem( self.data.interface_doSomeThing())
        self.tblPcsSet.setItem(self.curRow, 0, newItem);
        self.curRow += 1
    pass
    
if __name__ == '__main__': 
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    app = QApplication(sys.argv)
    main_window = Settings()
    #main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec_())
