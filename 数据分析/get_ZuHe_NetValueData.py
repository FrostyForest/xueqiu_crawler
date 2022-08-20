import time

import requests
import csv
import random
def get_ZuheNetValue(ZuHe_name):
    #ip池
    # proxy=[]
    # fp=open('./http.txt','r',encoding='utf-8')
    # ip_list=fp.readlines()
    # for row in ip_list:
    #     ip_address1='http://'+row
    #     ipdict={
    #         'http':ip_address1.strip("\n"),
    #     }
    #     proxy.append(ipdict)
    # fp.close()
    sucess=0
    while sucess!=1:
        try:
            url='https://xueqiu.com/cubes/nav_daily/all.json'
            proxy=[
                {
                'http':'http://221.181.238.59:9091'
                },
                {
                    'http': 'http://47.102.123.36:3128'
                },
                {
                    'https': 'https://113.31.118.22:80'
                },
                {
                    'http': 'http://106.15.93.221:8080'
                },
                {
                    'http': 'http://222.66.94.130:80'
                },
                {
                    'http': 'http://114.67.104.36:18888'
                },
                {
                    'http': 'http://58.246.58.150:9002'
                },
            ]
            headers = [
                {
                'Cookie':'device_id=6937eed60f66b1afaae2e099ee61d34a; s=c512byykvs; cookiesu=851660138162231; remember=1; xq_is_login=1; u=8137901980; bid=788a6f04f2f6a9185ca8ae0131b3474e_l6nr1hdk; xq_a_token=ca52d54d188574657b987f0a10390ee53aeaf875; xqat=ca52d54d188574657b987f0a10390ee53aeaf875; xq_r_token=db0dda862d174620d32e19cbcecb1a6b661c2d5e; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjgxMzc5MDE5ODAsImlzcyI6InVjIiwiZXhwIjoxNjYyODIzMjM4LCJjdG0iOjE2NjAyNjc2NzI1NTAsImNpZCI6ImQ5ZDBuNEFadXAifQ.n6ZeOiI2BmJflvyMryO9aurvKaDnBT9If3oIp_6jayZfhc4M7DqAXlKSNWveUkzL2aCZWRswk3x38WHlbcDeUl90oCzD8qWr6n_VsQ5jcvM6MkDHk5HJZw2Uw0XUs1tkKIIxCthcMIZ5SbmfdwDwaR5TseJSPFs_RpnwkxbfqwvR_aoWmEu7vSIXpQJl_RBflwffd9XDaXhMWFJPuJh2raxyH8WBV5RKP30g-Qw9NdX-hbPXx1MsFM6faxoSQuWkxUtzBlX3Yr-gEYOTC3vRHUe4HO98PFgGXSAJ2MhQKqxuEJdpxsudJHcilrXPiM-BHY8wmU922CHSiTcs3vbW0Q; acw_tc=2760826b16604955115287703ebf64fd6d72d1f4a4de24323f89833600efb5; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1660325446,1660362897,1660495512,1660495528; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660495537',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
                },
                {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
                    'Cookie':'__utma=1.1344804606.1616770344.1621000413.1621002956.5; device_id=ed257993933a55e01f20a879a7cc945a; s=db11inxq16; cookiesu=521660230281229; bid=788a6f04f2f6a9185ca8ae0131b3474e_l6ues1tm; acw_tc=2760827316605489839753389eaeb897f1a9ff496117d0f75b5387c60362a8; Hm_lvt_1db88642e346389874251b5a1eded6e3=1659712550,1660230282,1660546926,1660548987; xq_a_token=f9eb7174d5e3af7557ba53738e1a90a9ac71b9a4; xqat=f9eb7174d5e3af7557ba53738e1a90a9ac71b9a4; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjc1MDUzODQ1NTAsImlzcyI6InVjIiwiZXhwIjoxNjYzMTQxMjEzLCJjdG0iOjE2NjA1NDkyMTMwNjIsImNpZCI6ImQ5ZDBuNEFadXAifQ.g1FO--PspXjmLeeUPV12D_Y4OOLQMbJvVJUNv7xWOt0nFCsU2-WM9iAWEATC25HIwpepjvg-bLiDYiwemW0X3rAWgO3LPDcwGfK8fjZuhQ_u9geaN6gV6nbWO_80rYlcIT6givgv26WqLCZZLDcLsuP53pB3UghMxwbd1agvoXSiDi-07HcYo94eAf1OvJ1hds21d2pVrk7VmrvoLlX_MuN6hSAs6PKAG9fc0sJJVoXV6yI2eSeTDVOJPHhpY4MghueF67v_WLKsO3avZ2AxKRxPC235Xv0IecF0P0YX3CWkbGwV9lC4iyNPNNHA_2ThXopq_F-TEiqSz9nUEj3X7A; xq_r_token=097a0aa62c3ce488eb5a05ab849b29016f3f097b; xq_is_login=1; u=7505384550; is_overseas=0; snbim_minify=true; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660549283'
                }


            ]

            param = {
                'cube_symbol':ZuHe_name,
            }

            response=requests.get(url=url,params=param,headers=random.choice(headers)).json()#发起get请求
            time.sleep(0.4)

            zuhe_data=[]
            for i in range(0,len(response[0]['list'])):

                zuhe_data.append([response[0]['list'][i]['date'],response[0]['list'][i]['value'],response[0]['list'][i]['percent']])


            fp = open('%s.csv'%(ZuHe_name),'w',encoding='utf_8_sig',newline="")
            headr_list=['date','netValue','earnRate']
            csvwriter=csv.writer(fp)
            csvwriter.writerow(headr_list)
            csvwriter.writerows(zuhe_data)
            sucess=1
            #print("%s get value finish"%(ZuHe_name))
        except :
            print("进入休眠")
            time.sleep(5.1)
            print("休眠结束")

