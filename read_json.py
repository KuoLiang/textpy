# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:46:04 2021

@author: klout
"""
import json
from pprint import pprint
with open('data/ibike.json') as file:
    data = file.read()

jdata = json.loads(data)

pprint(jdata)

d = jdata['retVal'].values()

# 由北到南印出所有的車站，位置，緯度
station=[]
for st in d:
    # 站名，位址，緯度
    name, addr, lat = st['sna'], st['ar'], st['lat']
    item = (name, addr, lat)
    station.append(item)

pprint(station)    

# 排序
station.sort(key=lambda x: x[2], reverse=True)    
pprint(station)
with open('data/ibikeSorted.txt', 'w') as f:
    for i in station:
        f.write(str(i)+'\n')

# 每個區域 iBike station 的數量
area = {} # {area_name: count}
for st in d:
    ar = st['sareaen'] # area name
    if ar in list(area.keys()):
        area[ar] = area[ar] + 1
    else:
        area[ar] = 1
pprint(area)        

sortedArea = sorted(area.items(), key=lambda d: d[1])
pprint(sortedArea)    