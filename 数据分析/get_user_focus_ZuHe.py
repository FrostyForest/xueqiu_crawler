import requests
def get_user_focus_ZuHe(user_id):
    session=requests.session()
    headers = {
            'Cookie': '__utma=1.1344804606.1616770344.1621000413.1621002956.5; device_id=ed257993933a55e01f20a879a7cc945a; xq_a_token=bf75ab4bcea18c79de253cb841f2b27e248d8948; xqat=bf75ab4bcea18c79de253cb841f2b27e248d8948; xq_r_token=c7d30dc738a77dd909a8228f3053679e86bf104b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2MTgxNjI0MSwiY3RtIjoxNjU5NzEyNTE0ODg4LCJjaWQiOiJkOWQwbjRBWnVwIn0.ZqNVrli8Qdh2Uc9zJGApN7EKmZP4XCbQX64cPVfPu9oN1mG5BXxWOjkpEkFG4iVKYiHaX9TZrdRYrC2ta6MezyOE4gxq1dAyDhR5y5vVe1xoND0eJETOYx9w3um9SrboA5WVJjaM2988Z_vDwYYK9jIUDhWx0F9mGrZgx5gJug9IXrtszKwQ9EY6mWlST0oI3feaVsI7jk1Gj5BZTTjPDGaK2huFeT4b0E_QGf4p9CsSoGdnPcX-f9QGC_0RXnE2_g2CBOCd_xIhQQQ1S5lWG8n4Zth7pNw3CKp1pKO1NfWT8TD0Gv4wHEBC7TwqScWlqe7awDIvvGCHN8kCWVfTBA; u=231659712550633; Hm_lvt_1db88642e346389874251b5a1eded6e3=1659244628,1659247220,1659712550; s=db11inxq16; acw_tc=276077ae16597204266158605e906274bd98f161954c2ec77fb31d8dd268bf; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1659722028',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
        }
    param = {

            "size": "1000",
            "category": "3",
            "uid": user_id,
            "pid": "-120"

    }
    url='https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json'
    response=requests.get(url,params=param,headers=headers).json()
    user_focus_zuhe_list=[]
    for i in range(0,len(response['data']['stocks'])):
        x=[response['data']['stocks'][i]['symbol'],response['data']['stocks'][i]['name']]#0为组合代码，1为组合名字
        user_focus_zuhe_list.append(x)
    return user_focus_zuhe_list

