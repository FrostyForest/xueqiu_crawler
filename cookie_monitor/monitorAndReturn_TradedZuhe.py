import requests
import datetime,time
import os
from multiprocessing.dummy import Pool
from send_email import send_email
import random
from zuHe_BuyAndSold import autoBuyAndSold

# def time_stamp_proceed(timeStamp):#处理时间戳，返回字符串格式的时间
#     # 转换成localtime
#     time_local = time.localtime(timeStamp / 1000)
#     # 转换成新的时间格式(精确到秒)
#     time_local = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
#     return time_local

def zuHe_list_Monitor_send_email(zuHe_list):#实现对组合列表里的组合进行监控，若某个组合发生调仓，则添加进列表中，最后返回要调仓的组合列表
    trade_zuHe_list=[]
    parameter_list=[]
    for zuHe in zuHe_list:
        parameter_list.append([zuHe,trade_zuHe_list])

    def zuHe_Monitor(parameter):
        zuHe=parameter[0]
        trade_zuHe_list=parameter[1]
        url = 'https://xueqiu.com/cubes/rebalancing/history.json'
        headers = {
            'Cookie': 'Hm_lvt_1db88642e346389874251b5a1eded6e3=1660094558,1660112860,1660199534,1660227307; device_id=37775ef18cf8cc43dfb743be1f6164f0; s=dh16ckpaj6; bid=788a6f04f2f6a9185ca8ae0131b3474e_l63r39o3; xq_r_token=db0dda862d174620d32e19cbcecb1a6b661c2d5e; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjgxMzc5MDE5ODAsImlzcyI6InVjIiwiZXhwIjoxNjYyODIzMjM4LCJjdG0iOjE2NjAyMzEyMzg5OTcsImNpZCI6ImQ5ZDBuNEFadXAifQ.F6IlS_6gLofm1yYSkVo2qP9mp9FIJrDwEo_OkcxrdtUFqbQUFwDOMYycaUAchWxCH0HrMPD27IbmiIDYUkBffNfROf1IZ5nXbaxurXDdObC6qbCWqZemMFkUPtz5wQOM9It6OHpTm_TRb6CUiOm6rmJwXWSgUey4MZZxoK201L0OE-LvEcEnilaGswPQ6OnzgcRcD1HsB6JRzBC4wrNpjA_-EWBwDUcclAIGz2hSNyCXZ9wmYbTVGz31_6nNZ4GgZEIkxu6TllPK6XXOH9A7W7UB_sstSkaqOUFew6f5mhPk3VgYOEarUHX9u6qZv--skzl5TLtxxLvCXM8AKXO5EA; u=8137901980; remember=1; xq_is_login=1; __utma=1.1364056698.1659975384.1660143413.1660234746.6; __utmz=1.1659975384.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660234837; xq_a_token=ca52d54d188574657b987f0a10390ee53aeaf875; xqat=ca52d54d188574657b987f0a10390ee53aeaf875; acw_tc=276077a416602345122265780e0937a34bf43d9a45e4c80f8ae41b2cd43c51; __utmb=1.5.10.1660234746; __utmc=1; __utmt=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
        }
        param = {
            'cube_symbol': zuHe,
            'count': '20',
            'page': '1'
        }
        session = requests.session()
        session.keep_alive = False
        response = session.get(url=url, params=param, headers=headers).json()
        sleep_time=random.uniform(0.2,0.5)
        time.sleep(sleep_time)
        session.close()
        trade_count = len(response['list'][0]['rebalancing_histories'])  # 要调仓的次数
        trade_data_new = []
        trade_new=""
        for i in range(0, trade_count):

            stock_name = response['list'][0]['rebalancing_histories'][i]['stock_name']  # 股票名字
            stock_code = response['list'][0]['rebalancing_histories'][i]['stock_symbol']  # 股票代码

            stock_prev_weight = response['list'][0]['rebalancing_histories'][i]['prev_weight']  # 股票调仓前仓位
            stock_target_weight = response['list'][0]['rebalancing_histories'][i]['target_weight']  # 股票调仓后仓位
            stock_prev_price = response['list'][0]['rebalancing_histories'][i]['prev_price']  # 股票之前价格

            stock_price = response['list'][0]['rebalancing_histories'][i]['price']  # 股票现在价格


            if stock_target_weight!=None and stock_prev_weight!=None and (stock_target_weight - stock_prev_weight) < 1 and(stock_target_weight - stock_prev_weight) > 0:  # 跳过分红送配
                continue
            trade_data_new.append(stock_name)
            trade_new=trade_new+stock_name+" "
            trade_data_new.append(stock_code)
            trade_new = trade_new + stock_code+" "
            trade_data_new.append(stock_prev_weight)
            trade_new = trade_new + str(stock_prev_weight) + " "
            trade_data_new.append(stock_target_weight)
            trade_new = trade_new + str(stock_target_weight) + " "
            trade_data_new.append(stock_prev_price)
            trade_new = trade_new + str(stock_prev_price) + " "
            trade_data_new.append(stock_price)
            trade_new = trade_new + str(stock_price)+" "


        current_fileName = os.path.basename(__file__).split('.')[0]
        old_file = zuHe + "_" + "watching_by_me" + ".txt"  # 建立专属文件名

        if os.path.isfile(old_file) == 0:
            f1 = open("%s" % (old_file), 'w', encoding='utf-8')  # 创建文件
            f1.close()
        f1 = open(old_file, 'r', encoding='utf-8')
        trade_old = f1.readlines()  # 旧的交易记录
        if len(trade_old) != 0:
            trade_old = trade_old[0]  # 注意，从文件读取到的是一个字符串列表而非字符串

        # print(trade_new)
        # print(trade_old)
        if trade_new != trade_old and trade_new!="":

            f1 = open(old_file, 'w', encoding='utf-8')
            f1.writelines(trade_new)
            send_email(trade_new)
            trade_zuHe_list.append(zuHe)

        time.sleep(0.2)


    pool = Pool(5)  # 实例化线程池对象
    pool.map(zuHe_Monitor, parameter_list)  # 多线程处理函数
    pool.close()        # 关闭进程池，不再接受新的进程
    pool.join()         # 主进程阻塞等待子进程的退出
    print(trade_zuHe_list)#要调仓的组合
    return trade_zuHe_list

