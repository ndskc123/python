import unittest
from selenium import webdriver
import time

class Test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("file:///C:/Users/User/Desktop/html/Alert.html")
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
    def test_a(self):
        time.sleep(2)