team = {}                 #创建空字典
team = {"t0": "Piggice", "t1": "Tomoe", "t2": "Bochi the osu", "t3": "Slayconceit", 
        "t4": "NaimuTongzi", "t5": "Eveliya"}
print(team)                                            #字典，键与值一一对应
print(team["t0"])                                      #输入键打印值
team["t6"] = "iz5"                 #添加键值对
print(team)
team["t6"] = "iz6"                 #修改键值对
del team["t5"]                     #删除键值对  
print(team.get("t7", "no such person"))   #输入键打印值，没有则返回后面的语句
for t, id in team.items():         #使用for循环和items()函数遍历字典键值对
    print(f"{t}:{id}")
for t in team.keys():
    print(t)                       #遍历键，keys()返回的是列表，可用sorted()排序
for id in sorted(team.values()):
    print(id)                      #遍历值排序后打印
tomoe = {"Tomoe": "t1"}
iz6 = {"iz6": "t6"}
team_members = [tomoe, iz6]          #字典列表
print(team_members)
team = {"每天都爱你": team_members}   #字典中存储列表
print(team)
t1info = {"over_6k": tomoe}           #字典中存储字典
print(t1info)

