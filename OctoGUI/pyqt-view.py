from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

from PyQt5.uic import loadUiType

ui, _ = loadUiType('library.ui')

class MainGui(QMainWindow, ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # self.handel_UI_changes()

    def handel_UI_changes(self):
        self.hide_user_input_widget()

    def handel_buttons(self):
        pass

    def show_widget(self):
        pass

    def hide_widget(self):
        pass

    def show_user_input_widget(self):
        self.user_input_data_widget.show()

    def hide_user_input_widget(self):
        self.user_input_data_widget.hide()
    
    def handel_combobox(self):
        self.select_platform_cobobox.select


    #############################################
    ################ ################


    # creating the application - Deprecated
    def window(self):
        # must start with this passing the os info
        app = QApplication(sys.argv)
        # the widgetPp
        win = QMainWindow()
        #  Set size and title of the window (x,y,w,h)
        win.setGeometry(100,100,100,100)
        win.setWindowTitle("First PyQt5 window")
        win.show()
        sys.exit(app.exec_())


def main():
    app = QApplication(sys.argv)
    # Should be in seperate thread
    window = MainGui()
    window.show()
    app.exec_()    

if __name__ == "__main__":
    # os.system(f"pyrcc5 icons.qrc -o icons_rc.py")
    main()




























