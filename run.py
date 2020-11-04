import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner
def send_mail(report):
    yag = yagmail.SMTP(user='v_yangyi12@126.com', password='FADXJPZIFIDJBQJC', host='smtp.126.com')
    '''发送的邮箱，密码，服务器地址'''
    yag.send(['v_yangyi12@126.com', 'v_yangyi13@126.com'], '测试报告', '这是测试报告（本次测试报告不支持回复）', report)
    '''被发送的邮箱，主题，正文，附件'''
if __name__ == '__main__':
    suit=unittest.defaultTestLoader.discover('test_yangyi','test*.py')
    '''被执行测试的文件'''
    fp=open(r'../result/test.html','wb')
    '''报告被保存在哪里'''
    runner=HTMLTestRunner(stream=fp,title='测试报告',description='chrome浏览器，win10系统')
    '''报告的内容'''
    runner.run(suit)
    '''运行报告'''
    fp.close()
    '''关闭被保存文件'''
    send_mail(r'../result/test.html')
    '''发送邮件'''