from selenium import webdriver
import time
import unittest
from tools import web_tools
class Test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("file:///C:/Users/User/Desktop/html/frame/frameset.html")
        cls.tools=web_tools.Test(cls.driver)
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
    def test_a(self):
        self.tools.test_enter_frame('''//*[@id="leftframe"]''')
        self.tools.test_sendkeys('''//*[@id="left"]''','left')
        self.tools.test_quit_frame()
        self.tools.test_enter_frame('''//*[@id="middleframe"]''')
        self.tools.test_sendkeys('''//*[@id="middle"]''','middle')
        time.sleep(2)
