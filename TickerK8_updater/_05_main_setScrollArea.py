def set_ScrollArea(self):
    #
    # Main Widget
    #

    self.main_changelog_scroll.setWidgetResizable(True)

# -----------------------------------------------------------------------------------------------------------------------

    #
    # Changelog Widget
    #

    self.changlog_scroll.setWidgetResizable(True)

# -----------------------------------------------------------------------------------------------------------------------

    #
    # Settings Widget
    #

    self.settings_menu_scroll.setWidgetResizable(True)
    self.settings_menu_scroll.setWidget(self.settings_menu_scroll_widget)