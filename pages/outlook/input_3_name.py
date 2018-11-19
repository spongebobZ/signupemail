from framework.tools import Tools
from selenium.webdriver.common.by import By

class InputName(Tools):
    INPUT_LASTNAME = (By.ID,'LastName')
    INPUT_FIRSTNAME = (By.ID,'FirstName')
    NEXT_BTN = (By.ID, 'iSignupAction')

    def __init__(self,driver):
        Tools.__init__(self,driver)
        self.wait_page_ready(self.INPUT_LASTNAME)

    def type_name(self):
        import random, string
        lastname = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        firstname = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        self.type(self.INPUT_LASTNAME,lastname)
        self.type(self.INPUT_FIRSTNAME,firstname)
        self.click(self.NEXT_BTN)

