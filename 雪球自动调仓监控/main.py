#coding:utf-8
import os
import time
import sys
sys.path.append(r'C:\Users\林海\PycharmProjects\cookie_monitor')
from monitorAndReturn_TradedZuhe import zuHe_list_Monitor_send_email

os.system('chcp 65001')#将cmd编码格式从gbk变为utf
start = time.perf_counter()
end=time.perf_counter()
while 1:
    ZuHe_list = ['ZH2119969', 'ZH3099261', 'ZH3050233', 'ZH2579014', 'ZH2020519', 'ZH3112909','ZH2415922']
    zuHe_list_Monitor_send_email(ZuHe_list)
    #os.system('python ZuHe_MonitorAndWarningByEmail.py')
    os.system('python Auto_BuyAndSold_跟着大佬走.py')
    os.system('python Auto_BuyAndSold_跟着大佬走2.py')
    os.system('python Auto_BuyAndSold_跟着大佬走3.py')
    print(round(time.perf_counter()-end))
    end=time.perf_counter()
