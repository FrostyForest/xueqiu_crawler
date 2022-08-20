import numpy
import numpy as np
import pandas as pd
import csv
from get_ZuHe_NetValueData import get_ZuheNetValue
import os

class zuHe:
    name = ''
    sharpRation = 1.0#夏普比率
    lastingDays=100#组合持续时间
    netValue=1#净值
    max_recession=0.0#最大回撤
    the_last_day=""#最后净值日期
    def __init__(self,zuhe_name):
        self.name=zuhe_name
        file_path='./%s.csv'%(zuhe_name)
        if os.path.isfile(file_path) and os.path.getsize(file_path)!=0:#如果目录下已存在组合净值文件，则跳过请求
            pass
        else:
            get_ZuheNetValue(zuhe_name)#获取净值

        fp=open(file_path,'r',encoding='utf-8')
        reader=csv.reader(fp)
        next(reader)#跳过第一行


        netValue=[]
        date=[]
        daily_profitRate=[0]
        today_recession = [0]
        for row in reader:
            netValue.append(float(row[1]))
            date.append(pd.to_datetime(row[0]))
        if len(netValue)==0:
            netValue.append(1)
            date.append(pd.to_datetime('2017-06-27'))
        netValue = np.asarray(netValue) #转换为numpy数组

        fp=open('./%s.csv'%(zuhe_name),'w',encoding='utf-8',newline="")
        highest_netValue=1

        csvwriter=csv.writer(fp)

        row=[date[0].strftime('%Y-%m-%d'),netValue[0],0,0]#日期，净值，收益率，回撤
        csvwriter.writerow(row)

        for i in range(1,len(netValue)):
            x=(netValue[i]-netValue[i-1])/netValue[i-1]#求今日收益率
            daily_profitRate.append(x)
            if netValue[i] >highest_netValue:
                highest_netValue=netValue[i]
            recession=(netValue[i]-highest_netValue)/highest_netValue
            today_recession.append(recession)
            if recession<self.max_recession:
                self.max_recession=recession
            row=[date[i].strftime('%Y-%m-%d'),netValue[i],x,recession]
            csvwriter.writerow(row)


        zuhe_days=(date[len(date)-1]-date[0]).days#获取相差时间并转换成数字
        if zuhe_days==0:
            zuhe_days=1
        print(zuhe_days)
        if zuhe_days<2 :
            annualized_Return=0
        else:
            annualized_Return=np.power((netValue[len(netValue)-1]-netValue[0]),365.25/zuhe_days)-1#年化收益率
        nonRisk_interest=0.04#无风险利率
        annualized_VibrationRate=numpy.std(daily_profitRate)*numpy.sqrt(250)#年化收益波动率
        self.sharpeRatio=(annualized_Return-nonRisk_interest)/annualized_VibrationRate#夏普比率
        self.netValue=netValue[len(netValue)-1]
        self.lastingDays=len(date)
        self.the_last_day=date[len(date)-1].strftime('%Y-%m-%d')

zuHe('ZH2013543')
