from phone import xiaomi
import time
import unittest
from appium import webdriver
from tools import app_tools
class Test_faxian(unittest.TestCase):
    '''好游驿站模块'''
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
    def test_a(self):
        '''向上滑动'''
        self.tools.swipeUp()
    def test_haoyouyizhan(self):
        '''好游驿站模块'''
        haoyouyizhan_text=self.tools.test_text('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView
''')
        self.assertEqual(haoyouyizhan_text,'好游驿站')
        print('好游驿站第一次校验通过')
        self.tools.test_click('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.ImageButton
''')
        self.tools.test_back()
        haoyouyizhan_text = self.tools.test_text('''/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView
        ''')
        self.assertEqual(haoyouyizhan_text, '好游驿站')
        print('好游驿站第二次校验通过')
if __name__ == '__main__':
    unittest.main()