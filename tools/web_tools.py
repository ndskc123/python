from selenium.webdriver import ActionChains
import time
class Test():
    def __init__(self,driver):
        self.driver=driver
    def test_get(self,url):
        '''获取页面'''
        self.driver.get(url)
    def test_click(self,elements):
        '''元素点击'''
        self.driver.find_element_by_xpath(elements).click()
    def test_sendkeys(self,elements,sendkeys):
        '''输入框输入'''
        self.driver.find_element_by_xpath(elements).send_keys(sendkeys)
    def test_clear(self,elements,sendkeys):
        '''清除输入框'''
        self.driver.find_element_by_xpath(elements).clear(sendkeys)
    def test_back(self):
        '''后退'''
        self.driver.back()
    def test_forword(self):
        '''前进'''
        self.driver.forward()
    def test_refresh(self):
        '''页面刷新'''
        self.driver.refresh()
    def test_text(self,elements):
        '''获取页面文本内容'''
        text=self.driver.find_element_by_xpath(elements).text
        print(text)
        return text
    def test_enter_frame(self,elements):
        '''进入frame'''
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(elements))
    def test_quit_frame(self):
        '''退出frame'''
        self.driver.switch_to_default_content()
    def test_current_window(self):
        '''记住当前的窗口'''
        current_window = self.driver.current_window_handle
        return current_window
    def test_switch_to_window(self,current_window):
        '''切换窗口'''
        self.driver.switch_to_window(current_window)
    def test_alert_accept(self):
        '''警告框确定'''
        self.driver.switch_to_alert().accept()
    def test_alert_dismiss(self):
        '''警告框取消'''
        self.driver.switch_to_alert().dismiss()
    def test_alart_sendkeys(self,sendkeys):
        '''警告框输入'''
        self.driver.switch_to_alert().send_keys(sendkeys)
    def test_alert_text(self):
        '''警告框文本'''
        alert_text = self.driver.switch_to_alert().text
        print(alert_text)
        return alert_text
    def test_trackball(self,js='window.scrollBy(0,300)'):
        '''
        页面滑动，调用示例：
        driver.test_trackball('window.scrollBy(0,300)')
        '''
        time.sleep(2)
        self.driver.set_window_size(600, 600)
        self.driver.execute_script(js)
        self.driver.maximize_window()
    def test_move_mouse(self, elements):
        '''鼠标悬停'''
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(elements)).perform()
    def test_move_distance(self,elements,x=500,y=0):
        '''鼠标滑动距离'''
        time.sleep(2)
        action = ActionChains(self.driver)
        slider = self.driver.find_element_by_xpath(elements)
        action.click_and_hold(slider).perform()
        '''按下不松'''
        action.drag_and_drop_by_offset(slider, x, y).perform()
        '''移动多少的距离'''
    def test_move_element(self,element1,element2):
        '''鼠标从一个元素移动到另一个元素'''
        time.sleep(2)
        action = ActionChains(self.driver)
        x = self.driver.find_element_by_xpath(element1)
        y = self.driver.find_element_by_xpath(element2)
        action.click_and_hold(x).perform()
        '''按下不松'''
        action.drag_and_drop(x, y).perform()
    def test_printscreen(self,printscreen='./picture.png'):
        '''
        窗口截图，printscreen传文件保存路径(如：./picture.png)
        ("D:\python student\lianxi\work\p2.png")
        '''
        self.driver.save_screenshot(printscreen)



