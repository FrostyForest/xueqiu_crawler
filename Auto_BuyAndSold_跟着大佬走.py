from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver.common.keys import Keys
import os.path

def autoBuyAndSold(str,ZuHe_Name,ZuHe_list):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 后台运行
    option.add_argument(r"user-data-dir=C:\Users\林海\AppData\Local\Google\Chrome\User Data")#直接使用已登录的本地配置文件跳过登录
    driver = webdriver.Chrome(options=option)
    url="https://xueqiu.com/p/update?action=holdings&symbol="+ZuHe_Name
    driver.get(url)
    time.sleep(0.2)
    page_text = driver.page_source  # 获取页面源码
    tree = etree.HTML(page_text)  # 建立e树


    trade_str=str#读取字符串数据
    original_list=trade_str.split()#转换得未经处理的原始数据

    trade_list=[[]*6 for _ in range(len(original_list)//6)]#初始化存储交易数据的数据结构


    for i in range(0,len(original_list)):
        if i%6==2 or i%6==3:#转成浮点数
            trade_list[i // 6].append(original_list[i])
            end = len(trade_list[i//6][i%6]) - 1  # 定位末尾
            trade_list[i//6][i%6] = trade_list[i//6][i%6][:end]  # 去掉%再转成浮点数
            stock_percent=float(trade_list[i//6][i%6])
            trade_list[i // 6][i % 6]=stock_percent
        else:
            trade_list[i//6].append(original_list[i])

    configuration_button = driver.find_element_by_xpath('//*[@id="cube-submit"]')  # 调仓完成键

    for trade in trade_list:

        addStock_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div[3]/div/button')#添加股票键
        stock_list = tree.xpath('/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr')  # 股票列表
        stock_str = trade[0]
        stock_num = len(stock_list)
        stock_percent = int(trade[3]/len(ZuHe_list))
        print(len(ZuHe_list))

        if trade[2]!=0 and trade[3]!=0:#交易不是新建仓位或者清仓
            for i in range(1, stock_num):  # 遍历以找到对应股票位置
                stock_name = tree.xpath(
                    '/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr[%i]//span[@class="name"]/text()' % (
                        i))[0]  # 股票名字
                print(stock_name)
                if stock_name == stock_str:
                    input_box = driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr[%i]//input[@class="weight"]' % (
                            i))  # 定位输入框
                    #input_box.click()  # 点击输入框
                    driver.execute_script("arguments[0].click();", input_box)
                    input_box.send_keys(Keys.BACK_SPACE)  # 删除框内数据
                    time.sleep(0.1)
                    input_box.send_keys('%s' % (stock_percent))  # 输入仓位%
                    time.sleep(0.1)
                    input_box.send_keys(Keys.ENTER)  # 按回车键
                    time.sleep(0.1)
                    #configuration_button.click()  # 按调仓完成键
                    break
                if i==stock_num-1:#初始列表中没有该股票
                    trade[2]=0

        if trade[2]==0:#添加股票
            #addStock_Button.click();#点击添加股票键
            driver.execute_script("arguments[0].click();", addStock_Button)
            time.sleep(0.1)
            addStock_input_box=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/input')#定位输入股票文本框
            #addStock_input_box.click()
            driver.execute_script("arguments[0].click();", addStock_input_box)
            time.sleep(0.1)
            addStock_input_box.send_keys(stock_str)#输入股票名
            time.sleep(0.5)
            addStock_input_box.send_keys(Keys.ENTER)  # 按回车键
            time.sleep(0.1)
            addStock_configuraion_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[4]/button')#定位添加股票完成按钮
            #addStock_configuraion_Button.click()#点击加股票完成按钮
            driver.execute_script("arguments[0].click();", addStock_configuraion_Button)
            time.sleep(0.2)
            page_text = driver.page_source  # 获取页面源码
            tree = etree.HTML(page_text)  # 建立e树
            stock_list = tree.xpath('/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr')  # 股票列表
            stock_num=len(stock_list)#添加完后更新数据
            print(stock_num)
            for i in range(1, stock_num):  # 遍历以找到对应股票位置
                stock_name = tree.xpath(
                    '/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr[%i]//span[@class="name"]/text()' % (
                        i))[0]  # 股票名字
                print(stock_name)
                if stock_name == stock_str:
                    input_box = driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr[%i]//input[@class="weight"]' % (
                            i))  # 定位输入框
                    #input_box.click()  # 点击输入框
                    driver.execute_script("arguments[0].click();", input_box)
                    time.sleep(0.1)
                    input_box.send_keys(Keys.BACK_SPACE)  # 删除框内数据
                    time.sleep(0.2)
                    input_box.send_keys('%s' %(stock_percent))  # 输入仓位%
                    time.sleep(0.2)
                    input_box.send_keys(Keys.ENTER)  # 按回车键
                    time.sleep(0.1)
                    #configuration_button.click()  # 按调仓完成键
                    break
        if trade[3]==0:#删除股票
            for i in range(1, stock_num):  # 遍历以找到对应股票位置
                stock_name = tree.xpath(
                    '/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr[%i]//span[@class="name"]/text()' % (
                        i))[0]  # 股票名字

                if stock_name == stock_str:
                    delete_button = driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div/div[1]/form/div[3]/div/div/table/tbody/tr[%i]//a[@class="delete"]' % (
                            i))  # 删除按钮
                    #delete_button.click()  # 点击删除按钮
                    driver.execute_script("arguments[0].click();", delete_button)
                    time.sleep(0.1)
                    delete_confuguration_button = driver.find_element_by_xpath(
                        '/html/body/div[5]/div/div/div/div[2]/button[1]')  # 定位确认按钮
                    #delete_confuguration_button.click()  # 点击确认删除按钮
                    driver.execute_script("arguments[0].click();", delete_confuguration_button)
                    time.sleep(0.1)
                    #configuration_button.click()
                    break

    #configuration_button.click()
    driver.execute_script("arguments[0].click();", configuration_button)
    time.sleep(0.4)
    driver.quit()
    return



ZuHe_list=['ZH837642','ZH154076','ZH1350829','ZH484626']#要监控的组合列表
#while 1:
for ZuHe_Name in ZuHe_list:
    option = webdriver.ChromeOptions()
    option.add_argument('headless')#后台运行
    option.add_argument(r"user-data-dir=C:\Users\林海\AppData\Local\Google\Chrome\User Data")#直接使用已登录的本地配置文件跳过登录
    driver = webdriver.Chrome(options=option)
    url="https://xueqiu.com/P/"+ZuHe_Name
    driver.get(url)
    time.sleep(0.75)







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
    time.sleep(0.75)#一定要等待网页加载出来
    page_text=driver.page_source#获取页面源码
    tree=etree.HTML(page_text)#建立e树
    li_list=tree.xpath('//*[@id="cube-weight"]/div[2]/div[3]/ul[1]/div//text()')#从网页读取到的信息
    time.sleep(0.5)
    driver.quit()
    old_file=ZuHe_Name+".txt"
    if os.path.isfile(old_file)==0:
        f1=open("%s"%(old_file),'w',encoding='utf-8')#创建文件
        f1.close()
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
    check=trade_new.split()
    if check[2]=="分红配送":#跳过分红配送
        trade_new=trade_old
    print(trade_new)
    print(trade_old)

    if trade_new!=trade_old:
        f1 = open(old_file, 'w', encoding='utf-8')
        f1.writelines(trade_new)
        autoBuyAndSold(trade_new,'ZH2307994',ZuHe_list)#要调仓的组合
    time.sleep(0.5)











