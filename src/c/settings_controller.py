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
from PyQt4.QtCore import pyqtSlot, Qt, QPoint, QTime, QTimer, QTextCodec
from PyQt4.QtCore import QTextDecoder, QByteArray
from PyQt4.QtGui import QApplication, QMainWindow, QTableWidgetItem, QKeyEvent, QTextCursor

#from PyQt4.QtCore import Signal as pyqtSignal
#from PyQt4.QtCore import Slot as pyqtSlot

from ui.Ui_designer_generated import Ui_PanSearcher
from m.mydatawrapper import MyDataWrapper
from m.SosoSearchCrawler.sosearch import test
from c.linksdialog_controller import Links_dialog

class Settings(QDialog, Ui_PanSearcher):
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
        #self.tblPcsSet.setRowCount(self.maxRowCount);
        pass
        
    def initData(self):
        self.data = MyDataWrapper("")
        self.linksDialog = None
        self.aboutDialog = None
        self.author = self.tr("kjpioo2006 # gmail.com")
        self.thanksto = self.tr("daimajia and meibenjin")
        self.license = self.tr("MIT license")
        self.ver = "0.1.0"
        self.about = ("A baidu yun file-share download links getter. Version:%s\n\n\tAuthor:%s\n\tThanks to %s\n\n\tLicense: %s"%(self.ver, self.author, self.thanksto, self.license))
        pass

    @pyqtSlot(int)
    def on_ckbxSelectAll_stateChanged(self, stat):
        allCheckState = set([Qt.Unchecked, Qt.Checked])
        #use a workaround for "PyQt4.QtGui.QTableWidgetItem.setCheckState(int)" error
        checkedState = (allCheckState -(allCheckState - set([stat]))).pop()
        #print 'stat:%d'%stat
        for row in range(self.tblSearchResult.rowCount()):
            self.tblSearchResult.item(row, 0 ).setCheckState(checkedState)
        pass
    
    @pyqtSlot()
    def on_btnStartSearch_clicked(self):
        if(self.tblSearchResult.rowCount()>0):
            self.tblSearchResult.clearContents()
        
        results = test( str(self.lnedtKeyword.text().toUtf8()) )
        if len(results)>0:
            self.populateUiSearchResult(results)
            
    @pyqtSlot()
    def on_btnAbout_clicked(self):
        self.aboutDialog = Links_dialog(self.about)
        self.aboutDialog.setWindowTitle(self.tr("About"))
        self.aboutDialog.show()
        pass
    
    @pyqtSlot()
    def on_btnGetLinks_clicked(self):
        if self.tblSearchResult.rowCount()<1:
            return
        links_text = ""
        for row in range(self.tblSearchResult.rowCount()):
            if( self.tblSearchResult.item(row, 0 ).checkState() is Qt.Checked ):
                downloadlink = self.data.getDownloadLink(self.tblSearchResult.item(row, 3).text())
                links_text += (downloadlink['link']+'\n')
                #print links_text
            else:
                print 'row: %d'%row
        self.linksDialog = Links_dialog(links_text.strip())
        self.linksDialog.setWindowTitle(self.tr("Selected Download Links for copying"))
        self.linksDialog.show()
    
    def populateUiSearchResult(self, results):
        self.tblSearchResult.clearContents()
        self.tblSearchResult.setRowCount(len(results))
        for row in range(len(results)):
            newItem = QTableWidgetItem()
            newItem.setCheckState(Qt.Unchecked)
            self.tblSearchResult.setItem(row, 0, newItem)
            
            newTitle = QTableWidgetItem(results[row].getTitle().split("_免费高速下载")[0])
            self.tblSearchResult.setItem(row, 1, newTitle)
            
            print QTableWidgetItem(results[row].getContent())
            filesize = results[row].getContent().split(" 分享者")[0].split(' 文件大小:')[1].strip()
            newDesc = QTableWidgetItem(filesize)
            self.tblSearchResult.setItem(row, 2, newDesc)
            
            newUrl = QTableWidgetItem(results[row].getURL())
            self.tblSearchResult.setItem(row, 3, newUrl)
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
