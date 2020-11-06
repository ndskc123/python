from phone import xiaomi
import time
import unittest
from appium import webdriver
from tools import app_tools
class Test_faxian(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',xiaomi.phone)
        cls.driver.implicitly_wait(10)
        cls.tools=app_tools.Tools(cls.driver)
        time.sleep(6)
        cls.tools.test_click('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.TabWidget/android.widget.FrameLayout[4]/android.widget.FrameLayout/android.widget.ImageView
''')
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
    def test_faxian(self):
        '''发现'''
        faxian_text=self.tools.test_text('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[1]
''')
        self.assertEqual(faxian_text,'发现')
        print('发现校验通过')
