import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
#import Testlogin1
class testcinema(unittest.TestCase):
    driver = webdriver.Chrome()
    def test_ccheck(self):
        self.driver.get("http://www.hugeleafdata.com/")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.username_xpath = '/html/body/div/div[2]/div/div/div/div/div/div[1]/input'
        self.password_xpath = '/html/body/div/div[2]/div/div/div/div/div/div[2]/input'
        self.login_buttonname_xpath = '/html/body/div/div[2]/div/div/div/div/div/button'
        #self.ge_filed = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[3]/div[1]')
        self.login_class_name = 'login'
        self.username='18516285867'
        self.password='123456'
        self.driver.find_element_by_class_name(self.login_class_name).click()
        self.driver.find_element_by_xpath(self.username_xpath).clear()
        self.driver.find_element_by_xpath(self.password_xpath).clear()
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(self.password)
        self.driver.find_element_by_xpath(self.login_buttonname_xpath).click()
        #ActionChains(self.driver).move_to_element(self.ge_filed).perform()
        self.driver.find_element_by_link_text("院线分析").click()

    #a=Testlogin1.testLogin1
    #b=a.login(a.username,a.password)
    #def test_cinema(self):

    #self.a.test_loginsSuccess(self)

    if __name__ == '__main__':
        unittest.main()







