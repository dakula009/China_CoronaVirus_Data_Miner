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

# 创建空 dataframes
col_names =  ['省', '市', '新增确认','确认' , '死亡', '治愈']
col_names_p =  ['省','确认', '新增确认',  '死亡', '治愈']

my_df  = pd.DataFrame(columns = col_names)
my_df_p = pd.DataFrame(columns = col_names_p)

for item in areaTree:
    if item['name'] == '中国':
        item_ps = item['children']

        # 遍历省级数据
        for item_p in item_ps:
            province = item_p['name']
            # print(province)
            # print(item_p['total'])
            confirm = item_p['total']['confirm']
            death = item_p['total']['dead']
            heal = item_p['total']['heal']
            new_confirm = item_p['today']['confirm']

            # 向df添加数据
            data_dict = {'省': province,'新增确认':new_confirm,'确认': confirm, '死亡': death, '治愈': heal}
            my_df_p.loc[len(my_df_p)] = data_dict

            # 遍历地级数据
            item_cs = item_p['children']
            for item_c in item_cs:
                prefecture = item_c['name']
                # print('  ' + prefecture)
                # print('  ' + str(item_c['total']))
                new_confirm = item_c['today']['confirm']
                confirm = item_c['total']['confirm']
                # suspect = item_c['total']['suspect']
                death = item_c['total']['dead']
                heal = item_c['total']['heal']

                # 向df添加数据
                data_dict = {'省': province, '市':prefecture, '新增确认':new_confirm,'确认': confirm, '死亡': death, '治愈': heal}
                my_df.loc[len(my_df)] = data_dict

# 保存数据
my_df.index += 1   # 使index从1开始
my_df_p.index += 1
my_df.to_csv(r'./china_prefecture_status_{}.csv'.format(str(lastUpdateTime).split()[0]), encoding='utf_8_sig', header='true')
my_df_p.to_csv(r'./china_province_status_{}.csv'.format(str(lastUpdateTime).split()[0]), encoding='utf_8_sig', header='true')

print('Success')