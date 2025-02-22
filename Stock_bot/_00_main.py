#!/usr/bin/env python3
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from reportlab.graphics.barcode.qrencoder import QRMaskPattern
from timezonefinder import TimezoneFinder
import mysql.connector


class Login_widget(QWidget):
    def __init__(self):
        super().__init__()
#
# Login Widget
#

# Login Online Widget #
        self.Login_online_widget = QWidget(Form)
        self.Login_online_widget_layout = QGridLayout(self.Login_online_widget)
# Login Online Widget | Left Widget #
        self.Login_log_widget = QWidget(self.Login_online_widget)
        self.Login_log_widget_layout = QGridLayout(self.Login_log_widget)
        self.Login_log_exit_button = QPushButton(self.Login_log_widget)
        self.Login_log_login_title_label = QLabel(self.Login_log_widget)
        self.Login_log_login_line = QLineEdit(self.Login_log_widget)
        self.Login_log_password_line = QLineEdit(self.Login_log_widget)
        self.Login_log_login_button = QPushButton(self.Login_log_widget)
# Login Widget | Right Widget #
        self.Login_news_widget = QWidget(self.Login_online_widget)
        self.Login_news_widget_layout = QVBoxLayout(self.Login_news_widget)
        self.Login_news_widget_text_widget = QWidget(self.Login_news_widget)
        self.Login_news_widget_text_widget_layout = QGridLayout(self.Login_news_widget_text_widget)
        self.Login_news_widget_text_label = QLabel(self.Login_news_widget_text_widget)
        self.Login_news_widget_next_widget = QWidget(self.Login_news_widget_text_widget)
        self.Login_news_widget_next_widget_layout = QGridLayout(self.Login_news_widget_next_widget)
        self.Login_news_widget_left_button = QPushButton(self.Login_news_widget_next_widget)
        self.Login_news_widget_right_button = QPushButton(self.Login_news_widget_next_widget)
# Login Offline Widget #
        self.Login_offline_widget = QWidget(Form)
        self.Login_offline_layout = QGridLayout(self.Login_offline_widget)
        self.Login_offline_title_label = QLabel(self.Login_offline_widget)
        self.Login_offline_exit_button = QPushButton(self.Login_offline_widget)
        self.Login_offline_accounts_scrollarea = QScrollArea(self.Login_offline_widget)
        self.Login_offline_accounts_widget = QWidget(self.Login_offline_accounts_scrollarea)
# Notification Password Widget #
        self.Login_offline_password_widget = QWidget(Form)
        self.Login_offline_password_layout = QGridLayout(self.Login_offline_password_widget)
        self.Login_offline_main_password_widget = QWidget(self.Login_offline_password_widget)
        self.Login_offline_main_password_layout = QGridLayout(self.Login_offline_main_password_widget)
        self.Login_offline_password_exit_button = QPushButton(self.Login_offline_main_password_widget)
        self.Login_offline_password_title_label = QLabel(self.Login_offline_main_password_widget)
        self.Login_offline_password_line = QLineEdit(self.Login_offline_main_password_widget)
        self.Login_offline_password_login_button = QPushButton(self.Login_offline_main_password_widget)
# Security Widget #
        self.Security_widget_main = QWidget(Form)
        self.Security_widget_main_button1 = QPushButton(self.Security_widget_main)
        self.Security_widget_main_button1_anim = QPropertyAnimation(self.Security_widget_main_button1, b"pos")
        self.Security_widget_main_button2 = QPushButton(self.Security_widget_main)
        self.Security_widget_main_button2_anim = QPropertyAnimation(self.Security_widget_main_button2, b"pos")
        self.Security_widget_main_button3 = QPushButton(self.Security_widget_main)
        self.Security_widget_main_button3_anim = QPropertyAnimation(self.Security_widget_main_button3, b"pos")
        self.Security_widget_main_anim = QSequentialAnimationGroup(self.Security_widget_main)
        self.Security_widget_main_start = QPushButton(self.Security_widget_main)
        self.Security_exit = QPushButton(self.Security_widget_main)
# ----------------------------------------------------------------------------------------------------------------------


class Main_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.screen = QApplication.primaryScreen()
        self.screen_size = self.screen.size()
        self.screen_width = self.screen_size.width()
        self.screen_height = self.screen_size.height()
        self.new_width = int(self.screen_width * 0.3854166666666667)
        self.new_height = int(self.screen_height * 0.4916666666666667)

        self.Mode = False
        self.fullscreen = False
        self.window = None
#
# Main panel
#
        self.Main_widget = QWidget(Form)
        self.Main_widget_layout = QGridLayout(self.Main_widget)
# Main panel Top Widget
        self.Main_top_widget = QWidget(self.Main_widget)
        self.Main_top_widget_layout = QGridLayout(self.Main_top_widget)
        self.Main_top_button_exit = QPushButton(self.Main_top_widget)
        self.Main_top_button_window = QPushButton(self.Main_top_widget)
        self.Main_top_button_minimize = QPushButton(self.Main_top_widget)
        self.Main_top_button_search_button = QPushButton(self.Main_top_widget)
        self.Main_top_button_settings = QPushButton(self.Main_top_widget)
