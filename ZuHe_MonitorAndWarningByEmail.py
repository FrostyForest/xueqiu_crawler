from selenium import webdriver
from lxml import etree
from Xueqiu_LoginThroughVerificationCode import return_xueqiu_cookie
import time
from send_email import send_email

ZuHe_list=['ZH154076','ZH2119969']
while 1:
    for ZuHe_Name in ZuHe_list:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')#后台运行
        option.add_argument(r"user-data-dir=C:\Users\林海\AppData\Local\Google\Chrome\User Data")#直接使用已登录的本地配置文件跳过登录
        driver = webdriver.Chrome(options=option)
        url="https://xueqiu.com/P/"+ZuHe_Name
        driver.get(url)
        time.sleep(0.5)







        # c=return_xueqiu_cookie()
        # fp=open('./cookie.txt','w',encoding='utf-8')
        # fp.write(str(c))
        # fp=open('./cookie.txt','r',encoding='utf-8')
        # line=fp.readline()
        # driver.get('https://xueqiu.com/P/ZH305371')
        # Cookie=line
        # Cookie = Cookie.split(';')#处理文本cookie
        # for attribute in Cookie:
        #     tmp = attribute.split('=')
        #     if len(tmp)==2:
        #         driver.add_cookie({'name':tmp[0], 'value':tmp[1]})
        #
        #
        # # for attribute in Cookie:#处理数据cookie
        # #     driver.add_cookie({'name':attribute[0], 'value':attribute[1]})
        #
        # driver.get('https://xueqiu.com/P/ZH305371')
        # time.sleep(10)


        btn=driver.find_element_by_class_name('history')
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(0.5)#一定要等待网页加载出来
        page_text=driver.page_source#获取页面源码
        tree=etree.HTML(page_text)#建立e树
        li_list=tree.xpath('//*[@id="cube-weight"]/div[2]/div[3]/ul[1]/div//text()')#从网页读取到的信息
        driver.quit()
        old_file=ZuHe_Name+".txt"
        f1=open(old_file,'r',encoding='utf-8')
        trade_old=f1.readlines()#旧的交易记录
        if len(trade_old)!=0:
            trade_old=trade_old[0]#注意，从文件读取到的是一个字符串列表而非字符串
        trade_new=""
        for i in range(0,len(li_list)):
            if li_list[i]!=" ":
                if i!=(len(li_list)-1):
                    trade_new=trade_new+str(li_list[i])+" "
                else:
                    trade_new = trade_new + str(li_list[i])
        print(trade_new)
        print(trade_old)

        if trade_new!=trade_old:
            f1 = open(old_file, 'w', encoding='utf-8')
            f1.writelines(trade_new)
            send_email(trade_new)
        time.sleep(5)

