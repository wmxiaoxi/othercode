from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
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


#隐藏的元素使用js来操作的
js = "document.getElementsByClassName('item-top')[4].click()"
driver.execute_script(js) #执行JS



#从数据日报里面进去的
# driver.find_element_by_xpath('/html/body/div/div[2]/header/div[2]/span[1]').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/img').click()
time.sleep(2)
pharecount=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/ul/li[1]/div/p[2]/span").get_attribute("innerText")
print(pharecount)



#将滚动条移动到页面的底部
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(2)
#定位到table
menu_table = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div[3]")
#获取到table中tr
rows = menu_table.find_elements_by_tag_name('tr')
#取得table中tr的长度
before_add_numbers = len(rows)
print(before_add_numbers)

#获取列表中影片的名字
cnames =driver.find_elements_by_xpath ("/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr/td[1]/div/a")
cnames1 =driver.find_element_by_xpath ("/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/a").get_attribute("text")
lists=[]
for i in cnames:
    a=i.get_attribute("text")
    lists.append(a)
print(a,lists,len(lists))


#获取影片中第一页的票房
cnumbers=driver.find_elements_by_xpath("/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div/span")
numlist=[]
for n in cnumbers:
    nub=n.get_attribute("innerText")
    numlist.append(nub)
print(numlist)



pagecount=driver.find_elements_by_xpath("/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[2]/ul/li")
#print(pagecount)

#获取页面页数
lists1=[]
for j in pagecount:
    count1=j.get_attribute("outerText")
    lists1.append(count1)
#print(len(lists1))
finallycount=len(lists1)
print(finallycount)
print(lists1)
print(type(finallycount))


#分页功能成功跳转
index=2
if finallycount != 1:
    while (index<=finallycount):
        tt=str(index)
        driver.find_element_by_xpath(
                "/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[2]/ul/li["+ tt +"]").click()
        print(index,finallycount)
        time.sleep(2)
        cnames3 = driver.find_elements_by_xpath(
                "/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr/td[1]/div/a")
        cnames2 = driver.find_element_by_xpath(
                "/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/a").get_attribute(
                "text")
        cnumbers = driver.find_elements_by_xpath(
            "/html/body/div/div[3]/div/div[3]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr/td[2]/div/span")
        print(cnames2)
        if cnames2 == cnames1:
            print("分页跳转失效")
        else:
            print("成功跳转第"+str(index)+"页")
            for ii in cnames3:
                cnames4 = ii.get_attribute("text")
                lists.append(cnames4)
            for nn in cnumbers:
                cnumbers1=nn.get_attribute("innerText")
                numlist.append(cnumbers1)
            index=index+1
    #print(lists)
    print("该页面总条数"+str(len(lists)))
    #print(numlist)
    #将列表里的字符串 转化为浮点型数值
    numlist1 = list(map(float, numlist))
    #print(numlist1)

    #将取出的列表里的数据相加
    sumcount = 0
    for t in (range(len(numlist1))):
        sumcount=sumcount+numlist1[t]

    #将相加的结四舍五入并为整形
    #print(int(sumcount+0.5))
    #print(type(pharecount))
    if (int(sumcount+0.5)) == int(pharecount):
        print("列表票房统计总和和图行上总和一致！！")
    else:
        print("列表票房统计总和和图行上总和不一致，测试失败！！")




else:
    print("%只有一页%")

driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/span").click()
driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/div[2]/input").send_keys('中国机长')
driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/div/div[1]/div/button[2]/span").click()
time(10)
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
menu_table1=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div/div/div[2]")
rows1=menu_table1.find_elements_by_tag_name('tr')
print(len(rows1))


































# print (driver.ti
#userdata = driver.find_element_by_class_name("el-dropdown").text
# print(type(userdata))
# print(type(username))
#if userdata == username:
    #print('测试通过')
#else:
   # print('测试不通过')







