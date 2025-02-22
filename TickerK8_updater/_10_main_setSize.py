from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QSizePolicy

def set_Size(self):
    #
    # Self
    #

    self.setGeometry(QRect(self.screen_size.width()//4,
                           self.screen_size.height()//4,
                           self.screen_size.width()//2,
                           self.screen_size.height()//2
                           )
                     )

#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Widget
    #
    self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_changelog_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_open_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_social_media_instagram_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_social_media_github_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_social_media_discord_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_start_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Changelog Widget
    #

    #self.changlog_widget.setFixedSize(QSize())
    #self.changlog_scroll.setFixedSize(QSize())

# -----------------------------------------------------------------------------------------------------------------------

    #
    # Settings Widget
    #

    #self.settings_widget.setFixedSize(QSize())
    #self.settings_menu_scroll.setFixedSize(QSize())

# -----------------------------------------------------------------------------------------------------------------------

    pass