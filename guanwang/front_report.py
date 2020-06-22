from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

url="http://192.168.17.214/#/"
title1="瀚叶数据"
title_son=['行业研究', '专题研究']
#行业研究xpath共性
yjgx_xpath="//*[@id=\"websiteHeader\"]/ul/li[2]/a"
#行业研究xpath
hyyj_xpath="//*[@id=\"websiteHeader\"]/ul/li[2]/a[1]"
#行业研究子页面标题xpath
hyyj_son_xpath="//*[@id=\"tab-industry\"]"
#行业研究子页面数据量
hyyj_count_xpath="//*[@id=\"pane-industry\"]/div/span[1]"
#研究报告xpath
ele1_xpath="//*[@id=\"websiteHeader\"]/ul/li[2]/span"


driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.maximize_window()
time.sleep(3)
title=driver.title



if title==title1:
    print("成功打开瀚叶数据官网")
    ele1=driver.find_element_by_xpath(ele1_xpath)
    ActionChains(driver).move_to_element(ele1).perform()
    ele11= ele1.find_elements_by_xpath(yjgx_xpath)
    list=[]
    for i in ele11:
        list.append(i.get_attribute("innerText"))
    print(list)
    #print(len(list))
    if list == title_son:
        print("研究报告下方tab显示正确行业研究, 专题研究")
        ele1.find_element_by_xpath(hyyj_xpath).click()
        time.sleep(5)
        title13=driver.find_element_by_xpath(hyyj_son_xpath)
        #print(title13.get_attribute("outerText"))
        if title13.get_attribute("outerText") =="行业研究":
            name=driver.find_element_by_xpath("//*[@id=\"pane-industry\"]/ul/li[1]/div[2]/h2").get_attribute("outerText")
            print(name)
            js="var q=document.documentElement.scrollTop=100000"
            driver.execute_script(js)
            count=driver.find_element_by_xpath(hyyj_count_xpath).get_attribute("outerText")
            new_str=count.split('共 ')[1] #第一次切割后取空格后数据
            #print(new_str)
            new_str1=int(new_str.split(' 条')[0]) #第一次切割后取空格前数据
            print(new_str1)
            if new_str1 > 9:
                driver.find_element_by_xpath("//*[@id=\"pane-industry\"]/div/ul/li[2]").click()
                time.sleep(3)
                name1=driver.find_element_by_xpath("//*[@id=\"pane-industry\"]/ul/li[1]/div[2]/h2").get_attribute("outerText")
                print(name1)
                if name== name1:
                    print("行业研究报告点击分页失败！")
                else:
                    print("行业研究报告点击分页成功！")



            driver.back()
        else:
            print("未跳转到行业研究报告展示数据")
        time.sleep(3)
        ele1 = driver.find_element_by_xpath(ele1_xpath)
        ActionChains(driver).move_to_element(ele1).perform()
        ele1.find_element_by_xpath("//*[@id=\"websiteHeader\"]/ul/li[2]/a[2]").click()
        time.sleep(5)
        title14=driver.find_element_by_xpath("//*[@id=\"tab-subject\"]")
        if title14.get_attribute("outerText") == "专题研究":
            js = "var q=document.documentElement.scrollTop=100000"
            driver.execute_script(js)
            count = driver.find_element_by_xpath("//*[@id=\"pane-subject\"]/div/span[1]").get_attribute("outerText")
            newstr = count.split('共 ')[1]  # 第一次切割后取空格后数据
            #print(newstr)
            newstr1 = int(newstr.split(' 条')[0])  # 第一次切割后取空格前数据
            print(newstr1)
            driver.back()

else:
    print("...")
driver.quit()


