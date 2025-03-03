import requests
import pandas as pd
from lxml import html

url = 'https://weibo.com/ajax/side/hotSearch'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
    
def get_url():
    target = requests.get(url = url,headers={'User-Agent':UA})
    if target.status_code != 200:
        return None
    return target.json()['data']

# 获取热搜对象

label_list = ['爆','热','商','新','']
label_emoji = ['💥','🔥','🛒','🆕','']

def get_data(cnt):
    data = get_url()
    if data is None:
        print("request Failed.")
    # print(data)
    print(f"On_top:🔥{data['hotgov']['word'].strip('#')}")
    # 遍历 realtime 列表下前 cnt 条信息
    for i,text in enumerate(data['realtime'][:cnt],1):
        search_title = text['word']
        try:
            search_label = text['label_name']
            if search_label in label_list:
                search_label = label_emoji[label_list.index(search_label)]
            else:
                search_label = ''
        except:
            search_label = ''
        print(f"{i}.{search_label}{search_title} ")



if __name__ == '__main__':
    get_data(10)