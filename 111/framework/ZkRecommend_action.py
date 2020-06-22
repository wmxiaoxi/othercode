from Test_data.login_data import *
from Test_data.ZkRecommend_data import *
from framework.login_action import *
from common_fuc.basic_method import *

newmethod=method()

#只有一页的分页
def pageclick(*loc1):
     mentable=newmethod.find_element(*loc1)
     rows=len(mentable.find_elements("tag name","tr"))
     return rows








