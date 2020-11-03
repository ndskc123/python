from appium import webdriver
import time
import unittest
from tools import app_tools
class Test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        phone={
            'deviceName':'Redmi_5_Plus',
            'platformName':'Android',
            'platformVersion':'8.1',
            'appPackage':'com.baidu.searchbox',
            'appActivity':'com.baidu.searchbox.SplashActivity',
            'noReset':'True',
            'automation':'appium'
        }
        cls.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',phone)
        cls.driver.implicitly_wait(10)
        cls.tools=app_tools.Tools(cls.driver)
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
    def test_a(self):
        self.tools.swipeUp(n=2)
        time.sleep(2)
