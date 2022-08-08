# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# noinspection PyUnresolvedReferences
import requests
import json
from multiprocessing.dummy import Pool
if __name__ == '__main__':
    print_hi('PyCharm')




def xueqiu_user(uid,visited_user,sum):
    if sum>5:#限制递归深度
        return
    #获取当前用户名和粉丝数
    url='https://xueqiu.com/statuses/original/show.json'
    headers = {
        'Cookie': '__utma=1.1344804606.1616770344.1621000413.1621002956.5; device_id=ed257993933a55e01f20a879a7cc945a; xq_a_token=bf75ab4bcea18c79de253cb841f2b27e248d8948; xqat=bf75ab4bcea18c79de253cb841f2b27e248d8948; xq_r_token=c7d30dc738a77dd909a8228f3053679e86bf104b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2MTgxNjI0MSwiY3RtIjoxNjU5NzEyNTE0ODg4LCJjaWQiOiJkOWQwbjRBWnVwIn0.ZqNVrli8Qdh2Uc9zJGApN7EKmZP4XCbQX64cPVfPu9oN1mG5BXxWOjkpEkFG4iVKYiHaX9TZrdRYrC2ta6MezyOE4gxq1dAyDhR5y5vVe1xoND0eJETOYx9w3um9SrboA5WVJjaM2988Z_vDwYYK9jIUDhWx0F9mGrZgx5gJug9IXrtszKwQ9EY6mWlST0oI3feaVsI7jk1Gj5BZTTjPDGaK2huFeT4b0E_QGf4p9CsSoGdnPcX-f9QGC_0RXnE2_g2CBOCd_xIhQQQ1S5lWG8n4Zth7pNw3CKp1pKO1NfWT8TD0Gv4wHEBC7TwqScWlqe7awDIvvGCHN8kCWVfTBA; u=231659712550633; Hm_lvt_1db88642e346389874251b5a1eded6e3=1659244628,1659247220,1659712550; s=db11inxq16; acw_tc=276077ae16597204266158605e906274bd98f161954c2ec77fb31d8dd268bf; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1659722028',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
    }
    param = {
        'user_id': uid,

    }
    response = requests.get(url=url, params=param, headers=headers).json()
    user_name=response['user']['screen_name']#用户名

    if visited_user.count(uid)==0:#将该用户的uid添加到已访问过的uid列表
        visited_user.append(uid)
    else:
        return

    #获取关注的用户
    url='https://xueqiu.com/friendships/groups/members.json'
    session= requests.Session()
    headers={
        'Cookie':'__utma=1.1344804606.1616770344.1621000413.1621002956.5; device_id=ed257993933a55e01f20a879a7cc945a; xq_a_token=bf75ab4bcea18c79de253cb841f2b27e248d8948; xqat=bf75ab4bcea18c79de253cb841f2b27e248d8948; xq_r_token=c7d30dc738a77dd909a8228f3053679e86bf104b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2MTgxNjI0MSwiY3RtIjoxNjU5NzEyNTE0ODg4LCJjaWQiOiJkOWQwbjRBWnVwIn0.ZqNVrli8Qdh2Uc9zJGApN7EKmZP4XCbQX64cPVfPu9oN1mG5BXxWOjkpEkFG4iVKYiHaX9TZrdRYrC2ta6MezyOE4gxq1dAyDhR5y5vVe1xoND0eJETOYx9w3um9SrboA5WVJjaM2988Z_vDwYYK9jIUDhWx0F9mGrZgx5gJug9IXrtszKwQ9EY6mWlST0oI3feaVsI7jk1Gj5BZTTjPDGaK2huFeT4b0E_QGf4p9CsSoGdnPcX-f9QGC_0RXnE2_g2CBOCd_xIhQQQ1S5lWG8n4Zth7pNw3CKp1pKO1NfWT8TD0Gv4wHEBC7TwqScWlqe7awDIvvGCHN8kCWVfTBA; u=231659712550633; Hm_lvt_1db88642e346389874251b5a1eded6e3=1659244628,1659247220,1659712550; s=db11inxq16; acw_tc=276077ae16597204266158605e906274bd98f161954c2ec77fb31d8dd268bf; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1659722028',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
    }

    param={
        'uid': uid,
        'page': '1',
        'gid':'0'
    }
    response=requests.get(url=url,params=param,headers=headers).json()#发起get请求
    page_number=int(response['maxPage'])
    follow_name=[]#关注用户名字
    uid_list=[]#关注用户的uid
    n=1
    response_list=[]#响应列表
    page_list=[]
    for i in range(1,page_number+1):
        page_list.append([i,response_list])
    if page_number<110:
        def get_page(page):#封装函数便于多线程处理
            headers = {
                'Cookie': '__utma=1.1344804606.1616770344.1621000413.1621002956.5; device_id=ed257993933a55e01f20a879a7cc945a; xq_a_token=bf75ab4bcea18c79de253cb841f2b27e248d8948; xqat=bf75ab4bcea18c79de253cb841f2b27e248d8948; xq_r_token=c7d30dc738a77dd909a8228f3053679e86bf104b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2MTgxNjI0MSwiY3RtIjoxNjU5NzEyNTE0ODg4LCJjaWQiOiJkOWQwbjRBWnVwIn0.ZqNVrli8Qdh2Uc9zJGApN7EKmZP4XCbQX64cPVfPu9oN1mG5BXxWOjkpEkFG4iVKYiHaX9TZrdRYrC2ta6MezyOE4gxq1dAyDhR5y5vVe1xoND0eJETOYx9w3um9SrboA5WVJjaM2988Z_vDwYYK9jIUDhWx0F9mGrZgx5gJug9IXrtszKwQ9EY6mWlST0oI3feaVsI7jk1Gj5BZTTjPDGaK2huFeT4b0E_QGf4p9CsSoGdnPcX-f9QGC_0RXnE2_g2CBOCd_xIhQQQ1S5lWG8n4Zth7pNw3CKp1pKO1NfWT8TD0Gv4wHEBC7TwqScWlqe7awDIvvGCHN8kCWVfTBA; u=231659712550633; Hm_lvt_1db88642e346389874251b5a1eded6e3=1659244628,1659247220,1659712550; s=db11inxq16; acw_tc=276077ae16597204266158605e906274bd98f161954c2ec77fb31d8dd268bf; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1659722028',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
            }
            param = {  # get请求参数
                'uid': uid,
                'page': str(page[0]),
                'gid': '0'
            }
            response = requests.get(url=url, params=param, headers=headers).json()
            page[1].append(response)
            return

        pool=Pool(10)#实例化线程池对象
        pool.map(get_page,page_list)#多线程处理get_page函数

        n=1
        for j in response_list:
            print(n)
            n=n+1
            for i in range(0,len(j['users'])):
                following=[user_name,j['users'][i]['screen_name'],j['users'][i]['followers_count']]#元数据
                follow_name.append(following)
                uid_list.append(j['users'][i]['id'])

        fp = open('./follow_name.txt','a',encoding='utf-8')
        for i in follow_name:#将列表转字符串
            str1=''
            for j in i:
                str1=str1+str(j)+' '
            str1=str1+"\n"
            fp.write(str1)
        for uid1 in uid_list:
            if visited_user.count(uid1) == 0:#检查是否已访问过该用户，若访问过则不可再访问
                xueqiu_user(uid1,visited_user,sum+1)#递归

        return
    else:
        return



#-------------------------------------调试
visited_user=[]
xueqiu_user('8261590817',visited_user,1)


