import os
from multiprocessing.dummy import Pool
from selenium import webdriver

pool=Pool(3)#实例化线程池对象
zuHe_list=['ZH2034329','ZH2473346']
def multiple_web(ZuHe_Name):
    option = webdriver.ChromeOptions()
    #option.add_argument('headless')  # 后台运行
    option.add_argument(r"user-data-dir=C:\Users\林海\AppData\Local\Google\Chrome\User Data")  # 直接使用已登录的本地配置文件跳过登录
    driver = webdriver.Chrome(options=option)
    url = "https://xueqiu.com/P/" + ZuHe_Name
    driver.get(url)
pool.map(multiple_web,zuHe_list)#多线程处理get_page函数