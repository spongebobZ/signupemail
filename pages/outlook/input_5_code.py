from framework.tools import Tools
from selenium.webdriver.common.by import By

class InputCode(Tools):
    CODE_TIPS = (By.CLASS_NAME,'text-base')
    NEXT_BTN = (By.ID, 'iSignupAction')

    def __init__(self,driver):
        Tools.__init__(self,driver)
        self.wait_page_ready(self.CODE_TIPS)

    def wait_type_finished(self,timeout=200):
        self.wait_not_exist(self.CODE_TIPS,timeout)