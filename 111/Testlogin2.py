from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import  time
class testLogin1(unittest.TestCase):
    driver = webdriver.Chrome()

    def login(self,username,password):

        self.driver.get("http://www.hugeleafdata.com/")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.username_xpath = '/html/body/div/div[2]/div/div/div/div/div/div[1]/input'
        self.password_xpath='/html/body/div/div[2]/div/div/div/div/div/div[2]/input'
        self.login_buttonname_xpath='/html/body/div/div[2]/div/div/div/div/div/button'
        self.login_class_name ='login'
        self.driver.find_element_by_class_name(self.login_class_name).click()
        self.driver.find_element_by_xpath(self.username_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(self.password)
        self.driver.find_element_by_xpath(self.login_buttonname_xpath).click()

    #密码不正确
    def test_loginFail(self):
        self.username = '18516285867'
        self.password = '111111'
        self.login(self.username, self.password)
        self.userdata = self.driver.find_element_by_xpath("/html/body/div[2]").text
        self.assertEqual(self.userdata, '账号或密码不正确')


    #用户名不不正确
    def test_loginFail1(self):
        self.username = '18516285866'
        self.password = '123456'
        self.login(self.username, self.password)
        self.userdata = self.driver.find_element_by_xpath("/html/body/div[2]").text
        self.assertEqual(self.userdata, '账号或密码不正确')

    # 用户名为空

    def test_loginFail2(self):
        self.username = ''
        self.password = '123456'
        self.login(self.username, self.password)
        self.userdata = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div/div[2]/span").text
        self.assertEqual(self.userdata,'用户名不能为空')

     #密码为空
    def test_loginFail3(self):
        self.username = '18516285867'
        self.password = ''
        self.login(self.username, self.password)
        self.userdata = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div/div[3]/span").text
        self.assertEqual(self.userdata,'密码不能为空')

    #正常成功登录
    def test_loginsSuccess(self):
        self.username = '18516285867'
        self.password = '123456'
        self.login(self.username,self.password)
        self.userdata = self.driver.find_element_by_class_name("el-dropdown").text
        self.assertEqual(self.userdata,self.username)

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(testLogin1("test_loginsSuccess"))
    suite.addTest(testLogin1("test_loginFail"))
    runner = unittest.TextTestRunner()
    runner.run(suite)





