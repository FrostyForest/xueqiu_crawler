from monitorAndReturn_TradedZuhe import zuHe_list_Monitor
from monitorAndReturn_TradedZuhe import zuHe_list_Monitor_send_email
from zuHe_BuyAndSold import autoBuyAndSold
import time
from retrying import retry
import os
end = time.perf_counter()


while 1:
    try:
        send_email_zuhe_list=['ZH2119969','ZH3099261','ZH3050233','ZH3068612','ZH2579014',]
        zuHe_list_Monitor_send_email(send_email_zuhe_list)
        print("完成对组合列表的监控")


        autoTrade_zuhe_list_list=[
        ['ZH2307994',['ZH3099261','ZH3050233','ZH2514120','ZH3094661']],
        ['ZH2311106',['ZH3068612','ZH2579014','ZH2531440','ZH2263951']],
        ['ZH2290020',['ZH2479682','ZH2512650','ZH2884640','ZH2119969']]

                        ]
        for zuHe_list in autoTrade_zuhe_list_list:

            traded_str_list=[]#存放交易信息的列表
            traded_zuhe_list=zuHe_list_Monitor(zuHe_list[1],zuHe_list[0])
            for traded_zuhe in traded_zuhe_list:#读取交易了的组合的交易信息

                filename=traded_zuhe + "_" + zuHe_list[0] + ".txt"#要读取的文件名
                fp=open('./%s'%(filename),'r',encoding='utf-8')
                traded_str_list.append(fp.readline())
            for str in traded_str_list:#交易信息逐个交给交易函数处理
                if len(traded_zuhe_list)!=0:
                    autoBuyAndSold(str,zuHe_list[0],zuHe_list[1])#0:要自动调仓的组合，1：要监控的组合列表
            print("完成对" + zuHe_list[0] + "的自动调仓")
        time.sleep(4)
        print(round(time.perf_counter() - end))
        end = time.perf_counter()
    except KeyError:
        print('发生错误，进入休眠')
        time.sleep(21)
        print('再启动')






