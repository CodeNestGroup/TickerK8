from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QRect, QSize

def set_size_objects(self):

#
# Login
#

    self.Security_exit.setGeometry(0, 0, int(self.new_width * 0.08), int(self.new_height * 0.08))
    self.Security_widget_main_button1.setGeometry(QRect(int(self.new_width * 0.1), int(self.new_height * 0.2), int(self.new_width * 0.2666666666666667), int(self.new_height * 0.6)))
    self.Security_widget_main_button1.setIconSize(QSize(self.Security_widget_main_button1.width(), self.Security_widget_main_button1.height()))
    self.Security_widget_main_button2.setGeometry(QRect(int(self.new_width * 0.3666666666666667), int(self.new_height * 0.2), int(self.new_width * 0.2666666666666667), int(self.new_height * 0.6)))
    self.Security_widget_main_button2.setIconSize(QSize(self.Security_widget_main_button2.width(), self.Security_widget_main_button2.height()))
    self.Security_widget_main_button3.setGeometry(QRect(int(self.new_width * 0.6333333333333334), int(self.new_height * 0.2), int(self.new_width * 0.2666666666666667), int(self.new_height * 0.6)))
    self.Security_widget_main_button3.setIconSize(QSize(self.Security_widget_main_button3.width(), self.Security_widget_main_button3.height()))
    self.Login_button_deafult_position = [self.Security_widget_main_button1.pos(), self.Security_widget_main_button2.pos(), self.Security_widget_main_button3.pos()]
    self.Security_widget_main_start.setGeometry(QRect(int(self.new_width * 0.4), int(self.new_height * 0.825), int(self.new_width * 0.2), int(self.new_height * 0.15)))
# ----------------------------------------------------------------------------------------------------------------------

#
# Main Widget
#

# Main panel center left
    self.Main_center_left_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
# Main panel center center
    self.Main_center_center_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
# Main panel center right
    self.Main_center_right_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

#Main panel down left
    self.Main_down_left_button_news.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.Main_down_left_button_chart.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.Main_down_left_button_stats.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

#Main panel down center
    self.Main_down_center_indi.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.Main_down_center_fore.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

#Main panel down right
    self.Main_down_right_button_world.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.Main_down_right_button_market.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.Main_down_right_button_country.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
# ----------------------------------------------------------------------------------------------------------------------
