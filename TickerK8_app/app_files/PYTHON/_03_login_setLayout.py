def login_setLayout(self):
    #
    # Main Widget
    #

    # Add Widget
    self.main_layout.addWidget(self.login_widget, 60, 20, 60, 60)
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
