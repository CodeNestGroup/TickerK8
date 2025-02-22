def add_widget_to_layout(self):
#
# Form
#

    self.Form_layout.addWidget(self.Login_online_widget)
    self.Form_layout.addWidget(self.Login_offline_widget)
    self.Form_layout.addWidget(self.Security_widget_main)
    self.Form_layout.addWidget(self.Main_widget)
#----------------------------------------------------------------------------------------------------------------------

#
# Login Online
#

    self.Login_online_widget_layout.addWidget(self.Login_log_widget, 0, 0)
    self.Login_online_widget_layout.addWidget(self.Login_news_widget, 0, 1)
# Login Online | Log Widget #
    self.Login_log_widget_layout.addWidget(self.Login_log_exit_button, 0, 0, 6, 100)
    self.Login_log_widget_layout.addWidget(self.Login_log_login_title_label, 20, 0, 20, 100)
    self.Login_log_widget_layout.addWidget(self.Login_log_login_line, 40, 15, 20, 70)
    self.Login_log_widget_layout.addWidget(self.Login_log_password_line, 60, 15, 20, 70)
    self.Login_log_widget_layout.addWidget(self.Login_log_login_button, 80, 25, 20, 50)
# Login Online | News Widget #
    self.Login_news_widget_layout.addWidget(self.Login_news_widget_text_widget)
    self.Login_news_widget_text_widget_layout.addWidget(self.Login_news_widget_text_label, 0, 0, 10, 1)
    self.Login_news_widget_text_widget_layout.addWidget(self.Login_news_widget_next_widget, 10, 0, 1, 1)
    self.Login_news_widget_next_widget_layout.addWidget(self.Login_news_widget_left_button, 0, 1, 1, 5)
    self.Login_news_widget_next_widget_layout.addWidget(self.Login_news_widget_right_button, 0, 37, 1, 5)
#----------------------------------------------------------------------------------------------------------------------

#
# Login Offline
#

# Login Offline | Account Widget
    self.Login_offline_layout.addWidget(self.Login_offline_exit_button, 0, 0, 10, 100)
    self.Login_offline_layout.addWidget(self.Login_offline_title_label, 15, 0, 15, 100)
    self.Login_offline_layout.addWidget(self.Login_offline_accounts_scrollarea, 40, 25, 50, 50)
# Login Offline | Password Widget
    self.Login_offline_password_layout.addWidget(self.Login_offline_main_password_widget, 25, 10, 50, 80)
# Login Offline | Password Widget | Main
    self.Login_offline_main_password_layout.addWidget(self.Login_offline_password_exit_button, 5, 5, 10, 10)
    self.Login_offline_main_password_layout.addWidget(self.Login_offline_password_title_label, 15, 0, 15, 100)
    self.Login_offline_main_password_layout.addWidget(self.Login_offline_password_line, 40, 15, 25, 70)
    self.Login_offline_main_password_layout.addWidget(self.Login_offline_password_login_button, 75, 40, 15, 20)
#----------------------------------------------------------------------------------------------------------------------

#
#
# Main Page
#
#

    self.Main_widget_layout.addWidget(self.Main_top_widget, 0, 0, 8, 100)
    self.Main_widget_layout.addWidget(self.Main_center_widget, 8, 0, 70, 100)
    self.Main_widget_layout.addWidget(self.Main_down_widget, 78, 0, 22, 100)
# Main Page Top Widget
    self.Main_top_widget_layout.addWidget(self.Main_top_button_exit, 35, 5, 30, 3)
    self.Main_top_widget_layout.addWidget(self.Main_top_button_window, 35, 9, 30, 3)
    self.Main_top_widget_layout.addWidget(self.Main_top_button_minimize, 35, 13, 30, 3)
    self.Main_top_widget_layout.addWidget(self.Main_top_button_search_button, 25, 40, 50, 20)
    self.Main_top_widget_layout.addWidget(self.Main_top_button_settings, 35, 93, 30, 3)
# Main Page Center Widget
    self.Main_center_widget_layout.addWidget(self.Main_center_left_label, 0, 0, 100, 30)
    self.Main_center_widget_layout.addWidget(self.Main_center_center_label, 0, 30, 100, 40)
    self.Main_center_widget_layout.addWidget(self.Main_center_right_widget, 0, 70, 100, 30)
# Main Page Center Right Widget
    self.Main_center_right_widget_layout.addWidget(self.Main_center_right_deafoult_label)
# Main Page Down Widget
    self.Main_down_widget_layout.addWidget(self.Main_down_left_widget, 0, 0, 100, 30)
    self.Main_down_widget_layout.addWidget(self.Main_down_center_widget, 0, 30, 100, 40)
    self.Main_down_widget_layout.addWidget(self.Main_down_right_widget, 0, 70, 100, 30)
# Main Page Down Left Widget
    self.Main_down_left_widget_layout.addWidget(self.Main_down_left_button_news, 0, 0)
    self.Main_down_left_widget_layout.addWidget(self.Main_down_left_button_chart, 0, 1)
    self.Main_down_left_widget_layout.addWidget(self.Main_down_left_button_stats, 0, 2)
# Main Page Down Center Widget
    self.Main_down_center_widget_layout.addWidget(self.Main_down_center_indi, 0, 0)
    self.Main_down_center_widget_layout.addWidget(self.Main_down_center_fore, 0, 1)
# Main Page Down Right Widget
    self.Main_down_right_widget_layout.addWidget(self.Main_down_right_button_world, 0, 0)
    self.Main_down_right_widget_layout.addWidget(self.Main_down_right_button_market, 0, 1)
    self.Main_down_right_widget_layout.addWidget(self.Main_down_right_button_country, 0, 2)
