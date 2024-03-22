a = 1
print(a == 1)          #检查是否相等，返回True 或False
print(a != 1)          #检查是否不等
print(a >= 1)          
print(a >= 1 and a < 0, a >= 1 or a < 0)  #判断时可使用and和or
player_list = ["Piggice", "Bochi the osu", "Slay_conceit", "Eveliya", "NaimuTongz", "SansX"]
print("iz6" in player_list)      #用in检查元素是否在列表中
if a == 1:
    print("正确")                 #if后语句返回True则执行缩进后的代码
if a > 1:
    print("a > 1")
elif a < 1:
    print("a < 1")
else:
    print("a = 1")           #使用if-elif-else当if后语句为False测试elif后条件，若仍为False则运行else后代码，可使用多次elif
if player_list:              #检查列表是否非空，空集则返回False，if语句不执行
    print("player_list 非空")
else:
    print("player_list 为空集")
t0_player = ["Tomoe", "Piggice", "Stick_Fish"]
for player in t0_player:
    if player in player_list:
        print(f"{player} is t0 in our team")                #for和if语句同时使用检查两个列表
