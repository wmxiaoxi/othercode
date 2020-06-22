import unittest
from Test_data.ZkRecommend_data import *
from framework.ZkRecommend_action import *
from framework.login_action import  *
from common_fuc.basic_method import *
class Test_zktj(unittest.TestCase):
    newmethod=method()
    def test_yxzk(self):
        test_login(usevalue[0], passvalue[0], message[0], mesele[0], mesele[1])
        js = "document.getElementsByClassName('item-top')[4].click()"
        newmethod.excute(js)#执行JS
        time.sleep(3)
        newmethod.scrolldown()
        i=newmethod.check_eles("tag name","li")
        if i <=1:
            count=pageclick(loc[0],loc[1])

        else:
            rows1=pageclick(loc[0], loc[1])
            newmethod.click(loc[0],"/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[2]/ul/li['+str(i)+']")
            rows2 = pageclick(loc[0], loc[1])
            count=rows1*(i-1)+rows2




