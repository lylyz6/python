player_list = ["Piggice", "Tomoe", "Bochi the osu", "Slay_conceit", "Eveliya", "NaimuTongzi", "iz6"]
for player in player_list:
    print(f"{player} is pretty good. ")                   #用循环结构遍历列表
for i in range(1, 5):                                     #用range函数打印1， 2， 3， 4，在i = 5 时终止循环停止打印
    print(i)
for i in range(5):
    print(i)                                              #等同于（0， 5）
Number = list(range(2, 20, 3))                            #用range和list生成数表，2是起始数，20为终止数，3为每次递增的大小
print(Number) 
print(min(Number),max(Number),sum(Number))                #数表中的最小值，最大值，总和
square = [i ** 2 for i in range(2, 50, 7)]                #列表推导式，在range（2， 50， 7）的所有取值的平方进行列表
print(square)
print(player_list[0:2])                                   #对列表切片，保留编号0到编号2前一个（编号1）
print(player_list[:3])                                    #保留编号3之前的列表
print(player_list[3:])                                    #保留从编号3及之后的列表
for t0_player in player_list[:2]:                         #遍历切片
    print(f"{t0_player} is t0")
player_list2 = player_list[:]                             #将切片复制为新列表，没有[:]会将两个列表变量相关联

t0_players = ("Piggice", "Tomoe")       #元组，不可修改的列表
print(t0_players[0])                    
for player in t0_players:
    print(player)                       #读取，遍历方法同列表
lists = [0, 1, 1, 2, 2, 2, 3]
print(set(lists))                       #剔除重复值形成集合