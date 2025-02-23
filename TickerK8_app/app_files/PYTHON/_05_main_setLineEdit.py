from PyQt5.QtWidgets import QLineEdit

def set_Place_Holder(self):
#
# Login Widget
#

    self.Login_log_login_line.setPlaceholderText("USERNAME OR EMAIL")
    self.Login_log_password_line.setPlaceholderText("PASSWORD")
# ----------------------------------------------------------------------------------------------------------------------

def set_Password(self):
#
# Login Widget
#

    self.Login_log_password_line.setEchoMode(QLineEdit.Password)
# ----------------------------------------------------------------------------------------------------------------------
