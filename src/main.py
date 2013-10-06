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
from PyQt4.QtCore import Qt, QPoint, QTime, QTimer, QTextCodec, QTranslator
from PyQt4.QtCore import QTextDecoder, QByteArray
from PyQt4.QtGui import QApplication, QMainWindow, QTableWidgetItem, QKeyEvent, QTextCursor

from c.settings_controller import Settings

if __name__ == '__main__': 
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    translator = QTranslator()
    translator.load('translations/cn')
    app = QApplication(sys.argv)
    app.installTranslator(translator)
    
    main_window = Settings()
    #main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec_())
