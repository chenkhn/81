# 打开网页函数
def open_page(driver,url):
    driver.get(url)               #打开网页
    driver.maximize_window()      #最大化浏览器窗口

# 登录账号函数
def login_fun(driver,name,passwd):
    driver.find_element_by_id("username").send_keys(name)        #定位到用户名输入框元素并输入用户名信息
    driver.find_element_by_id("password").send_keys(passwd)      #定位到密码输入框元素并输入密码信息
    driver.find_element_by_id("btnSubmit").click()               #定位到登录按钮元素并进行点击操作

# 搜索功能函数（由于单据编号输入框元素在子页面内，所以无法直接定位子页面内的元素，通过先定位到对应的子页面id属性值再切换到该子页面）
def search_fun(driver,name,url,passwd,key):
    import time                            #导入强制时间等待模块
    open_page(driver,url)                  #调用打开网页函数
    login_fun(driver,name,passwd)          #调用登录账号函数
    driver.find_element_by_xpath("//div[@id='leftMenu']//span[text()='零售出库']").click()    #定位到零售出库元素并进行点击操作
    id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")      #获取到与子页面id属性值有相同部分的其它元素id属性值
    id_iframe = id + "-frame"              #得到完整的子页面id属性值
    driver.switch_to.frame(id_iframe)      #通过子页面id属性值切换到子页面
    # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
    driver.find_element_by_id("searchNumber").send_keys(key)      #定位到单据编号输入框元素并输入数据
    driver.find_element_by_id("searchBtn").click()                #定位到查询按钮元素并进行点击操作
    time.sleep(2)                          #强制等待2s
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text    #获取单据编号的文本内容
    return num
