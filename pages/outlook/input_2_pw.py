import os
from framework.tools import Tools
from selenium.webdriver.common.by import By
from configparser import ConfigParser

class InputPw(Tools):
    INPUT_PW = (By.ID,'PasswordInput')
    NEXT_BTN = (By.ID, 'iSignupAction')

    def __init__(self,driver):
        Tools.__init__(self,driver)
        self.wait_page_ready(self.INPUT_PW)

    def type_pw(self):
        config = ConfigParser()
        conf_path = os.path.dirname(os.path.abspath('.')) + '/config/conf.ini'
        config.read(conf_path)
        pw = config.get('data','password')
        self.type(self.INPUT_PW,pw)
        self.click(self.NEXT_BTN)

