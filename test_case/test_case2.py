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
        cls.tools=web_tools.Test(cls.driver)
        cls.driver.get("file:///C:/Users/User/Desktop/html/tagname.html")
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
    def test_a(self):
        time.sleep(2)