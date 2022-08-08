import requests
import csv
url='https://xueqiu.com/cubes/nav_daily/all.json'
headers = {
    'Cookie':'Hm_lvt_1db88642e346389874251b5a1eded6e3=1659623909,1659627901,1659710821,1659857427; device_id=37775ef18cf8cc43dfb743be1f6164f0; s=dh16ckpaj6; bid=788a6f04f2f6a9185ca8ae0131b3474e_l63r39o3; xq_a_token=0af02fc9be0f5a31761f6d596076469a20ecbc11; xqat=0af02fc9be0f5a31761f6d596076469a20ecbc11; xq_r_token=075a9236d16ad248c9452a8c40a0480c54932a57; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjgxMzc5MDE5ODAsImlzcyI6InVjIiwiZXhwIjoxNjYxNTI3MDMwLCJjdG0iOjE2NTk0NTQ3Njc3NzksImNpZCI6ImQ5ZDBuNEFadXAifQ.fYf-ad47BctsbyTtEH9aA6Pzf2nLbnVU9rOpXnOPsu-t6-fn9XsT5aqAnorP6klFzMLBR1DHetdpMxOhN1UXbc3VtLLRCTfzdfuJPNcvty-ockLAEcveKZ4CXvaQwa6Ks1JUluYDwBL2DY0SODslKxbdhH2n5ANRW9JW6E5ScyijOdJDElaag97jQd-mqkliPJtqgDvTBhDEV4Af_uaSscMh8QBZ79-kJDnrqky3_NzfHJwJ__56rlll6btcymqRv3Ju9CfbKKxL48VOHoHp35rpVCqaZ-SO22wQORaTGbq0q3lk_UK0uPG-qcGpj0Oef_GFkG8V52e0qNO2q8o2lQ; u=8137901980; remember=1; xq_is_login=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1659860986; acw_tc=2760828016598592288446187e785fbb33e667cf8e6e7ac5cff02a21732d45; is_overseas=0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}

param = {
    'cube_symbol':'ZH2119969',
}
response=requests.get(url=url,params=param,headers=headers).json()#发起get请求
print(response[0]['list'][0]['date'])
zuhe_data=[]
for i in range(0,len(response[0]['list'])):

    zuhe_data.append([response[0]['list'][i]['date'],response[0]['list'][i]['value'],response[0]['list'][i]['percent']])


fp = open('zuhe_data2.csv','w',encoding='utf_8_sig',newline="")
csvwriter=csv.writer(fp)
csvwriter.writerows(zuhe_data)
print("finish")