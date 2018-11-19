import time,os
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# create a logger instance
logger = Logger(logger='Tools').getlog()

class Tools():
    def __init__(self,driver):
        self.driver = driver

    #click to close browser
    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info('Click forward on current page.')

    def back(self):
        self.driver.back()
        logger.info('Click back on current page.')

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('wait for %d seconds.' % seconds)

    #click to close current page
    def close(self):
        try:
            self.driver.close()
            logger.info('Closing and quit the browser.')
        except NameError as e:
            logger.error('Failed to quit the browser with %s' % e)

    def take_shot(self,message=''):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        shot_name = file_path + rq + message+'.png'
        try:
            self.driver.get_screenshot_as_file(shot_name)
            logger.info('Had take screenshot and save to folder : /screenshots as %s'%shot_name)
        except NameError as e:
            logger.error('Failed to take screenshot! %s' % e)
            self.take_shot()

    def find_element(self,selector):
        #selector must be a tuple like (By.ID,'eat')
        try:
            el = self.driver.find_element(by = selector[0],value = selector[1])
            return el
        except NoSuchElementException as e:
            logger.error('no element due to selector:%s'%','.join(selector))
            raise e

    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.take_shot()

    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.take_shot()

    def click(self, selector):
        el = self.find_element(selector)
        text = el.text
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def click_when_ready(self,selector,timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(selector))
            self.click(selector)
        except TimeoutException as e:
            logger.error('waiting time out:%s' % e)

    def select_by_text(self,seletor,text):
        Select(self.find_element(seletor)).select_by_visible_text(text)


    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    #-------------------wait-------------------------
    def wait_exist(self,selector,waittime = 10):
        try:
            WebDriverWait(self.driver,waittime).until(EC.presence_of_element_located(selector))
        except TimeoutException as e:
            logger.error('waiting time out:%s'%e)

    def wait_not_exist(self,selector,timeout = 10):
        try:
            WebDriverWait(self.driver,timeout).until_not(EC.presence_of_element_located(selector))
        except TimeoutException as e:
            logger.error('waiting time out:%s'%e)

    def wait_page_ready(self,selector,timeout=10):
        self.wait_exist(selector,timeout)



