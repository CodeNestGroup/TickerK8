#
# Import
#

import urllib.request
import json
import os
import subprocess

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QDesktopServices

#
# File Compatibility Check
#

class file_compatibility_check:
    def __init__(self):
        self.app_path = None

    def tickerk8_compatibility_check(self):
        try:
            self.app_path = os.getcwd()
        except:
            print('Blad otwarcia listy plikow')

#
# Check Updates
#

class updates_controller:
    def __init__(self, main_self):
        self.main_self = main_self
        self.releases_json_data = None
        self.main_changelog_widget = None

    def check_updates(self):
        try:
            with urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8/releases') as response:
                if response.getcode() == 200:
                    try:
                        self.releases_json_data = json.loads(response.read().decode())
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
        for releases in self.releases_json_data:
            button = QPushButton(self.main_changelog_widget)
            button.setProperty('class', 'main_changelog_button')
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setText(f'{releases["name"]}')
            button.clicked.connect(lambda _, r=releases: self.open_changlog(r))

            widget_layout.addWidget(button)
        self.main_changelog_widget.setLayout(widget_layout)

        self.main_self.main_changelog_scroll.setWidget(self.main_changelog_widget)

    def open_changlog(self, release):
        if self.main_self.changlog_widget.isHidden():
            #
            # Create Widget of Changlog
            #

            # Changlog Scroll Widget
            self.changlog_scroll_widget = QWidget(self.main_self.changlog_scroll)
            self.changlog_scroll_widget.setObjectName('changlog_scroll_widget')
#-----------------------------------------------------------------------------------------------------------------------

            # Changlog Scroll Widget Layout
            changlog_scroll_widget_layout = QVBoxLayout(self.changlog_scroll_widget)
            changlog_scroll_widget_layout.setSpacing(0)
            changlog_scroll_widget_layout.setContentsMargins(0,0,0,0)
            self.changlog_scroll_widget.setLayout(changlog_scroll_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

            # Changlog Title
            changlog_title_label = QLabel(self.changlog_scroll_widget)
            changlog_title_label.setObjectName('changlog_title_label')
            changlog_title_label.setText(release['name'])
            changlog_title_label.setAlignment(Qt.AlignCenter)
            changlog_scroll_widget_layout.addWidget(changlog_title_label)
#-----------------------------------------------------------------------------------------------------------------------

            # Changlog Date
            changlog_date_label = QLabel(self.changlog_scroll_widget)
            changlog_date_label.setObjectName('changlog_date_label')
            changlog_date_label.setText(release['published_at'])
            changlog_date_label.setAlignment(Qt.AlignCenter)
            changlog_scroll_widget_layout.addWidget(changlog_date_label)
#-----------------------------------------------------------------------------------------------------------------------

            # Changlog Text
            changlog_text_label = QLabel(self.changlog_scroll_widget)
            changlog_text_label.setObjectName('changlog_text_label')
            changlog_text_label.setText(release['body'])
            changlog_scroll_widget_layout.addWidget(changlog_text_label)
#-----------------------------------------------------------------------------------------------------------------------

            # Changlog Exit
            changlog_exit_button = QPushButton(self.changlog_scroll_widget)
            changlog_exit_button.setObjectName('changlog_exit_button')
            changlog_exit_button.setText('Exit')
            changlog_exit_button.clicked.connect(self.close_changlog)
            changlog_scroll_widget_layout.addWidget(changlog_exit_button)
#-----------------------------------------------------------------------------------------------------------------------

            #
            # Set Widget
            #

            self.main_self.changlog_scroll.setWidget(self.changlog_scroll_widget)
#-----------------------------------------------------------------------------------------------------------------------

            #
            # Set Hidden
            #

            self.main_self.main_widget.setHidden(True)
            self.main_self.changlog_widget.setHidden(False)
#-----------------------------------------------------------------------------------------------------------------------

    def close_changlog(self):
        if not self.main_self.changlog_widget.isHidden() and self.main_self.main_widget.isHidden():
            self.main_self.changlog_widget.setHidden(True)
            self.main_self.main_widget.setHidden(False)
            self.changlog_scroll_widget.deleteLater()

#-----------------------------------------------------------------------------------------------------------------------

#
# Open
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

def open_TickerK8():
    try:
        subprocess.run(['bash', os.getcwd()+'/TickerK8.sh'])
    except:
        print('Linux Fail')
        try:
            subprocess.run([os.getcwd()+'/TickerK8.bat'], shell=True)
        except:
            print('Windows Fail')


#
# Controllers
#

class controller_settings:
    def __init__(self, main_self):
        self.main_self = main_self
#-----------------------------------------------------------------------------------------------------------------------
