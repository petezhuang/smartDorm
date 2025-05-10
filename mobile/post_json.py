import requests
import json
url = 'https://www.u2601175.nyat.app:15108/api/get_data_from_raspi'
headers = {'Content-Type': 'application/json'}

def post_json():
    # 准备JSON数据
    with open('data.json') as f:
        data = json.load(f)

    try:
        x=requests.post(url, json=data, headers=headers, verify=False)
        #print(x.status_code)
    except Exception as e:
        #print(e)
        pass