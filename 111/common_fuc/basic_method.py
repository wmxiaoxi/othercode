import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


#封装
class method():
    #创建一个日志

    driver=webdriver.Chrome()


    #打开浏览器
    def open1(self,url):
        #self.driver=driver
        self.driver.get(url)
        self.driver.maximize_window()

   #关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    #浏览器前进操作
    def forward(self):
        self.driver.forward()

   #浏览器返回操作
    def back(self):
        self.driver.back()


   #定位元素
    def find_element(self,*loc):
        try:
            #WebDriverWait(self.driver,5).until(self.driver.find_element(*loc))
            WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

            # 定位元素

    def find_elements(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except Exception as e:
            raise e


    def send_keys(self,value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e



    def click(self,*loc):
        try:
            self.find_element(*loc).click()
        except AttributeError as e:
            raise e

    #模拟移动到固定位置

    def move_to_element(self,*loc):
        try:
            ele=self.find_element(*loc)
            ActionChains.move_to_element(ele).perform()
        except AttributeError as e:
            raise e

    #强制等待
    def sleep(self,second):
        return time.sleep(second)

    # 断言
    def assert_keyword(self, excepted_word, name):

        try:
            assert True == (excepted_word in  name)

        except AssertionError as e:
            raise e
        except Exception as  e:
            raise e


    # 保存截图
    def get_windoes_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/img/'#设置截图保存路径
        rq=time.strftime('%Y%m%d%H%M', time.localtime(time.time()))#获取当前系统时间
        img_name = file_path + rq + '.png'  # 设置截图名称格式
        try:
            self.driver.get_screenshot_as_file(img_name)#指定截图存放路径和名称
            print("已将截图保存到文件夹/img/img")
        except NameError as e:
            print("截图保存失败! %s" % e)
            self.get_windows_img()


    #执行js
    def excute(self,js):
        self.driver.execute_script(js)

    #滚动条移至到底部
    def scrolldown(self):
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

    #滚动条移至到顶部
    def scrolltop(self):
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)


    #滚动条移动到固定的位置
    def  move(self,*loc):
        target = self.find_element(*loc)
        self.execute_script("arguments[0].scrollIntoView();", target)
        target.click()

    #查找返回行数条数
    def check_eles(self,*loc1):
        rows = self.find_elements(*loc1)
        return len(rows)

    #查找返回行数条数
    def check_ele(self,*loc1):
        rows = self.find_element(*loc1)
        return len(rows)


 # 获取输入框的值
    def Get_attribute(self, type, value1, value2):
        if type == "xpath":
            Value = self.driver.find_element_by_xpath(value1).get_attribute(value2)
            return Value
        elif type == "name":
            Value = self.driver.find_element_by_name(value1).get_attribute(value2)
            return Value
        elif type == "link_text":
            Value = self.driver.find_element_by_link_text(value1).get_attribute(value2)
            return Value
        elif type == "class_name":
            Value = self.driver.find_element_by_class_name(value1).get_attribute(value2)
            return Value
        elif type == "id":
            Value = self.driver.find_element_by_id(value1).get_attribute(value2)
            return Value



















