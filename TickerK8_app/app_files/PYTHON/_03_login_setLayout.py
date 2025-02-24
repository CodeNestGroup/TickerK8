def login_setLayout(self):
    #
    # Main Widget
    #

    # Add Widget
    self.main_layout.addWidget(self.login_widget, 5, 20, 90, 60)
    self.main_layout.addWidget(self.register_widget, 5, 20, 90, 60)

    # Setup Layout
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.main_layout.setRowStretch(i, 1)
        self.main_layout.setColumnStretch(i, 1)

    # Set Layout
    self.setLayout(self.main_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Login Widget
    #

    # Add Widget
    self.login_widget_layout.addWidget(self.login_title_label, 10, 10, 10, 80)
    self.login_widget_layout.addWidget(self.login_login_lineedit, 50, 10, 5, 80)
    self.login_widget_layout.addWidget(self.login_password_lineedit, 60, 10, 5, 80)
    self.login_widget_layout.addWidget(self.login_login_button, 80, 40, 5, 20)
    self.login_widget_layout.addWidget(self.login_register_button, 90, 45, 5, 10)

    # Setup Layout
    self.login_widget_layout.setSpacing(0)
    self.login_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.login_widget_layout.setRowStretch(i, 1)
        self.login_widget_layout.setColumnStretch(i, 1)

    # Set Layout
    self.login_widget.setLayout(self.login_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Register Widget
    #

    # Add Widget
    self.register_widget_layout.addWidget(self.register_title_label, 10, 10, 10, 80)
    self.register_widget_layout.addWidget(self.register_name_subtitle_label, 15, 10, 5, 5)
    self.register_widget_layout.addWidget(self.register_name_lineedit, 20, 12, 5, 76)
    self.register_widget_layout.addWidget(self.register_emial_subtitle_label, 25, 10, 5, 5)
    self.register_widget_layout.addWidget(self.register_emial_lineedit, 30, 12, 5, 76)
    self.register_widget_layout.addWidget(self.register_emial_confirm_lineedit, 35, 12, 5, 76)
    self.register_widget_layout.addWidget(self.register_phonenumber_subtitle_label, 40, 10, 5, 5)
    self.register_widget_layout.addWidget(self.register_phonenumber_combobox, 45, 12, 5, 2)
    self.register_widget_layout.addWidget(self.register_phonenumber_lineedit, 50, 14, 5, 74)
    self.register_widget_layout.addWidget(self.register_country_subtitle_label, 55, 10, 5, 5)
    self.register_widget_layout.addWidget(self.register_country_combobox, 60, 12, 5, 76)
    self.register_widget_layout.addWidget(self.register_password_subtitle_label, 65, 10, 5, 5)
    self.register_widget_layout.addWidget(self.register_password_lineedit, 70, 12, 5, 76)
    self.register_widget_layout.addWidget(self.register_password_confirm_lineedit, 75, 12, 5, 76)
    self.register_widget_layout.addWidget(self.register_register_button, 90, 45, 5, 10)

    # Setup Layout
    self.register_widget_layout.setSpacing(0)
    self.register_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.register_widget_layout.setRowStretch(i, 1)
        self.register_widget_layout.setColumnStretch(i, 1)

    # Set Layout
    self.register_widget.setLayout(self.register_widget_layout)

