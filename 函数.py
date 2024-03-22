def greet(name):                                    #定义函数
    print(f"hello, {name}")
greet("sansx")
def greet_(name, time="moring"):                  #定义多个形参，并设置默认值
    print(f"good {time}, {name}.")
greet_("sansx")
greet_("sansx", "evening")
def info(id, uid):                                  #让函数返回值
    information = f"{id}: {uid}"
    return information
print(info("iz6", "26093361"))
def player_list(matchname,*name):                            #用*传递任意数量实参形成元组
    print(f"{matchname}: {name}")
player_list("yhc s2","sansx", "iz6", "tomoe")
from 第8章作业 import make_shirt as ms           #从模块中引入函数并重命名
ms("small")
import 第8章作业 as p8                           #引入模块并重命名
p8.describe_city("Guangzhou")
from 第8章作业 import *                          #从模块引入所有函数