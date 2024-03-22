import random as r
print(r.random())                  #生成[0,1)随机数
print(r.randint(1,3))              #生成[a,b]随机整数
print(r.uniform(2,3))              #生成[a,b]随机小数
player_list = ["Piggice", "Tomoe", "Bochi the osu", "Slay_conceit", "Eveliya", "NaimuTongzi", "iz6"]
print(r.choice(player_list))              #从序列类型随机返回一个元素
r.shuffle(player_list)                    #打乱序列
print(player_list)
print(r.sample(player_list,3))            #从列表随机返回n个值形成列表

import time as t
print(t.time())                           #返回当前时间戳
t.sleep(3)                                #让程序暂停n秒        