#
# Import
#

import json
import os

from PyQt5.QtCore import QSize, QRect, QPoint, QParallelAnimationGroup, QSequentialAnimationGroup, QPropertyAnimation, QTimer, Qt, QUrl, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
import pygame

from PyQt5.QtWidgets import QVBoxLayout, QPushButton
#-----------------------------------------------------------------------------------------------------------------------

def main_page_window(self):
    if self.fullscreen:
        self.window.showNormal()
        self.window.resize(self.new_width, self.new_height)
    else:
        self.window.showFullScreen()

    self.fullscreen = not self.fullscreen

# Main, Minimize #
def main_page_minimize(self):
    self.window.showMinimized()

#
# Sounds
#

# Button Sound
def buttons_sound():
    pygame.mixer.init()  # Initialize the mixer
    sound_file = os.path.abspath("../SOUND/button_clicked.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Notification Sound
def notification_sound():
    pygame.mixer.init()  # Initialize the mixer
    sound_file = os.path.abspath("../SOUND/notification_error.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def error_sound():
    pygame.mixer.init()  # Initialize the mixer
    sound_file = os.path.abspath("../SOUND/error.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

#----------------------------------------------------------------------------------------------------------------------

#
# Resize After Login
#

def resize_photo(photo, button):
    new_width = int(photo.height()*(button.width()/button.height()))
    scaled_pix = photo.copy((photo.width()-new_width) // 2, 0, new_width, photo.height())
    return scaled_pix.scaled(button.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)



def main_set_news_photo(self):
    pix_1 = QPixmap('../PICTURES/UI/earth_background.png')
    pix_2 = QPixmap('../PICTURES/UI/market_background.png')
    pix_3 = QPixmap('../PICTURES/UI/country_background.png')

    self.main_down_right_button_world.setIcon(QIcon(resize_photo(pix_1, self.main_down_right_button_world)))
    self.main_down_right_button_world.setIconSize(self.main_down_right_button_world.size())
    self.main_down_right_button_market.setIcon(QIcon(resize_photo(pix_2, self.main_down_right_button_market)))
    self.main_down_right_button_market.setIconSize(self.main_down_right_button_market.size())
    self.main_down_right_button_country.setIcon(QIcon(resize_photo(pix_3, self.main_down_right_button_country)))
    self.main_down_right_button_country.setIconSize(self.main_down_right_button_country.size())

    self.main_down_right_label_world.setFixedSize(self.main_down_right_button_country.size())
    self.main_down_right_label_market.setFixedSize(self.main_down_right_button_country.size())
    self.main_down_right_label_country.setFixedSize(self.main_down_right_button_country.size())

def animate_icon(animation, target_size):
    #
    pass
#----------------------------------------------------------------------------------------------------------------------

from _15_CustomWidgets import news_main_widget, news_form_widget
import mysql.connector

class news_controller(object):
    def __init__(self, form, main_self):
        self.main_self = main_self
        self.form = form
        self._news_main_widget = None
        self._news_form_widget = None

    def _connect_database(self):
        return mysql.connector.connect(
            host='localhost',
            user='client',
            password='Qwerty123456#',
            database='TickerK8',
        )

    def get_news_main(self):
        _connect = self._connect_database()
        _cursor = _connect.cursor()
        _cursor.execute('SELECT id, json_file FROM news LIMIT 5;')
        _result = _cursor.fetchall()
        _connect.close()
        return _result

    def news_main_create_widget(self):
        #self._news_main_widget = news_main_widget(self.form, self.main_self.Main_center_right_widget, self.get_news_main())
        #self.main_self.Main_center_right_widget_layout.addWidget(self._news_main_widget)
        #self.main_self.Main_center_right_deafoult_label.setHidden(True)
        pass
