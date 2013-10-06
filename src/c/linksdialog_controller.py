# -*- coding: utf-8 -*-

"""
Module implementing Settings.
"""
import os
import sys
#print sys.getdefaultencoding()
from ctypes import *

from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtCore import Qt, QPoint, QTime, QTimer, QTextCodec
from PyQt4.QtCore import QTextDecoder, QByteArray
from PyQt4.QtGui import QApplication, QMainWindow, QTableWidgetItem, QKeyEvent, QTextCursor

#from PyQt4.QtCore import Signal as pyqtSignal
#from PyQt4.QtCore import Slot as pyqtSlot

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
        self.txteditLinks.setReadOnly(True)
        pass
    
    def initData(self):
        pass
    
if __name__ == '__main__': 
    pass
