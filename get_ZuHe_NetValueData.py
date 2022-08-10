import time

import requests
import csv
def get_ZuheNetValue(ZuHe_name):

    url='https://xueqiu.com/cubes/nav_daily/all.json'
    headers = {
        'Cookie':'device_id=6937eed60f66b1afaae2e099ee61d34a; s=c512byykvs; cookiesu=851660138162231; Hm_lvt_1db88642e346389874251b5a1eded6e3=1660138162,1660138315,1660138336,1660138387; remember=1; xq_a_token=0af02fc9be0f5a31761f6d596076469a20ecbc11; xqat=0af02fc9be0f5a31761f6d596076469a20ecbc11; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjgxMzc5MDE5ODAsImlzcyI6InVjIiwiZXhwIjoxNjYxNTI3MDMwLCJjdG0iOjE2NjAxMzgzOTI4NjAsImNpZCI6ImQ5ZDBuNEFadXAifQ.JZOTxJmVRfHj-B_WWCUg3nzfbNYJyzJWnMG77YF4CO7NPKd-hNN_g6RbwuXMDBrJE1w0cDwbcNTpMPBtTruf_HOEbJdbipoTIPYPON1VxkEL8HDkVasAwiPwj6WEFU5RT_YIU4mfzEI9tVW5QoG9W7j16sGsSkxF_l728yoh54pClp7aAGxpMlMytqS5juJinWwM6STuuw7ygJrg-W0lKkln7w_AhhHA56_0PM-4H-qK_KkapjB6QtHXSs_va4BA4D4DEexrXXdDihUgjHAADbsJyK351kgZkqDoFRmFqdD2PHG90YBm9lYb723Lqqde5OeAHly61z-oCe3UeNm0_A; xq_r_token=075a9236d16ad248c9452a8c40a0480c54932a57; xq_is_login=1; u=8137901980; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660138394',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    param = {
        'cube_symbol':ZuHe_name,
    }
    response=requests.get(url=url,params=param,headers=headers).json()#发起get请求
    time.sleep(0.5)

    zuhe_data=[]
    for i in range(0,len(response[0]['list'])):

        zuhe_data.append([response[0]['list'][i]['date'],response[0]['list'][i]['value'],response[0]['list'][i]['percent']])


    fp = open('%s.csv'%(ZuHe_name),'w',encoding='utf_8_sig',newline="")
    headr_list=['date','netValue','earnRate']
    csvwriter=csv.writer(fp)
    csvwriter.writerow(headr_list)
    csvwriter.writerows(zuhe_data)
    print("%s get value finish"%(ZuHe_name))
    return

