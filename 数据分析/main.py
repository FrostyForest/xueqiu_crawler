import time


from get_user_focus_ZuHe import  get_user_focus_ZuHe
from zuHe_Analyze import zuHe
from multiprocessing.dummy import Pool
import csv

visited_zuhe=set()#用于存储已经计算过的组合代号

fpr = open('./analytic_zuhe_list.csv', 'r', newline='', encoding='utf_8_sig',buffering=1)
csvreader=csv.reader(fpr)
header = next(csvreader)
for row in csvreader:#读取已经计算过的组合
    visited_zuhe.add(row[0])
fpr.close()



fpr=open('./follow_name.txt','r',encoding='utf_8_sig')

zuhe_analytic_list=[]

fpw = open('./analytic_zuhe_list.csv', 'a', newline='', encoding='utf_8_sig',buffering=1)
fpw1 = open('./visited_zuhe_list.csv', 'w', newline='', encoding='utf_8_sig',buffering=1)#存储已访问过的组合
csvwriter=csv.writer(fpw)
csvwriter1=csv.writer(fpw1)
# headr_list=['组合代码','组合名字','净值','夏普比率','持续天数','最大回撤','净值最后日期']#写标题行
# csvwriter.writerow(headr_list)

user_list_data=fpr.readlines()
fpr.close()
for row in user_list_data:#遍历用户表
    row=row.split()
    user_id=row[4]#获取用户id
    user_focus_zuhe_list=get_user_focus_ZuHe(user_id)
    if len(user_focus_zuhe_list)<1:#如果关注组合数少于一，跳过
        continue
    data_list = []

    def zuhe_proceed(zuhe_id,zuhe_name,data_list):#并行执行的部分
        if zuhe_id[0]=='S':
            return
        if zuhe_id in visited_zuhe:
            print('zuhe_id in visited_zuhe!')
            return
        zuhe=zuHe(zuhe_id)#对相应组合进行相关数据处理
        visited_zuhe.add(zuhe_id)
        data=[zuhe_id]
        csvwriter1.writerow(data)
        meta_data = [zuhe_id, zuhe_name, zuhe.netValue, zuhe.sharpeRatio, zuhe.lastingDays, zuhe.max_recession,zuhe.the_last_day]
        print(meta_data)
        if zuhe.netValue<2 or zuhe.lastingDays<180 or zuhe.sharpeRatio<1.5:
            print("not good enough")
            return
        meta_data=[zuhe_id,zuhe_name,zuhe.netValue,zuhe.sharpeRatio,zuhe.lastingDays,zuhe.max_recession,zuhe.the_last_day]
        if len(meta_data)!=0:
            csvwriter.writerow(meta_data)
            print("%s已加入组合列表"%(zuhe_name))

    #pool = Pool(4)
    print(row[1])
    print(user_focus_zuhe_list)
    for x in user_focus_zuhe_list:
        #pool.apply_async(zuhe_proceed,(x[0],x[1],data_list))#并发执行
        zuhe_proceed(x[0],x[1],data_list)#顺序执行
    # pool.close()
    # # 等待po中所有子进程执行完成，必须放在close语句之后
    # pool.join()
    print("%s用户的关注组合分析完成"%(row[1]))
    # 关闭进程池，关闭后po不再接收新的请求

fpw.close()
fpw1.close()








