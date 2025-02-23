#
# Import
#

import sys
import os
from PyQt5.QtWidgets import *
#-----------------------------------------------------------------------------------------------------------------------

#
# Login Widget
#

class Login_widget(QWidget):
    #
    # Init
    #

    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
        self.main_layout = QGridLayout(self)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Login Widget
        #

        self.login_widget = QWidget(self)
        self.login_widget_layout = QGridLayout(self.login_widget)
        self.login_title_label = QLabel(self.login_widget)
        self.login_login_lineedit = QLineEdit(self.login_widget)
        self.login_password_lineedit = QLineEdit(self.login_widget)
        self.login_login_button = QPushButton(self.login_widget)
        self.login_register_button = QPushButton(self.login_widget)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Register Widget
        #

        self.register_widget = QWidget(self)
        self.register_widget_layout = QGridLayout(self.register_widget)
        self.register_title_label = QLabel(self.register_widget)

        self.register_emial_subtitle_label = QLabel(self.register_widget)
        self.register_emial_lineedit = QLineEdit(self.register_widget)
        self.register_emial_confirm_lineedit = QLineEdit(self.register_widget)

        self.register_phonenumber_subtitle_label = QLabel(self.register_widget)
        self.register_phonenumber_combobox = QComboBox(self.register_widget)
        self.register_phonenumber_lineedit = QLineEdit(self.register_widget)

        self.register_password_subtitle_label = QLabel(self.register_widget)
        self.register_password_lineedit = QLineEdit(self.register_widget)
        self.register_password_confirm_lineedit = QLineEdit(self.register_widget)

        self.register_register_button = QPushButton(self.register_widget)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Setup Login Widget
    #

    def setup_login_widget(self):
        #
        # Import setup functions
        #

        from _01_login_setObjectName import login_setObjectName
        from _02_login_setProperty import login_setProperty
        from _03_login_setLayout import login_setLayout
        from _04_login_setWidget import login_setWidget
        from _05_login_setLineEdit import login_setLineEdit
        from _06_login_setLabel import login_setLabel
        from _07_login_setPushButton import login_setPushButton
        from _08_login_setRetranslate import login_setRetranslate
        from _09_login_setConnectButton import login_setConnectButton
        from _10_login_setGraphics import login_setGraphics
        from _11_login_setAnimation import login_setAnimation
        from _12_login_setSize import login_setSize
        #from _13_login_Scripts import

#-----------------------------------------------------------------------------------------------------------------------

        #
        # Call setup functions
        #

        # setObjectName
        login_setObjectName(self)
        # setProperty
        login_setProperty(self)
        # setLayout
        login_setLayout(self)
        # setWidget
        login_setWidget(self)
        # setLineEdit
        login_setLineEdit(self)
        # setLabel
        login_setLabel(self)
        # setPushButton
        login_setPushButton(self)
        # setRetranslate
        login_setRetranslate(self)
        # setConnectButton
        login_setConnectButton(self)
        # setGraphics
        login_setGraphics(self)
        # setAnimation
        login_setAnimation(self)
        # setSize
        login_setSize(self)
# ----------------------------------------------------------------------------------------------------------------------

#
# Main Widget
#

class Main_widget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
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


#
# Window
#

class Window_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.window_layout = QVBoxLayout()
        self.window_layout.setSpacing(0)
        self.window_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.window_layout)

        self.login_widget = None
        self.main_widget = None

    def open_login_widget(self):
        if not self.login_widget:
            self.login_widget = Login_widget(self)
            self.login_widget.setup_login_widget()
            self.window_layout.addWidget(self.login_widget)
            self.login_widget.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Window_Widget()
    Window.open_login_widget()
    Window.show()
    sys.exit(app.exec_())