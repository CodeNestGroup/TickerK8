from PyQt5.QtWidgets import QSizePolicy

def set_size_objects(self):
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
