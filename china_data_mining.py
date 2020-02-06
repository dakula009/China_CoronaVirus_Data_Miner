# —*— coding: utf-8 —*—
import requests
import json
import time
import pandas as pd

# 请求的URL
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'

# 伪装请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'referer': 'https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0'
}

# 抓取数据
r = requests.get(url % time.time(), headers=headers)

data = json.loads(r.text)
data = json.loads(data['data'])

lastUpdateTime = data['lastUpdateTime']
print('数据更新时间 ' + str(lastUpdateTime))

areaTree = data['areaTree']

# 创建空 dataframe
col_names =  ['省', '市', '确认' , '疑似', '死亡', '治愈']
my_df  = pd.DataFrame(columns = col_names)

for item in areaTree:
    if item['name'] == '中国':
        item_ps = item['children']
        for item_p in item_ps:
            province = item_p['name']
            # print(province)
            item_cs = item_p['children']
            for item_c in item_cs:
                prefecture = item_c['name']
                # print('  ' + prefecture)
                # print('  ' + str(item_c['total']))
                confirm = item_c['total']['confirm']
                suspect = item_c['total']['suspect']
                death = item_c['total']['dead']
                heal = item_c['total']['heal']

                # 向df添加数据
                data_dict = {'省': province, '市':prefecture, '确认': confirm, '疑似': suspect, '死亡': death, '治愈': heal}
                my_df.loc[len(my_df)] = data_dict

# 保存数据
my_df.to_csv(r'./china_status_{}.csv'.format(str(lastUpdateTime).split()[0]), encoding='utf_8_sig', header='true')

print('Success')