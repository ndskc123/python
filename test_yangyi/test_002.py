from appium import webdriver
import time
import unittest

class Test_appium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        phone={
            'deviceName':'Redmi_5_Plus',
            'platformName':'Android',
            'platformVersion':'8.1',
            'automation':'appium',
            'appPackage':'com.baidu.searchbox',
            'appActivity':'com.baidu.searchbox.SplashActivity',
            'noReset':'True'

        }
        cls.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',phone)
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
    def test_a(self):
        time.sleep(2)
        

if __name__ == '__main__':
    unittest.main()