import os
import unittest

from pages.input_2_pw import InputPw
from pages.input_3_name import InputName
from pages.input_4_birth import InputBirth
from pages.input_5_code import InputCode

from framework.browser_engine import BrowserEngine
from pages.outlook.input_1_mail import InputMail


class TestSignUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_signup(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        p1 = InputMail(self.driver)
        p1.type_email()
        p2 = InputPw(self.driver)
        p2.type_pw()
        p3 = InputName(self.driver)
        p3.type_name()
        p4 = InputBirth(self.driver)
        p4.select_birth()
        p5 = InputCode(self.driver)
        p5.wait_type_finished()
        with open(os.path.dirname(os.path.abspath('.')) + '/emails/email.txt','a',encoding='utf-8') as fw:
            fw.write(p1.get_email())
