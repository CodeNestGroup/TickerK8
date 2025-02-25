def set_Layout(self):
    #
    # Self
    #

    self.layout.addWidget(self.app_widget)
    self.layout.addWidget(self.changlog_widget)
    self.layout.addWidget(self.settings_widget)

    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0, 0, 0, 0)

    self.setLayout(self.layout)

    #
    # Main Widget
    #

    # Main
    self.main_widget_layout.addWidget(self.main_changelog_scroll, 0, 0, 90, 50)
    self.main_widget_layout.addWidget(self.main_settings_widget, 0, 50, 90, 50)
    self.main_widget_layout.addWidget(self.main_update_widget, 90, 0, 10, 80)
    self.main_widget_layout.addWidget(self.main_start_button, 90, 75, 10, 25)

    self.main_widget_layout.setSpacing(0)
    self.main_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.main_widget_layout.setRowStretch(i, 1)
        self.main_widget_layout.setColumnStretch(i, 1)

    self.app_widget.setLayout(self.main_widget_layout)

    # Main Settings
    self.main_settings_widget_layout.addWidget(self.main_settings_open_button, 0, 0, 50, 50)
    self.main_settings_widget_layout.addWidget(self.main_settings_social_media_instagram_button, 0, 50, 50, 50)
    self.main_settings_widget_layout.addWidget(self.main_settings_social_media_github_button, 50, 0, 50, 50)
    self.main_settings_widget_layout.addWidget(self.main_settings_social_media_discord_button, 50, 50, 50, 50)

    self.main_settings_widget_layout.setSpacing(0)
    self.main_settings_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.main_settings_widget_layout.setRowStretch(i, 1)
        self.main_settings_widget_layout.setColumnStretch(i, 1)

    self.main_settings_widget.setLayout(self.main_settings_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Changelog Widget
    #

    self.changlog_widget_layout.addWidget(self.changlog_scroll, 10, 20, 80, 60)

    self.changlog_widget_layout.setSpacing(0)
    self.changlog_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.changlog_widget_layout.setRowStretch(i, 1)
        self.changlog_widget_layout.setColumnStretch(i, 1)

    self.changlog_widget.setLayout(self.changlog_widget_layout)

#-----------------------------------------------------------------------------------------------------------------------

    #
    # Settings Widget
    #

    self.settings_widget_layout.addWidget(self.settings_menu_scroll)

    self.settings_widget_layout.setSpacing(0)
    self.settings_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.settings_widget_layout.setRowStretch(i, 1)
        self.settings_widget_layout.setColumnStretch(i, 1)

    self.settings_widget.setLayout(self.settings_widget_layout)


    # Menu #
    self.settings_menu_scroll_widget_layout.setSpacing(0)
    self.settings_menu_scroll_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.settings_menu_scroll_widget_layout.setRowStretch(i, 1)
        self.settings_menu_scroll_widget_layout.setColumnStretch(i, 1)

    self.settings_menu_scroll_widget.setLayout(self.settings_menu_scroll_widget_layout)
