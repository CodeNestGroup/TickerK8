#
# Import
#
import os
from json import load
def set_Css(self, code):
    # Open Json Config File

    with open(f'{self.file_app_path}/APP_FILES/CONFIG/main_config.json', 'r') as json_file_read:
        # Load file
        config = dict(load(json_file_read))
    # Set Style
    self.setStyleSheet(open(self.file_app_path+config[code]).read())
