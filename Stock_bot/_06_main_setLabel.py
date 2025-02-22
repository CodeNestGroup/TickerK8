from PyQt5.QtCore import Qt

def set_Align(self):
#
# Login
#

# Login Online Widget #
    self.Login_log_login_title_label.setAlignment(Qt.AlignCenter)
    self.Login_log_login_line.setAlignment(Qt.AlignCenter)
    self.Login_log_password_line.setAlignment(Qt.AlignCenter)

# Login Offline Widget #
    self.Login_offline_title_label.setAlignment(Qt.AlignCenter)
    self.Login_offline_password_title_label.setAlignment(Qt.AlignCenter)
    self.Login_offline_password_line.setAlignment(Qt.AlignCenter)
# ----------------------------------------------------------------------------------------------------------------------

#
# Main Widget
#

# Main panel Center Left
    self.Main_center_left_label.setAlignment(Qt.AlignCenter)
# Main panel Center center
    self.Main_center_center_label.setAlignment(Qt.AlignCenter)
# Main panel Center right
    self.Main_center_right_deafoult_label.setAlignment(Qt.AlignCenter)

# Main panel down Widget
    self.Main_down_right_label_world.setAlignment(Qt.AlignCenter)
    self.Main_down_right_label_market.setAlignment(Qt.AlignCenter)
    self.Main_down_right_label_country.setAlignment(Qt.AlignCenter)


# ----------------------------------------------------------------------------------------------------------------------
