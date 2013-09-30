# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\tmp\baidu\pcs_auto_downloader\pyqt_APPframework_mvc\src\ui\links_dialog.ui'
#
# Created: Sat Sep 28 22:35:24 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_linksDialog(object):
    def setupUi(self, linksDialog):
        linksDialog.setObjectName("linksDialog")
        linksDialog.resize(661, 518)
        linksDialog.setWindowTitle("")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(linksDialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txteditLinks = QtGui.QPlainTextEdit(linksDialog)
        self.txteditLinks.setObjectName("txteditLinks")
        self.horizontalLayout_3.addWidget(self.txteditLinks)

        self.retranslateUi(linksDialog)
        QtCore.QMetaObject.connectSlotsByName(linksDialog)

    def retranslateUi(self, linksDialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    linksDialog = QtGui.QDialog()
    ui = Ui_linksDialog()
    ui.setupUi(linksDialog)
    linksDialog.show()
    sys.exit(app.exec_())

