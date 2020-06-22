#测试环境将图形验证码和手机验证码验证去掉
from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get("http://www.hugeleafdata.com/")
driver.implicitly_wait(3)
reg_buttonname_class_name='reg'
#/html/body/div/div[2]/div/div/div/div/div[1]/div[1]/input