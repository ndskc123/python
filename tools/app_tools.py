import time
class Tools():
    def __init__(self,driver):
        self.driver=driver

    def test_click(self,elements):
        '''点击'''
        time.sleep(1)
        self.driver.find_element_by_xpath(elements).click()

    def test_back(self):
        '''返回'''
        time.sleep(2)
        self.driver.keyevent(4)

    def test_text(self,elements):
        '''文本'''
        time.sleep(1)
        text_name = self.driver.find_element_by_xpath(elements).text
        print(text_name)
        return text_name

    def swipeUp(self, t=600, n=1):
        '''向上滑动屏幕'''
        time.sleep(2)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.65
        y2 = l['height'] * 0.35
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(2)
    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        time.sleep(2)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.35
        y2 = l['height'] * 0.65
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(2)
    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        time.sleep(2)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.65
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.35
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
        time.sleep(2)
    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        time.sleep(2)
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.35
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.65
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
        time.sleep(2)

