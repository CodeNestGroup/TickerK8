from _14_main_setScripts import *
from _13_Widget_Open_Close import *

def set_Connect_button(self):
#
# Main Page
#

    self.Main_top_button_exit.clicked.connect(self.off)
    self.Main_top_button_window.clicked.connect(lambda: main_page_window(self))
    self.Main_top_button_minimize.clicked.connect(lambda: main_page_minimize(self))
# ----------------------------------------------------------------------------------------------------------------------