# Main panel Center Widget
        self.Main_center_widget = QWidget(self.Main_widget)
        self.Main_center_widget_layout = QGridLayout(self.Main_center_widget)
# Main panel Center Left
        self.Main_center_left_label = QLabel(self.Main_center_widget)
# Main panel Center center
        self.Main_center_center_label = QLabel(self.Main_center_widget)
# Main panel Center right
        self.Main_center_right_widget = QWidget(self.Main_center_widget)
        self.Main_center_right_widget_layout = QVBoxLayout(self.Main_center_right_widget)
        self.Main_center_right_deafoult_label = QLabel(self.Main_center_right_widget)
# Main panel down Widget
        self.Main_down_widget = QWidget(self.Main_widget)
        self.Main_down_widget_layout = QGridLayout(self.Main_down_widget)
        self.Main_down_left_widget = QWidget(self.Main_down_widget)
        self.Main_down_left_widget_layout = QGridLayout(self.Main_down_left_widget)
        self.Main_down_left_button_news = QPushButton(self.Main_down_left_widget)
        self.Main_down_left_button_chart = QPushButton(self.Main_down_left_widget)
        self.Main_down_left_button_stats = QPushButton(self.Main_down_left_widget)
        self.Main_down_center_widget = QWidget(self.Main_down_widget)
        self.Main_down_center_widget_layout = QGridLayout(self.Main_down_center_widget)
        self.Main_down_center_indi = QPushButton(self.Main_down_center_widget)
        self.Main_down_center_fore = QPushButton(self.Main_down_center_widget)
        self.Main_down_right_widget = QWidget(self.Main_down_widget)
        self.Main_down_right_widget_layout = QGridLayout(self.Main_down_right_widget)
        self.Main_down_right_button_world = QPushButton(self.Main_down_right_widget)
        self.Main_down_right_label_world = QLabel(self.Main_down_right_button_world)
        self.Main_down_right_button_market = QPushButton(self.Main_down_right_widget)
        self.Main_down_right_label_market = QLabel(self.Main_down_right_button_market)
        self.Main_down_right_button_country = QPushButton(self.Main_down_right_widget)
        self.Main_down_right_label_country = QLabel(self.Main_down_right_button_country)
# ----------------------------------------------------------------------------------------------------------------------

    def setupUi(self, form):
        from _01_main_setObjectName import set_object_name
        from _02_main_setProperty import set_Property_objects
        from _03_main_setLayout import add_widget_to_layout, set_layout_properties, set_layout_columnstretch, set_Layout_to_Widget
        from _04_main_setWidget import set_widget_hidden, set_scroll_resizable, set_widget_to_scroll, set_Widget_wrap
        from _05_main_setLineEdit import set_Place_Holder, set_Password
        from _06_main_setLabel import set_Align
        from _07_setPushButton import set_button_disabled
        from _08_main_setRetranslate import retranslate
        from _09_main_ConnectButtons import set_Connect_button
        from _10_main_setGraphics import set_label_graphic
        from _11_main_setSize import set_size_objects
        from _12_main_setAnimation import set_Add_Anim, set_Duration, set_curve
        from _14_main_setScripts import startup, news_controller


        self.window = form
        self.window.setObjectName("Form")
        # Ustaw nowy rozmiar okna
        self.window.resize(self.new_width, self.new_height)
        self.window.setWindowFlag(Qt.FramelessWindowHint)
        self.window.setWindowTitle("STOCK BOT")
        self.news_controller = news_controller(form, self)
        #Set ObjectName
        set_object_name(self)
        #Set Property
        set_Property_objects(self)
        # Set Layout
        add_widget_to_layout(self)
        set_layout_properties(self)
        set_layout_columnstretch(self)
        set_Layout_to_Widget(self)
        # Set Widget
        set_widget_hidden(self)
        set_scroll_resizable(self)
        set_widget_to_scroll(self)
        set_Widget_wrap(self)
        # Set Line Edit
        set_Place_Holder(self)
        set_Password(self)
        # Set Label
        set_Align(self)
        # Set Push Butoon
        set_button_disabled(self)
        # Retranslate
        retranslate(self)
        # Connect Buttons
        set_Connect_button(self)
        # Set Graphics
        set_label_graphic(self)
        # Set Size
        set_size_objects(self)
        # Set Animation
        set_Add_Anim(self)
        set_Duration(self)
        set_curve(self)
        # Set Combo Box
        startup(self)
        QtCore.QMetaObject.connectSlotsByName(self.window)

    @staticmethod
    def off():
        sys.exit(app.exec_())
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login_widget()
    app.setStyleSheet(open('CSS/_main_day_css.css').read())
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
