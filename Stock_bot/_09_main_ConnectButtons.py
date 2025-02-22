from _14_main_setScripts import *
from _13_Widget_Open_Close import *

def set_Connect_button(self):
#
# Login
#

# Login Online Widget #
    self.Login_log_exit_button.clicked.connect(self.off)
    self.Login_log_login_button.clicked.connect(lambda: login_script_online(self))
    self.Login_news_widget_left_button.clicked.connect(lambda: login_news_left(self))
    self.Login_news_widget_right_button.clicked.connect(lambda: login_news_right(self))
# Login Offline Widget #
    self.Login_offline_exit_button.clicked.connect(self.off)
    self.Login_offline_password_exit_button.clicked.connect(lambda: login_offline_open_close_login(self, None))
    self.Login_offline_password_login_button.clicked.connect(lambda: login_script_offline_check(self, self.user_path))
# ----------------------------------------------------------------------------------------------------------------------

#
# Security
#

    self.Security_widget_main_button1.clicked.connect(lambda: Security_failed(self))
    self.Security_widget_main_button2.clicked.connect(lambda: Security_succes(self))
    self.Security_widget_main_button3.clicked.connect(lambda: Security_failed(self))
    self.Security_widget_main_start.clicked.connect(lambda: Security_controller(self))
    self.Security_exit.clicked.connect(lambda: security_exit(self))
# ----------------------------------------------------------------------------------------------------------------------

#
# Main Page
#

    self.Main_top_button_exit.clicked.connect(self.off)
    self.Main_top_button_window.clicked.connect(lambda: main_page_window(self))
    self.Main_top_button_minimize.clicked.connect(lambda: main_page_minimize(self))
# ----------------------------------------------------------------------------------------------------------------------
