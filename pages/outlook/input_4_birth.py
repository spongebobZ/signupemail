import os
from framework.tools import Tools
from selenium.webdriver.common.by import By
from configparser import ConfigParser

class InputBirth(Tools):
    SELECT_YEAR = (By.ID,'BirthYear')
    SELECT_MONTH = (By.ID, 'BirthMonth')
    SELECT_DAY = (By.ID, 'BirthDay')
    NEXT_BTN = (By.ID, 'iSignupAction')

    def __init__(self,driver):
        Tools.__init__(self,driver)
        self.wait_page_ready(self.SELECT_YEAR)

    def select_birth(self):
        config = ConfigParser()
        conf_path = os.path.dirname(os.path.abspath('.')) + '/config/conf.ini'
        config.read(conf_path)
        birthyear = config.get('data', 'birthyear')
        # birthmonth = config.get('data', 'birthmonth')
        # birthday = config.get('data', 'birthday')
        self.select_by_text(self.SELECT_YEAR,birthyear)
        self.select_by_text(self.SELECT_MONTH, '1月')
        self.select_by_text(self.SELECT_DAY, '3日')
        self.click(self.NEXT_BTN)
