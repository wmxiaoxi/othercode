# coding=utf-8
from TestUnittest.login_test import  TestLogin
from TestUnittest.ZkRecommend_test import *
from HTMLTestRunner import HTMLTestRunner
from datetime  import date
import unittest
from BeautifulReport import BeautifulReport
# now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
#这个方法适用于执行少量测试用例，需要手动一个一个addTest去加载，
# 如果一个类下面有很多测试用例会比较麻烦，这时候我们需要makeSuite()方法，下一篇我们接着讲
# suite.addTest(unittest.makeSuite(TestLogin))  # 一次记载多个用例
if __name__=='__main__':
    filepath = '../result/htmlreport'+str(date.today())+'.html'
    ftp = open(filepath, 'w+')
    suite = unittest.TestSuite()
    suite.addTest(Test_zktj('test_yxzk'))

    #runner=HTMLTestRunner(stream=ftp,title='login report',description='report')
    runner = unittest.TextTestRunner()
    runner.run(suite)