########################
def zuHe_list_Monitor(zuHe_list,watcher_zuhe):#实现对组合列表里的组合进行监控，若某个组合发生调仓，则添加进列表中，最后返回要调仓的组合列表
    trade_zuHe_list=[]
    parameter_list=[]#[][0]为要监控的某个组合
    for zuHe in zuHe_list:
        parameter_list.append([zuHe,trade_zuHe_list])

    def zuHe_Monitor(parameter):
        zuHe=parameter[0]
        trade_zuHe_list=parameter[1]
        url = 'https://xueqiu.com/cubes/rebalancing/history.json'
        headers = {
            'Cookie': 'Hm_lvt_1db88642e346389874251b5a1eded6e3=1660094558,1660112860,1660199534,1660227307; device_id=37775ef18cf8cc43dfb743be1f6164f0; s=dh16ckpaj6; bid=788a6f04f2f6a9185ca8ae0131b3474e_l63r39o3; xq_r_token=db0dda862d174620d32e19cbcecb1a6b661c2d5e; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjgxMzc5MDE5ODAsImlzcyI6InVjIiwiZXhwIjoxNjYyODIzMjM4LCJjdG0iOjE2NjAyMzEyMzg5OTcsImNpZCI6ImQ5ZDBuNEFadXAifQ.F6IlS_6gLofm1yYSkVo2qP9mp9FIJrDwEo_OkcxrdtUFqbQUFwDOMYycaUAchWxCH0HrMPD27IbmiIDYUkBffNfROf1IZ5nXbaxurXDdObC6qbCWqZemMFkUPtz5wQOM9It6OHpTm_TRb6CUiOm6rmJwXWSgUey4MZZxoK201L0OE-LvEcEnilaGswPQ6OnzgcRcD1HsB6JRzBC4wrNpjA_-EWBwDUcclAIGz2hSNyCXZ9wmYbTVGz31_6nNZ4GgZEIkxu6TllPK6XXOH9A7W7UB_sstSkaqOUFew6f5mhPk3VgYOEarUHX9u6qZv--skzl5TLtxxLvCXM8AKXO5EA; u=8137901980; remember=1; xq_is_login=1; __utma=1.1364056698.1659975384.1660143413.1660234746.6; __utmz=1.1659975384.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660234837; xq_a_token=ca52d54d188574657b987f0a10390ee53aeaf875; xqat=ca52d54d188574657b987f0a10390ee53aeaf875; acw_tc=276077a416602345122265780e0937a34bf43d9a45e4c80f8ae41b2cd43c51; __utmb=1.5.10.1660234746; __utmc=1; __utmt=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
        }
        param = {
            'cube_symbol': zuHe,
            'count': '20',
            'page': '1'
        }
        session=requests.session()
        session.keep_alive = False
        session.get("https://xueqiu.com/P/ZH2311106", headers=headers)
        sleep_time = random.uniform(0, 2)
        time.sleep(sleep_time)
        response = session.get(url=url, params=param, headers=headers).json()
        sleep_time=random.uniform(0.2,0.75)
        time.sleep(sleep_time)
        session.close()

        trade_count = len(response['list'][0]['rebalancing_histories'])  # 要调仓的次数

        trade_data_new = []
        trade_new=""
        for i in range(0, trade_count):

            stock_name = response['list'][0]['rebalancing_histories'][i]['stock_name']  # 股票名字
            stock_code = response['list'][0]['rebalancing_histories'][i]['stock_symbol']  # 股票代码

            stock_prev_weight = response['list'][0]['rebalancing_histories'][i]['prev_weight']  # 股票调仓前仓位
            stock_target_weight = response['list'][0]['rebalancing_histories'][i]['target_weight']  # 股票调仓后仓位
            stock_prev_price = response['list'][0]['rebalancing_histories'][i]['prev_price']  # 股票之前价格

            stock_price = response['list'][0]['rebalancing_histories'][i]['price']  # 股票现在价格


            if stock_target_weight!=None and stock_prev_weight!=None and (stock_target_weight - stock_prev_weight) < 1 and(stock_target_weight - stock_prev_weight) > 0:  # 跳过分红送配
                continue
            trade_data_new.append(stock_name)
            trade_new=trade_new+stock_name+" "
            trade_data_new.append(stock_code)
            trade_new = trade_new + stock_code+" "
            trade_data_new.append(stock_prev_weight)
            trade_new = trade_new + str(stock_prev_weight) + " "
            trade_data_new.append(stock_target_weight)
            trade_new = trade_new + str(stock_target_weight) + " "
            trade_data_new.append(stock_prev_price)
            trade_new = trade_new + str(stock_prev_price) + " "
            trade_data_new.append(stock_price)
            trade_new = trade_new + str(stock_price)+" "


        current_fileName = os.path.basename(__file__).split('.')[0]
        old_file = zuHe + "_" + watcher_zuhe + ".txt"  # 建立专属文件名

        if os.path.isfile(old_file) == 0:
            f1 = open("%s" % (old_file), 'w', encoding='utf-8')  # 创建文件
            f1.close()
        f1 = open(old_file, 'r', encoding='utf-8')
        trade_old = f1.readlines()  # 旧的交易记录
        if len(trade_old) != 0:
            trade_old = trade_old[0]  # 注意，从文件读取到的是一个字符串列表而非字符串


        if trade_new != trade_old and trade_new!="":

            f1 = open(old_file, 'w', encoding='utf-8')
            f1.writelines(trade_new)
            #send_email(trade_new)
            trade_zuHe_list.append(zuHe)

        time.sleep(0.25)


    pool = Pool(4)  # 实例化线程池对象
    pool.map(zuHe_Monitor, parameter_list)  # 多线程处理函数
    time.sleep(0.5)

    print(trade_zuHe_list)#要调仓的组合
    return trade_zuHe_list




