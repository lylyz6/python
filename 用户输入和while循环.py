message = input("I will reply what you write")      #让用户输入文本并返回
print(message)       
number = float(input("输入一个小于10的整数: "))
print(f"大于{int(number)}小于10的奇数有:")
while number < 10:                                 #满足右侧条件则循环
    number += 1                                
    if number - int(number) != 0:
        print("请输入整数!")
        break                                       #break终止并退出循环
    if number % 2 == 0:
        continue                                    #continue提前结束当前循环并进入下一个循环
    print(int(number))
will_player_list = ["Piggice", "Tomoe", "Bochi the osu", "Slay_conceit", "Eveliya", "NaimuTongzi", "iz6"]
player_list = []
while will_player_list:                            #使用while移动列表
    player = will_player_list.pop()
    player_list.append(player)
    print(f"verifyed player: {player}, verifyed players: {player_list}")
while "iz6" in player_list:                        #删除特定元素
    player_list.remove("iz6")
print(player_list)