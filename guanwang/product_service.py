from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
url="http://192.168.17.214/#/"
ele_xpath="//*[@id=\"websiteHeader\"]/ul/li[3]/span"
title1="瀚叶数据"
public="//*[@id=\"websiteHeader\"]/ul/li[3]/a"


driver = webdriver.Chrome()

def openurl(url):
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()
    return
def guanwang(ele_xpath,public):
    title = driver.title
    if title == title1:
        print("成功打开瀚叶数据官网")
        product_ele=driver.find_element_by_xpath(ele_xpath)
        ActionChains(driver).move_to_element(product_ele).perform()
        public_eles=product_ele.find_elements_by_xpath(public)
        list=[]
        for titlecount in public_eles:
            aa=titlecount.get_attribute("outerText")
            list.append(aa)
        if list==['IP价值评估','企业信用评估','解决方案']:
            result="产品服务tab下显示"+list[0]+","+list[1]+"，"+list[2]
            print(result)
            aa=int(len(list))
        return aa
#循环点击产品服务下的3个tab
def pservice_click(ele_xpath):
    product=guanwang(ele_xpath,public)
    i=1
    print(product)
    while  i <= product:
         product_ele = driver.find_element_by_xpath(ele_xpath)
         ActionChains(driver).move_to_element(product_ele).perform()
         p_ele=driver.find_element_by_xpath("//*[@id=\"websiteHeader\"]/ul/li[3]/a["+str(i)+"]")
         p_name=p_ele.get("outerText")
         p_ele.click()
         time.sleep(5)
         driver.back()
         i=i+1
    else:
        print("执行完毕点击tab跳转")
        driver.quit()







openurl(url)
pservice_click(ele_xpath)











