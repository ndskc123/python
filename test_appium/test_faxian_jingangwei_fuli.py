from phone import xiaomi
import time
import unittest
from appium import webdriver
from tools import app_tools
class Test_faxian_fuli(unittest.TestCase):
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
    def test_fuli(self):
        '''发现-金刚位-福利'''
        fuli_text=self.tools.test_text('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView
''')
        self.assertEqual(fuli_text,'福利')
        print('第一次校验金刚位福利通过')
        self.tools.test_click('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView
''')
        self.tools.test_back()
        fuli_text = self.tools.test_text('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView
        ''')
        self.assertEqual(fuli_text, '福利')
        print('第二次校验金刚位福利通过')

