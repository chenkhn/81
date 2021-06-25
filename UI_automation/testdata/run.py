from commen import method            #导入（关联）method.py
from testdata import data            #导入（关联）data.py
from selenium import webdriver       #导入selenium库中的webdriver库
driver1 = webdriver.Chrome()         #webdriver库与Chrome浏览器建立会话（连接webdriver库和Chrome浏览器）
driver1.implicitly_wait(10)          #隐式等待10s

url1 = data.data_t["url"]            #字典取值，取url的值再参数化
name1 = data.data_t["name"]          #字典取值，取name的值再参数化
passwd1 = data.data_t["passwd"]      #字典取值，取passwd的值再参数化
key1 = data.data_t["key"]            #字典取值，取key的值再参数化

result = method.search_fun(driver=driver1,url=url1,name=name1,passwd=passwd1,key=key1)     #调用搜索功能函数，关键字传参
if key1 in result:          #判断搜索功能是否正常
    print("搜索成功")
else:
    print("搜索失败")