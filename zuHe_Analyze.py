import numpy
import numpy as np
import pandas as pd
import csv
from get_ZuHe_NetValueData import get_ZuheNetValue

def zuHe_SharpRation_Calculate(zuhe_name):

    get_ZuheNetValue(zuhe_name)

    fp=open('./%s.csv'%(zuhe_name),'r',encoding='utf-8')
    reader=csv.reader(fp)
    next(reader)#跳过第一行

    netValue=[]
    date=[]
    daily_profitRate=[0]
    for row in reader:
        netValue.append(float(row[1]))
        date.append(pd.to_datetime(row[0]))

    netValue = np.asarray(netValue) #转换为numpy数组

    for i in range(1,len(netValue)):
        x=(netValue[i]-netValue[i-1])/netValue[i-1]
        daily_profitRate.append(x)
    zuhe_days=(date[len(date)-1]-date[0]).days#获取相差时间并转换成数字
    annualized_Return=np.power((netValue[len(netValue)-1]-netValue[0]),365.25/zuhe_days)-1#年化收益率
    nonRisk_interest=0.04#无风险利率
    annualized_VibrationRate=numpy.std(daily_profitRate)*numpy.sqrt(250)#年化收益波动率
    sharpeRatio=(annualized_Return-nonRisk_interest)/annualized_VibrationRate#夏普比率
    return sharpeRatio


