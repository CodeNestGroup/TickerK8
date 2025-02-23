from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5.QtCore import QSize

def set_label_graphic(self):
#
# Login Online
#

# Login Online Widget | Log Widget #
    self.Login_log_exit_button.setIcon(QIcon("./img/main_graphics/exit.svg"))
# Login Online Widget | News Widget #
    self.Login_news_widget_left_button.setIcon(QIcon("./img/main_graphics/angle-small-left.svg"))
    self.Login_news_widget_right_button.setIcon(QIcon("./img/main_graphics/angle-small-right.svg"))
# ----------------------------------------------------------------------------------------------------------------------

#
# Login Offline
#

# Login Offline Widget | Account #
    self.Login_offline_exit_button.setIcon(QIcon("./img/main_graphics/exit.svg"))
# Login Offline Widget | Password #
    self.Login_offline_password_exit_button.setIcon(QIcon("./img/main_graphics/exit.svg"))
# ----------------------------------------------------------------------------------------------------------------------

#
# Security
#

    self.Security_exit.setIcon(QIcon("./img/main_graphics/exit.svg"))
# ----------------------------------------------------------------------------------------------------------------------

#
# Main Widget
#

#Main Page Top
    self.Main_top_button_exit.setIcon(QIcon("../ICONS/UI/exit-alt.png"))
    self.Main_top_button_window.setIcon(QIcon("../ICONS/UI/expand.png"))
    self.Main_top_button_minimize.setIcon(QIcon("../ICONS/UI/down-left-and-up-right-to-center.png"))
    self.Main_top_button_search_button.setIcon(QIcon("../ICONS/UI/analyse-alt.png"))
    self.Main_top_button_settings.setIcon(QIcon("../ICONS/UI/settings-sliders.png"))
# Main panel Center right
    self.Main_center_right_deafoult_label.setPixmap(QPixmap('../ICONS/UI/newspaper.png'))
#Main Page Down
#Left
    self.Main_down_left_button_news.setIcon(QIcon("./img/main_graphics/newspaper.svg"))
    self.Main_down_left_button_chart.setIcon(QIcon("./img/main_graphics/chart-mixed-up-circle-dollar.svg"))
    self.Main_down_left_button_stats.setIcon(QIcon("./img/main_graphics/chart-pie-alt.svg"))
#Center
    self.Main_down_center_indi.setIcon(QIcon("./img/main_graphics/fuel-gauge.svg"))
    self.Main_down_center_fore.setIcon(QIcon("./img/main_graphics/cloud-sun-rain.svg"))
#Right
# ----------------------------------------------------------------------------------------------------------------------