#----------------------------------------------------------------------------------------------------------------------

def set_layout_properties(self):
#
# Form
#
    self.Form_layout.setSpacing(0)
    self.Form_layout.setContentsMargins(0, 0, 0, 0)
# ----------------------------------------------------------------------------------------------------------------------

#
# Login
#
    
# Login Online Widget #
    self.Login_online_widget_layout.setSpacing(0)
    self.Login_online_widget_layout.setContentsMargins(0, 0, 0, 0)
    self.Login_log_widget_layout.setSpacing(0)
    self.Login_log_widget_layout.setContentsMargins(0, 0, 0, 0)
    self.Login_news_widget_layout.setSpacing(0)
    self.Login_news_widget_layout.setContentsMargins(0, 0, 0, 0)
    self.Login_news_widget_text_widget_layout.setSpacing(0)
    self.Login_news_widget_text_widget_layout.setContentsMargins(0, 0, 0, 0)
    self.Login_news_widget_text_widget_layout.setSpacing(0)
    self.Login_news_widget_next_widget_layout.setContentsMargins(5, 0, 5, 0)
# Login Offline Widget #
    self.Login_offline_layout.setSpacing(0)
    self.Login_offline_layout.setContentsMargins(0, 0, 0, 0)
# ----------------------------------------------------------------------------------------------------------------------

#
#
# Main Page
#
#
    self.Main_widget_layout.setSpacing(0)
    self.Main_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.Main_widget_layout.setRowStretch(i ,1)
        self.Main_widget_layout.setColumnStretch(i, 1)
#Main panel top
    self.Main_top_widget_layout.setSpacing(0)
    self.Main_top_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.Main_top_widget_layout.setRowStretch(i, 1)
        self.Main_top_widget_layout.setColumnStretch(i, 1)
#Main panel center
    self.Main_center_widget_layout.setSpacing(0)
    self.Main_center_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.Main_center_widget_layout.setRowStretch(i, 1)
        self.Main_center_widget_layout.setColumnStretch(i, 1)
#Main Page Center Right Widget
    self.Main_center_right_widget_layout.setSpacing(0)
    self.Main_center_right_widget_layout.setContentsMargins(0, 0, 0, 0)
#Main panel Down
    self.Main_down_widget_layout.setSpacing(0)
    self.Main_down_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.Main_down_widget_layout.setRowStretch(i, 1)
        self.Main_down_widget_layout.setColumnStretch(i, 1)
# Main Page Down Left
    self.Main_down_left_widget_layout.setSpacing(0)
    self.Main_down_left_widget_layout.setContentsMargins(0, 0, 0, 0)
# Main Page Down Center
    self.Main_down_center_widget_layout.setSpacing(0)
    self.Main_down_center_widget_layout.setContentsMargins(0, 0, 0, 0)
# Main Page Down Right
    self.Main_down_right_widget_layout.setSpacing(0)
    self.Main_down_right_widget_layout.setContentsMargins(0, 0, 0, 0)
# ----------------------------------------------------------------------------------------------------------------------

def set_layout_columnstretch(self):
    #
    # Login
    #

    # Login Online Widget #
    self.Login_online_widget_layout.setColumnStretch(0, 1)
    self.Login_online_widget_layout.setColumnStretch(1, 1)

    # Login Offline Widget #
    self.Login_offline_layout.setRowStretch(10, 5)
    self.Login_offline_layout.setRowStretch(30, 10)
    self.Login_offline_layout.setRowStretch(90, 10)

    self.Login_offline_password_layout.setRowStretch(0, 25)
    self.Login_offline_password_layout.setColumnStretch(0, 10)
    self.Login_offline_password_layout.setRowStretch(75, 25)
    self.Login_offline_password_layout.setColumnStretch(90, 10)

    self.Login_offline_main_password_layout.setRowStretch(0, 5)
    self.Login_offline_main_password_layout.setRowStretch(90, 10)

def set_Layout_to_Widget(self):
#
# Form
#

    self.window.setLayout(self.Form_layout)
# ----------------------------------------------------------------------------------------------------------------------

#
# Login
#

    self.Login_online_widget.setLayout(self.Login_online_widget_layout)
    self.Login_log_widget.setLayout(self.Login_log_widget_layout)
    self.Login_news_widget.setLayout(self.Login_news_widget_layout)
    self.Login_news_widget_text_widget.setLayout(self.Login_news_widget_text_widget_layout)
    self.Login_news_widget_next_widget.setLayout(self.Login_news_widget_next_widget_layout)
# ----------------------------------------------------------------------------------------------------------------------

#
# Main Page
#

    self.Main_widget.setLayout(self.Main_widget_layout)
# Main Page Top
    self.Main_top_widget.setLayout(self.Main_top_widget_layout)
# Main Page Center
    self.Main_center_widget.setLayout(self.Main_center_widget_layout)
# Main Page Center Right Widget
    self.Main_center_right_widget.setLayout(self.Main_center_right_widget_layout)
# Main Page Down
    self.Main_down_widget.setLayout(self.Main_down_widget_layout)
# Main Page Down Left
    self.Main_down_left_widget.setLayout(self.Main_down_left_widget_layout)
# Main Page Down Center
    self.Main_down_center_widget.setLayout(self.Main_down_center_widget_layout)
# Main Page Down Right
    self.Main_down_right_widget.setLayout(self.Main_down_right_widget_layout)
# ----------------------------------------------------------------------------------------------------------------------
