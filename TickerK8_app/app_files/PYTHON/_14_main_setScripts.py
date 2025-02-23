import json
import os
import time
from datetime import datetime
from webbrowser import open_new

from PyQt5.QtCore import QSize, QRect, QPoint, QParallelAnimationGroup, QSequentialAnimationGroup, QPropertyAnimation, QTimer, Qt, QUrl, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
import pygame
import random

from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from reportlab.lib.pdfencrypt import checkU


#
# Startup
#

def startup(self):
    try:
        startup_connection()
        self.Mode = True
    except:
        self.Mode = False

    if self.Mode:
        self.Login_online_widget.setHidden(False)
        set_news_login(self)
    else:
        self.Login_offline_widget.setHidden(False)

    login_offline_choose_account(self)

#
# Login Online
#

# Login, News, To left #
def login_news_left(self):
    self.login_news_index -= 1
    if self.login_news_index <= -1:
        self.login_news_index = 4
    set_news_login(self)
    buttons_sound()

# Login, News, To right #
def login_news_right(self):
    self.login_news_index += 1
    if self.login_news_index >= 5:
        self.login_news_index = 0
    set_news_login(self)
    buttons_sound()

# Login Online #
def login_script_online(self):
    try:
        user_login = search_login_execute_query(self.Login_log_login_line.text(), self.Login_log_password_line.text(), 'login')
        if user_login:
            self.active_user_id = user_login[0][0]
            self.Login_online_widget.setHidden(True)
            self.Security_widget_main.setHidden(False)
            self.Login_log_login_line.setText("")
            self.Login_log_password_line.setText("")
            Security_restart(self)
            self.user_path = user_login[0][1]
            buttons_sound()
        else:
            self.Login_log_login_line.setText("")
            self.Login_log_password_line.setText("")
            error_sound()
    except:
        self.Login_online_widget.setHidden(True)
        self.Login_offline_widget.setHidden(False)
        self.Mode = False

#
# Login Offline
#

# Login choose account #
def login_offline_choose_account(self):
    layout = QVBoxLayout(self.Login_offline_accounts_widget)
    layout.setSpacing(0)
    layout.setContentsMargins(0, 0, 0, 0)
    for files in os.listdir("../JSON/USERS"):
        user = json.load(open(f"./app_files/JSON/USERS/{files}"))
        button = QPushButton(f"{user['User']['login']}", self.Login_offline_accounts_widget)
        button.setProperty("class", "Notification_account_button")
        button.clicked.connect(lambda: login_offline_open_close_login(self, f"./app_files/JSON/USERS/{files}"))
        layout.addWidget(button)

    self.Login_offline_accounts_widget.setLayout(layout)
    self.Login_offline_accounts_scrollarea.setWidget(self.Login_offline_accounts_widget)
    buttons_sound()

def login_offline_open_close_login(self, path):
    self.Login_offline_password_widget.setGeometry(QRect(0, 0, self.window.size().width(), self.window.size().height()))
    if self.Login_offline_password_widget.isHidden():
        self.Login_offline_password_widget.setHidden(False)
        self.Login_offline_password_line.setText("")
        self.Login_offline_password_line.setPlaceholderText("Offline Password")
    else:
        self.Login_offline_password_widget.setHidden(True)
        self.Login_offline_password_line.setText("")
        self.Login_offline_password_widget.setHidden(True)
    self.user_path = path
    buttons_sound()



def login_script_offline_check(self, path):
    correct_password = json.load(open(path))['User']['offline_password']
    line_password = self.Login_offline_password_line.text()

    if correct_password == line_password:
        self.Login_offline_password_widget.setHidden(True)
        self.Login_offline_widget.setHidden(True)
        self.Security_widget_main.setHidden(False)

        Security_restart(self)
        buttons_sound()
    else:
        self.Login_offline_password_line.setPlaceholderText("Wrong Password")
        error_sound()
        self.Login_offline_password_line.setText("")
#
# Security
#

# Security | Exit #
def security_exit(self):
    if self.Mode:
        self.Login_online_widget.setHidden(False)
    else:
        self.Login_offline_widget.setHidden(False)

    self.Security_widget_main.setHidden(True)
    self.active_user_id = None
    buttons_sound()

# Security | Restart #
def Security_restart(self):
    random_numbers = random.sample(range(0, 51), 3)
    list_cards = ["001-three-of-hearts", "002-ace-of-hearts", "004-six-of-spades", "005-seven-of-spades",
                  "006-eight-of-spades",
                  "007-nine-of-spades", "008-ten-of-spades", "009-jack-of-spades", "010-queen-of-spades",
                  "011-king-of-spades",
                  "012-two-of-hearts", "014-four-of-hearts", "015-five-of-hearts", "016-six-of-hearts",
                  "017-seven-of-hearts",
                  "018-eight-of-hearts", "019-nine-of-hearts", "020-ten-of-hearts", "021-jack-of-hearts",
                  "022-queen-of-hearts",
                  "024-king-of-hearts", "025-ace-of-clubs", "026-two-of-clubs", "027-three-of-clubs",
                  "028-four-of-clubs",
                  "029-five-of-clubs", "030-six-of-clubs", "031-seven-of-clubs", "032-eight-of-clubs",
                  "033-nine-of-clubs",
                  "035-ten-of-clubs", "036-jack-of-clubs", "037-queen-of-clubs", "038-king-of-clubs",
                  "039-ace-of-diamonds",
                  "040-two-of-diamonds", "041-three-of-diamonds", "042-four-of-diamonds", "043-ace-of-spades-1",
                  "044-seven-of-diamonds",
                  "045-eight-of-diamonds", "046-six-of-diamonds", "047-nine-of-diamonds", "048-ten-of-diamonds",
                  "049-five-of-diamonds",
                  "050-jack-of-diamonds", "051-queen-of-diamonds", "052-king-of-diamonds", "057-two-of-spades",
                  "061-three-of-spades",
                  "062-four-of-spades", "064-five-of-spades"]
    self.Security_widget_main_button1.setIcon(QIcon(f"./img/anty_bot/{list_cards[random_numbers[0]]}.png"))
    self.Security_widget_main_button1.setEnabled(False)
    self.Security_widget_main_button2.setIcon(QIcon(f"./img/anty_bot/{list_cards[random_numbers[1]]}.png"))
    self.Security_widget_main_button2.setEnabled(False)
    self.Security_widget_main_button3.setIcon(QIcon(f"./img/anty_bot/{list_cards[random_numbers[2]]}.png"))
    self.Security_widget_main_button3.setEnabled(False)
    self.Security_widget_main_start.setEnabled(True)

