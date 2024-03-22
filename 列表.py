player_list = ["Piggice", "Bochi the osu", "Slay_conceit", "Eveliya", "NaimuTongz", "SansX"]
print(player_list[0])           #列表0代表第一个
print(player_list[-1])          #列表-1代表倒数第一个
player_list[4] = "NaimuTongzi"    #修改某元素
player_list.append("iz6")       #最后面添加
player_list.insert(2,"Tomoe")   #选择位置添加，后面的向后移动一位
del player_list[-1]             #选择位置删除，后面的向前移动一位
poped_player = player_list.pop(-1)#删除某位置元素并将这个元素单独列出来
removing_player = "NaimuTongzi"
player_list.remove(removing_player) #删除指定元素
print(player_list,poped_player)
player_list.sort()                  #按首字母顺序排序
print(player_list)
player_list.sort(reverse = True)    #按首字母倒序排列
print(player_list)
sorted_list = sorted(player_list)   #创建一个新列表为原列表的首字母顺序排序
print(player_list)
print(sorted_list)
player_list.reverse()               #把原列表顺序倒转
print(player_list)
print(len(player_list))             #确定列表长度