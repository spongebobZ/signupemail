from framework.tools import Tools
from selenium.webdriver.common.by import By

class InputMail(Tools):
    INPUT_MAIL = (By.ID,'MemberName')
    NEXT_BTN = (By.ID,'iSignupAction')
    email=''

    def __init__(self,driver):
        Tools.__init__(self,driver)
        self.wait_page_ready(self.INPUT_MAIL)

    def type_email(self):
        import random,string
        self.email = ''.join(random.sample(string.ascii_letters + string.digits, 8)) + '@outlook.com'
        self.type(self.INPUT_MAIL,self.email)
        self.click(self.NEXT_BTN)

    def get_email(self):
        return self.email