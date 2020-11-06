from selenium import webdriver
import unittest
import time
from tools import web_tools
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
class Test_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://www.baidu.com/")
        cls.tools=web_tools.Test(cls.driver)
    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
    def test_case_01(self):
        self.tools.test_sendkeys('''//*[@id="kw"]''','selenium')
        self.tools.test_click('''//*[@id="su"]''')
        # self.driver.set_window_size(600,600)
        # js="window.scrollTo(0,500);"
        # self.driver.execute_script(js)
        # self.driver.maximize_window()
        self.tools.test_trackball()

if __name__ == '__main__':
    unittest.main()





