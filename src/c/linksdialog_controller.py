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

from ui.Ui_links_dialog import Ui_linksDialog
class Links_dialog(QDialog, Ui_linksDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, links_content ,  parent=None):
        super(Links_dialog,self).__init__(parent)
        self.setupUi(self)      
        #self.initData()
        self.initUi(links_content)
        
    def initUi(self, content):
        #QTimer.singleShot(0,self.searchWords,QtCore.SLOT(self.searchWords.setFocus()))
        #self.tblPcsSet.setRowCount(self.maxRowCount);
        self.txteditLinks.setPlainText(content)
        pass
        
    def initData(self):
        pass
    
if __name__ == '__main__': 
    pass
