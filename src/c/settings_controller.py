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

from ui.Ui_designer_generated import Ui_PanSearcher
from m.mydatawrapper import MyDataWrapper
from m.SosoSearchCrawler.sosearch import test
class Settings(QDialog, Ui_PanSearcher):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(Settings,self).__init__(parent)
        self.setupUi(self)      
        #self.initData()
        self.initUi()
        
    def initUi(self):
        #QTimer.singleShot(0,self.searchWords,QtCore.SLOT(self.searchWords.setFocus()))
        #self.tblPcsSet.setRowCount(self.maxRowCount);
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
    
    @pyqtSlot()
    def on_btnStartSearch_clicked(self):
        results = test( self.lnedtKeyword.text() )
        if len(results)>0:
            self.populateUiSearchResult(results)
    
    def populateUiSearchResult(self, results):
        self.tblSearchResult.setRowCount(len(results))
        
        pass
'''
url     -> http://pan.baidu.com/share/link?fid=358851085&shareid=4174481751&uk=2
804095996
title   -> ubuntu-13.04-server-i386.iso_免费高速下载|百度云 网盘-分享无限制
content -> 文件名:ubuntu-13.04-server-i386.iso 文件大小:688.66M 分享者:Jiessie_U
ser 分享时间:2013-7-2 17:10 下载次数:406 路径:操作系统/ubuntu/ubuntu-13.04-serve
r-i
'''
    
if __name__ == '__main__': 
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    app = QApplication(sys.argv)
    main_window = Settings()
    #main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec_())
