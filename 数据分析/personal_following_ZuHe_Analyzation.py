from selenium import webdriver
import time
import csv
from lxml import etree
import re
from zuHe_Analyze import zuHe

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 后台运行
option.add_argument(r"user-data-dir=C:\Users\林海\AppData\Local\Google\Chrome\User Data")  # 直接使用已登录的本地配置文件跳过登录
driver = webdriver.Chrome(options=option)
url = 'https://xueqiu.com/u/8137901980#/portfolio'
driver.get(url)
time.sleep(0.5)
focus_zuhe_button=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/a[2]')
driver.execute_script("arguments[0].click();", focus_zuhe_button)#点击关注的组合按钮
time.sleep(0.5)
page_text=driver.page_source#获取页面源码
tree=etree.HTML(page_text)#建立e树
driver.quit()
follow_zuhe_number=len(tree.xpath('/html/body/div[1]/div[3]/div[1]/table/tbody/tr'))#关注的组合数目
zuhe_list=[]
for i in range(1,follow_zuhe_number+1):
    zuHe_code=tree.xpath('/html/body/div[1]/div[3]/div[1]/table/tbody/tr[%i]//@data-analytics-data'%(i))[0]#组合代码
    zuHe_code=re.findall(r"['](.*?)[']", zuHe_code)[0]#正则表达式提取字符串
    netValue=float(tree.xpath('/html/body/div[1]/div[3]/div[1]/table/tbody/tr[%i]/td[2]//text()'%(i))[0])#净值
    zuHe_name=tree.xpath('/html/body/div[1]/div[3]/div[1]/table/tbody/tr[%i]/td[1]/a/text()'%(i))[0]#组合名字
    zuhe=[]
    if netValue>2.1:
        zuhe.append(zuHe_code)
        zuhe.append(zuHe_name)
        zuhe_list.append(zuhe)

fp=open('following_zuhe.csv','w',newline='',encoding='utf_8_sig')
zuhe_analytic_list=[]
csvwriter=csv.writer(fp)
headr_list=['组合代码','组合名字','净值','夏普比率','持续天数']

csvwriter.writerow(headr_list)
for zuhe in zuhe_list:
    if zuhe[1]=="已关停":
        continue
    z=zuHe(zuhe[0])#送入组合代码作为参数去计算相关指标
    time.sleep(0.75)#一定要等待计算分析完成
    zuHeX=[]
    zuHeX.append(zuhe[0])#添加组合代码
    zuHeX.append(zuhe[1])#添加组合名字
    zuHeX.append(z.netValue)#添加组合净值
    zuHeX.append(z.sharpeRatio)#添加夏普比率
    zuHeX.append(z.lastingDays)#添加持续时间
    zuhe_analytic_list.append(zuHeX)
    csvwriter.writerow(zuHeX)
    print(zuhe[1]+"分析完成")
print(0)

print('finish')


