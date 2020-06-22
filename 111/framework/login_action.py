from Test_data.login_data import *
from common_fuc.basic_method import *

newmethod=method()

def test_login(usevalue,passvalue,excepted_word,*loc):
    newmethod.open1("http://www.hugeleafdata.com/")
    #newmethod.driver.get("http://www.hugeleafdata.com/")
    newmethod.click(loginlj1[0],loginlj1[1])
    newmethod.sleep(5)
    newmethod.send_keys(usevalue,useloc[0],useloc[1])
    newmethod.send_keys(passvalue,passloc[0],passloc[1])
    newmethod.click(loginbut[0],loginbut[1])
    newmethod.sleep(2)
    name=newmethod.find_element(*loc).text
    newmethod.assert_keyword(excepted_word, name)







