# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tmp\baidu\pcs_auto_downloader\pyqt_APPframework_mvc\src\ui\designer_generated.ui'
#
# Created: Mon Sep 30 23:44:01 2013
#      by: pyside-uic 0.2.15 running on PyQt4 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PanSearcher(object):
    def setupUi(self, PanSearcher):
        PanSearcher.setObjectName("PanSearcher")
        PanSearcher.resize(713, 576)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(PanSearcher)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(PanSearcher)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGetLinks = QtGui.QPushButton(self.groupBox)
        self.btnGetLinks.setObjectName("btnGetLinks")
        self.gridLayout.addWidget(self.btnGetLinks, 0, 0, 1, 1)
        self.btnDownSelected = QtGui.QPushButton(self.groupBox)
        self.btnDownSelected.setEnabled(False)
        self.btnDownSelected.setObjectName("btnDownSelected")
        self.gridLayout.addWidget(self.btnDownSelected, 0, 1, 1, 1)
        self.btnAbout = QtGui.QPushButton(self.groupBox)
        self.btnAbout.setObjectName("btnAbout")
        self.gridLayout.addWidget(self.btnAbout, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(PanSearcher)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lnedtKeyword = QtGui.QLineEdit(PanSearcher)
        self.lnedtKeyword.setInputMask("")
        self.lnedtKeyword.setText("")
        self.lnedtKeyword.setObjectName("lnedtKeyword")
        self.horizontalLayout.addWidget(self.lnedtKeyword)
        self.btnStartSearch = QtGui.QPushButton(PanSearcher)
        self.btnStartSearch.setObjectName("btnStartSearch")
        self.horizontalLayout.addWidget(self.btnStartSearch)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ckbxSelectAll = QtGui.QCheckBox(PanSearcher)
        self.ckbxSelectAll.setObjectName("ckbxSelectAll")
        self.horizontalLayout_2.addWidget(self.ckbxSelectAll)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tblSearchResult = QtGui.QTableWidget(PanSearcher)
        self.tblSearchResult.setAutoFillBackground(True)
        self.tblSearchResult.setAlternatingRowColors(True)
        self.tblSearchResult.setShowGrid(False)
        self.tblSearchResult.setObjectName("tblSearchResult")
        self.tblSearchResult.setColumnCount(4)
        self.tblSearchResult.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblSearchResult.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblSearchResult.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblSearchResult.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblSearchResult.setHorizontalHeaderItem(3, item)
        self.tblSearchResult.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tblSearchResult)
        self.lblStatus = QtGui.QLabel(PanSearcher)
        self.lblStatus.setObjectName("lblStatus")
        self.verticalLayout.addWidget(self.lblStatus)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.label_3.setBuddy(self.lnedtKeyword)

        self.retranslateUi(PanSearcher)
        QtCore.QMetaObject.connectSlotsByName(PanSearcher)

    def retranslateUi(self, PanSearcher):
        PanSearcher.setWindowTitle(QtGui.QApplication.translate("PanSearcher", "searcher and downloader for  Netdisk shared files", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGetLinks.setText(QtGui.QApplication.translate("PanSearcher", "Get Links", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDownSelected.setText(QtGui.QApplication.translate("PanSearcher", "download Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAbout.setText(QtGui.QApplication.translate("PanSearcher", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PanSearcher", "find", None, QtGui.QApplication.UnicodeUTF8))
        self.lnedtKeyword.setPlaceholderText(QtGui.QApplication.translate("PanSearcher", "e.g.: ubuntu-12.04.3*.iso", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStartSearch.setText(QtGui.QApplication.translate("PanSearcher", "GO", None, QtGui.QApplication.UnicodeUTF8))
        self.ckbxSelectAll.setText(QtGui.QApplication.translate("PanSearcher", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.tblSearchResult.setSortingEnabled(True)
        self.tblSearchResult.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("PanSearcher", "select", None, QtGui.QApplication.UnicodeUTF8))
        self.tblSearchResult.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("PanSearcher", "name", None, QtGui.QApplication.UnicodeUTF8))
        self.tblSearchResult.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("PanSearcher", "desc.", None, QtGui.QApplication.UnicodeUTF8))
        self.tblSearchResult.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("PanSearcher", "link", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setText(QtGui.QApplication.translate("PanSearcher", "status:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PanSearcher = QtGui.QDialog()
    ui = Ui_PanSearcher()
    ui.setupUi(PanSearcher)
    PanSearcher.show()
    sys.exit(app.exec_())

