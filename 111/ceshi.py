from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import  time
#coding=utf-8s
driver = webdriver.Chrome()
#打开浏览器
driver.get("http://www.hugeleafdata.com/")
driver.implicitly_wait(3)
#放大浏览器
driver.maximize_window()
login_buttonname_class_name = 'login'
driver.find_element_by_class_name(login_buttonname_class_name).click()
username='18516285867'
password = '123456'
username_xpath = '/html/body/div/div[2]/div/div/div/div/div/div[1]/input'
password_xpath='/html/body/div/div[2]/div/div/div/div/div/div[2]/input'
login_buttonname_xpath='/html/body/div/div[2]/div/div/div/div/div/button'
# 清空输入框
driver.find_element_by_xpath(username_xpath).clear()
driver.find_element_by_xpath(password_xpath).clear()
# 输入值
driver.find_element_by_xpath(username_xpath).send_keys(username)
driver.find_element_by_xpath(password_xpath).send_keys(password)
driver.find_element_by_xpath(login_buttonname_xpath).click()
time.sleep(2)
#获取cookie
cookie=driver.get_cookies()
print(cookie)

driver.find_element_by_xpath('/html/body/div/div[2]/header/div[2]/span[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/img').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/span').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/div[1]/input').clear()
driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/div[1]/input').send_keys('2019-11-10')
#/html/body/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div[1]/input


# js="var q=document.documentElement.scrollTop=100000"
# driver.execute_script(js)

#将滚动条移动到固定的位置
loactor=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[5]/td[2]/div/a")
ActionChains(driver).move_to_element(loactor).perform()
a=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/div/input")
a.click()

#滚动条用js滚动到固定位置
target=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[17]/span")
driver.execute_script("arguments[0].scrollIntoView();",target)
target.click()





# itme1=a.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]")
# item2=a.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[17]/span')
# ActionChains(driver).drag_and_drop(itme1,item2).perform()
# ActionChains(driver).click_and_hold(item2).perform()






# from selenium import webdriver
# b=webdriver.chrome()
# b.get("")
# ele=b.find_element_by_link_text()
# ele.click()
# b.back()
# b.find_element_by_css_selector("input[type=\"text\"]")


