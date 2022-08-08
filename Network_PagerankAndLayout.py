import networkx as nx
import matplotlib.pyplot as plt
import csv


# G = nx.DiGraph()
#
# a = []
# f = open('follow_name_3.txt','r',encoding='utf-8')
# line = f.readline()
# while line:
#     a.append(line.split())
# #保存文件是以空格分离的
#     line = f.readline()
# f.close()
#
#
# #将txt转csv
# fp = open('follow_name_3.csv','w',encoding='utf_8_sig',newline="")
# csvwriter=csv.writer(fp)
# csvwriter.writerows(a)
# print("to csv finish")
#
#
#
#
# #清洗txt数据再输出
# fp = open('follow_name_3_1.txt','w',encoding='utf-8')
# for x in a:
#     y=[x[0],x[1]]
#     str=" ".join(y)
#     fp.write(str+"\n")
# print("wash data finish")


#pagerank结点排序算法和spring_layout分布算法(点太多用不了）
G = nx.DiGraph()

a = []
f = open('follow_name_3_1.txt','r',encoding='utf-8')
line = f.readline()
while line:
    a.append(line.split())#保存文件是以空格分离的

    line = f.readline()
f.close()
G.add_edges_from(a)

pagerank_list=nx.pagerank(G,alpha=1)
sorted_page=sorted(pagerank_list.items(),key=lambda x:x[1],reverse=True)#根据pagerank值对结点字典进行降序排序

fp=open('rank_result_3.txt','w',encoding='utf-8')
print(sorted_page[0])
for i in sorted_page:
    t=''
    for j in i:
        t=t+str(j)+' '
    t=t+"\n"
    fp.write(t)
print("rank finish")