# Security | Controller #
def Security_controller(self):
    self.Security_widget_main_start.setEnabled(False)
    self.Security_widget_main_button1.setIcon(QIcon(f"./img/anty_bot/stock.png"))
    self.Security_widget_main_button2.setIcon(QIcon(f"./img/anty_bot/stock.png"))
    self.Security_widget_main_button3.setIcon(QIcon(f"./img/anty_bot/stock.png"))
    combination = random.sample(range(1, 2), 1)[0]
    button_list = [self.Security_widget_main_button1,
                   self.Security_widget_main_button2,
                   self.Security_widget_main_button3]
    positions = self.Login_button_deafult_position
    while combination >= 0:
        random_buttons = random.sample(range(3), 2)
        group_anim = QParallelAnimationGroup()
        anim_1 = QPropertyAnimation(button_list[random_buttons[0]], b"pos")
        anim_1.setDuration(1500)
        anim_2 = QPropertyAnimation(button_list[random_buttons[1]], b"pos")
        anim_2.setDuration(1500)
        anim_1.setEndValue(positions[random_buttons[1]])
        anim_2.setEndValue(positions[random_buttons[0]])
        group_anim.addAnimation(anim_1)
        group_anim.addAnimation(anim_2)
        self.Security_widget_main_anim.addAnimation(group_anim)
        first_pos = positions[random_buttons[0]]
        sec_pos = positions[random_buttons[1]]
        positions[random_buttons[0]] = sec_pos
        positions[random_buttons[1]] = first_pos
        combination -= 1
    self.Security_widget_main_anim.start()
    self.Security_widget_main_anim.finished.connect(lambda: Security_finisched(self))
    buttons_sound()

# Security | Finished #
def Security_finisched(self):
    self.Security_widget_main_button1.setEnabled(True)
    self.Security_widget_main_button2.setEnabled(True)
    self.Security_widget_main_button3.setEnabled(True)

# Security | Failed #
def Security_failed(self):
    while self.Security_widget_main_anim.animationCount() > 0:
        group = self.Security_widget_main_anim.takeAnimation(0)
        group.stop()
        del group
    self.Security_widget_main_start.setEnabled(True)
    self.Security_widget_main_button1.setGeometry(QRect(int(self.new_width * 0.1), int(self.new_height * 0.2), int(self.new_width * 0.2666666666666667), int(self.new_height * 0.6)))
    self.Security_widget_main_button2.setGeometry(QRect(int(self.new_width * 0.3666666666666667), int(self.new_height * 0.2), int(self.new_width * 0.2666666666666667), int(self.new_height * 0.6)))
    self.Security_widget_main_button3.setGeometry(QRect(int(self.new_width * 0.6333333333333334), int(self.new_height * 0.2), int(self.new_width * 0.2666666666666667), int(self.new_height * 0.6)))
    self.login_failed += 1
    if self.login_failed == 5:
        security_exit(self)
        self.login_failed = 0
    Security_restart(self)
    buttons_sound()

# Security | Succes#
def Security_succes(self):
    self.Security_widget_main.setHidden(True)
    self.Main_widget.setHidden(False)
    self.window.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
    self.window.showFullScreen()
    self.window.setFixedSize(self.screen_width, self.screen_height)
    self.fullscreen = True
    buttons_sound()

    main_set_news_photo(self)

    self.news_controller.news_main_create_widget()

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

    self.Main_down_right_button_world.setIcon(QIcon(resize_photo(pix_1, self.Main_down_right_button_world)))
    self.Main_down_right_button_world.setIconSize(self.Main_down_right_button_world.size())
    self.Main_down_right_button_market.setIcon(QIcon(resize_photo(pix_2, self.Main_down_right_button_market)))
    self.Main_down_right_button_market.setIconSize(self.Main_down_right_button_market.size())
    self.Main_down_right_button_country.setIcon(QIcon(resize_photo(pix_3, self.Main_down_right_button_country)))
    self.Main_down_right_button_country.setIconSize(self.Main_down_right_button_country.size())

    self.Main_down_right_label_world.setFixedSize(self.Main_down_right_button_country.size())
    self.Main_down_right_label_market.setFixedSize(self.Main_down_right_button_country.size())
    self.Main_down_right_label_country.setFixedSize(self.Main_down_right_button_country.size())

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
            host='192.168.1.1',
            user='_client',
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
        self._news_main_widget = news_main_widget(self.form, self.main_self.Main_center_right_widget, self.get_news_main())
        self.main_self.Main_center_right_widget_layout.addWidget(self._news_main_widget)
        self.main_self.Main_center_right_deafoult_label.setHidden(True)
