#
# Import
#

import urllib.request
import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

#
# Check Updates
#

class updates_controller:
    def __init__(self, main_self):
        self.main_self = main_self
        self.releses_json_data = None
        self.main_changelog_widget = None

    def check_updates(self):
        try:
            with urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8/releases') as response:
                if response.getcode() == 200:
                    try:
                        self.releses_json_data = json.loads(response.read().decode())
                    except json.JSONDecodeError:
                        print("Data Load Error")
                else:
                    print(f"Error: {response.getcode()}")
        except Exception as e:
            print(f"Request failed: {e}")

    def setup_changlog_scroll(self):
        self.main_changelog_widget = QWidget(self.main_self.main_changelog_scroll)
        self.main_changelog_widget.setObjectName('main_changelog_widget')
        widget_layout = QVBoxLayout(self.main_changelog_widget)
        widget_layout.setSpacing(0)
        widget_layout.setContentsMargins(0, 0, 0, 0)
        for releses in self.releses_json_data:
            button = QPushButton(self.main_changelog_widget)
            button.setProperty('class', 'main_changelog_button')
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setText(f'{releses["name"]}')


            widget_layout.addWidget(button)
        self.main_changelog_widget.setLayout(widget_layout)

        self.main_self.main_changelog_scroll.setWidget(self.main_changelog_widget)




#-----------------------------------------------------------------------------------------------------------------------

#
# Open Link
#

def open_discord():
    url = QUrl("https://discord.gg/twZ3SNcC")
    QDesktopServices.openUrl(url)

def open_instagram():
    url = QUrl("https://www.instagram.com/codenestgroup/")
    QDesktopServices.openUrl(url)

def open_github():
    url = QUrl("https://github.com/CodeNestGroup")
    QDesktopServices.openUrl(url)


#
# Controllers
#

class controller_settings:
    def __init__(self, main_self):
        self.main_self = main_self

class controller_changlog:
    def __init__(self, main_self):
        self.main_self = main_self
        self.changlog_scroll_widget = None

    def open_hide(self):
        if self.main_self.changlog_widget.isHidden():
            self.main_self.changlog_widget.setHidden(False)
        else:
            self.main_self.changlog_widget.setHidden(True)

    def create_widget(self):
        self.changlog_scroll_widget = QWidget(self.main_self.changelog_scroll)

        changlog_scroll_widget_layout = QVBoxLayout(self.changlog_scroll_widget)
        changlog_scroll_widget_layout.setSpacing(0)
        changlog_scroll_widget_layout.setContentsMargins(0, 0, 0, 0)

        for i in range(1):

            changlog_title_label = QLabel(self.changlog_scroll_widget)
            changlog_date_label = QLabel(self.changlog_scroll_widget)

            changlog_text_label = QLabel(self.changlog_scroll_widget)

            changlog_exit_button = QPushButton(self.changlog_scroll_widget)

#-----------------------------------------------------------------------------------------------------------------------

def open_TickerK8():
    pass

