#
# Import
#

import sys
import os

from PyQt5.QtCore import QPauseAnimation, QRect
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QScrollArea, QPushButton
from PyQt5.QtGui import QGuiApplication

# setup_Ui #
from _01_main_setObjectName import *
from _02_main_setProperty import *
from _03_main_setLayout import *
from _04_main_setWidget import *
from _05_main_setScrollArea import *
from _06_main_setLabel import *
from _07_main_setPushButton import *
from _08_main_setConnect import *
from _09_main_setGraphics import *
from _10_main_setSize import *
from _11_main_setText import *
from _12_main_setCss import *
from _13_main_Scripts import *

#-----------------------------------------------------------------------------------------------------------------------

#
# Main Window | Create
#

class Main_window(QWidget):

    #
    # Init
    #

    def __init__(self):
        #
        # Self Setup
        #

        super().__init__()
        self.setWindowTitle('TickerK8 Launcher')
        self.screen_size = QGuiApplication.primaryScreen().size()
        self.file_app_path = os.path.dirname(os.path.abspath(__file__))

#-----------------------------------------------------------------------------------------------------------------------
        #
        # Self Items
        #

        # Self
        self.layout = QVBoxLayout(self)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Main Widget
        #

        self.main_widget = QWidget(self)
        self.main_widget_layout = QGridLayout(self.main_widget)
        self.main_changelog_scroll = QScrollArea(self.main_widget)
        self.main_settings_widget = QWidget(self.main_widget)
        self.main_settings_widget_layout = QGridLayout(self.main_settings_widget)
        self.main_settings_open_button = QPushButton(self.main_settings_widget)
        self.main_settings_social_media_instagram_button = QPushButton(self.main_settings_widget)
        self.main_settings_social_media_github_button = QPushButton(self.main_settings_widget)
        self.main_settings_social_media_discord_button = QPushButton(self.main_settings_widget)
        self.main_update_widget = QWidget(self.main_widget)
        self.main_start_button = QPushButton(self.main_widget)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Changelog Widget
        #

        self.changlog_widget = QWidget(self)
        self.changlog_widget_layout = QGridLayout(self.changlog_widget)
        self.changlog_scroll = QScrollArea(self.changlog_widget)

#-----------------------------------------------------------------------------------------------------------------------

        #
        # Settings Widget
        #

        self.settings_widget = QWidget(self)
        self.settings_widget_layout = QGridLayout(self.settings_widget)
        self.settings_menu_scroll = QScrollArea(self.settings_widget)
        self.settings_menu_scroll_widget = QWidget(self.settings_menu_scroll)
        self.settings_menu_scroll_widget_layout = QGridLayout(self.settings_menu_scroll_widget)

#-----------------------------------------------------------------------------------------------------------------------

        self.updates_controller = updates_controller(self)
        self.updates_controller.check_updates()
        self.updates_controller.setup_changlog_scroll()

        self.open_instagram = lambda: open_instagram()
        self.open_github = lambda: open_github()
        self.open_discord = lambda: open_discord()
        self.open_TickerK8 = lambda: open_TickerK8()

    #
    # Setup
    #

    # Set Object Name
    def set_object_name(self):
        set_ObjectName(self)

    # Set Property
    def set_property(self):
        set_Property(self)

    # Set Layout
    def set_layout(self):
        set_Layout(self)

    # Set Size
    def set_size(self):
        set_Size(self)

    # Set Widget
    def set_widget(self):
        set_Widget(self)

    # Set Scroll Area
    def set_scroll_area(self):
        set_ScrollArea(self)

    # Set Label
    def set_label(self):
        set_Label(self)

    # Set Push Button
    def set_pushbutoon(self):
        set_PushButton(self)

    # Set Connect
    def set_connect(self):
        set_Connect(self)

    # Set Grpahics
    def set_graphics(self):
        set_Graphics(self)

    # Set Text
    def set_text(self):
        set_Text(self)

    # Set Css
    def set_css(self):
        set_Css(self, 'default_light')
#-----------------------------------------------------------------------------------------------------------------------

#
# Start App
#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    window.set_object_name()
    window.set_property()
    window.set_layout()
    window.set_size()
    window.set_widget()
    window.set_scroll_area()
    window.set_label()
    window.set_pushbutoon()
    window.set_connect()
    window.set_graphics()
    window.set_text()
    window.set_css()
    sys.exit(app.exec_())
