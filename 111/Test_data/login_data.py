# 选找登录的链接定位
loginlj1 = ("class name", "login")
# 用户名输入框定位
useloc = ('xpath', '/html/body/div/div[2]/div/div/div/div/div/div[1]/input')
# 密码输入框定位
passloc = ('xpath', '/html/body/div/div[2]/div/div/div/div/div/div[2]/input')
# 登录按钮的定位
loginbut = ('xpath', '/html/body/div/div[2]/div/div/div/div/div/button')
#基础数据
#url = 'http://www.hugeleafdata.com/'
passvalue =('123456',"123457")
usevalue = ('18516285867',"18516285866")


#断言定位

#成功登录
mesele=("class name","el-dropdown")
#用户名密码不正确
mesele1=("xpath","/html/body/div[2]")
#用户名为空
mesele2=("xpath","/html/body/div/div[2]/div/div/div/div/div/div[2]/span")
#密码为空
mesele3=("xpath","/html/body/div/div[2]/div/div/div/div/div/div[3]/span")

message=('18516285867','账号或密码不正确','用户名不能为空','密码不能为空')
