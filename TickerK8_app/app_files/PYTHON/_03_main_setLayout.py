def add_widget_to_layout(self):
#
# Main Page
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
# Main Page
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
    pass

def set_Layout_to_Widget(self):
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
