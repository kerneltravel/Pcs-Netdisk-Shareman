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
from PySide.QtCore import Qt, QPoint, QTime, QTimer, QTextCodec, QTranslator
from PySide.QtCore import QTextDecoder, QByteArray
from PySide.QtGui import QApplication, QMainWindow, QTableWidgetItem, QKeyEvent, QTextCursor

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
