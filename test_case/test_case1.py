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
        cls.driver.get("file:///C:/Users/User/Desktop/html/Alert.html")
        cls.tools=web_tools.Test(cls.driver)
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
    def test_aaa(self):
        self.tools.test_click('''//*[@id="btnConfirm"]''')
        alert_text1=self.tools.test_alert_text()
        self.assertEqual('Chose an option.',alert_text1)
        self.tools.test_alert_accept()
        test_text1=self.tools.test_text('''//*[@id="output"]''')
        self.assertEqual('Confirmed.',test_text1)

        self.tools.test_click('''//*[@id="btnConfirm"]''')
        alert_text2=self.tools.test_alert_text()
        self.assertEqual('Chose an option.',alert_text2)
        self.tools.test_alert_dismiss()
        test_text2=self.tools.test_text('''//*[@id="output"]''')
        self.assertEqual('Rejected!',test_text2)
        time.sleep(2)
    def test_aab(self):
        self.tools.test_click('''//*[@id="btnAlert"]''')
        self.tools.test_alert_text()
        self.tools.test_alert_accept()
        test_text3=self.tools.test_text('''//*[@id="output"]''')
        self.assertEqual("Alert is gone.",test_text3)
        time.sleep(2)

    def test_aac(self):
        self.tools.test_click('''//*[@id="btnPrompt"]''')
        self.tools.test_alert_text()
        self.tools.test_alart_sendkeys('yangyi')
        self.tools.test_alert_accept()
        test_text4=self.tools.test_text('''//*[@id="output"]''')
        self.assertEqual('yangyi',test_text4)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
