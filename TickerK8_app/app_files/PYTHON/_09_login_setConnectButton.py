#
# Import
#

from _13_login_Scripts import show_hide_login_register_widget, login

#-----------------------------------------------------------------------------------------------------------------------
def login_setConnectButton(self):
    #
    # Login Widget
    #

    self.login_login_button.clicked.connect(lambda: login(self))
    self.login_register_button.clicked.connect(lambda: show_hide_login_register_widget(self))
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Register Widget
    #