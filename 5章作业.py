#5.3 to 5.5
score = 0
alien_color = "yellow"
if alien_color == "green":
    score = score + 5
    print("恭喜你猜对了，获得5分")
score = 0
if alien_color == "green":
    print("恭喜你获得5分")
else:
    print("恭喜你获得10分")
if alien_color == "green":
    print("恭喜你获得5分")
elif alien_color == "yellow":
    print("恭喜你获得10分")
elif alien_color == "red":
    print("恭喜你获得15分")

#5.6
age = 20
if age < 2:
    print("this person is a infant")
elif age >= 2 and age < 4:
    print("this person is a toddle")
elif age >= 4 and age < 13:
    print("this person is a child")
elif age >= 13 and age < 18:
    print("this person is an adolescent")
elif age >= 18 and age < 65:
    print("this person is an adult")
elif age >= 65:
    print("this person is an old")

#5.7
favorite_fruits = ["apple", "orange", "banana"]
fruits = ["apple", "orange", "watermelon", "banana", "appear"]
for fruit in fruits:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")

#5.8 & 5.9
id_list = ["iz6", "admin", "amagiri yune", "sansx", "yzyxwx"]
if id_list:
    for id in id_list:
        if id == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {id}, thank you for logging in again")
else:
    print("We need to find some users!")

#5.10
current_users = ["iz6", "Kusuhara", "Amagiri Yune", "SansX", "yzyxwx"]
current_users_lower = []
for i in range(len(current_users)):
    current_users_lower.append(current_users[i].lower())
new_users = ["iz6", "Bochi the osu", "yzyxwx", "Slay_conceit", "Eveliya"]
for id in new_users:
    if id.lower() in current_users_lower:
        print(f"{id} has been used, please change your id")
    else:
        print(f"{id} is available!")

#5.11
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in number:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")

#6.1
iz6 = {"username": "iz6", "uid": 26093361, "coutry": "China", "pp": 6783 }
print(iz6.get("username"), iz6.get("uid"), iz6.get("coutry"), iz6.get("pp"))

#6.2
people = ["I", "you", "he", "she", "they"]
number = [1, 2, 3, 4, 5]
people_number = {}
for i in range(5):
    people_number[people[i]] = number[i]
    print(f"Hi, {people[i]}.Do you like number {number[i]}? ")
print(people_number)

#6.3 & 6.4
dictionary = {}
noun = ["list", "tuple", "dict", "set", "str"]
explaination = ["内置类型，可变（或不可哈希），其中可以包含任意类型的数据，支持使用下标和切片访问其中的某个或某些元素，常用方法有append()、insert()、remove()、pop()、sort()、reverse()、count()、index()，支持运算符+、+=、*、*=。可以使用[]直接定义列表，也可以使用list()把其他类型的可迭代对象转换为列表，列表推导式也可以用来创建列表，若干标准库函数、内置类型方法以及扩展库函数或方法也会返回列表。列表不能作为字典的“键”，也不能作为集合的元素", 
                "内置类型，不可变（或可哈希），其中可以包含任意类型的数据，如果元组中只有一个元素，必须加一个逗号，例如(3,)。元组支持使用下标和切片访问其中的某个或某些元素，支持运算符+、*。可以使用()直接定义元组，也可以使用tuple()把其他可迭代对象转换为元组，若干标准库函数、内置类型方法以及扩展库方法或方法也会返回元组。元组可以作为字典的“键”或者集合的元素，但是如果元组中包含列表、字典、集合或其他可变对象，就不能作为字典的“键”和集合的元素了。", 
                "内置类型，常用于表示特定的映射关系或对应关系，可变（不可哈希），元素形式为“键:值”，其中“键”必须是可哈希类型的数据且不重复。如果创建字典时指定的“键”有重复，只保留最后一个，例如执行语句x = {'a': 96, 'b': 98, 'c': 99, 'a': 97}后x的值为{'a': 97, 'b': 98, 'c': 99}。", 
                "内置类型，可变（不可哈希），其中每个元素都必须可哈希且不会重复。", 
                "内置类型，可哈希（不可变），可以是空字符串或包含任意多个任意字符的对象，使用单引号、双引号、三单引号、三双引号作为定界符，不同定界符之间可以嵌套。在字符串前面加字母r或R表示原始字符串，加字母f或F表示对其中的占位符进行格式化，可以在一个字符串前面同时加字母r和f（不区分大小写）。"]
for i in range(5):
    dictionary[noun[i]] = explaination[i]
for noun, explaination in sorted(dictionary.items()):
    print(f"{noun}:{explaination}")

#6.5
Rivers_Country = {
    "Yangtzi": "China", 
    "lyin": "Germany", 
    "Nile": "Egypt"}
for river, country in Rivers_Country.items():
    print(f"The {river} runs through {country}.")
for river in Rivers_Country.keys():
    print(river)
for country in Rivers_Country.values():
    print(country)

#6.7
sansx = {"username": "SansX", "uid": 29735986, "coutry": "Mauritius", "pp": 6607}
yzyxwx = {"username": "yxyzwx", "uid": 31851527, "coutry": "China", "pp": 5004 }
players = [iz6, sansx, yzyxwx]
for player in players:
    print(player)

#7.1
car = input("what car do you want to rent: ")
print(f"Let me see if I can find you a {car}.")

#7.2
quatity = int(input("How many guest would have dinner: "))
if quatity > 8:
    print("There is no free desk.")
elif quatity <= 8:
    print("There is free desk.")
else:
    print("What do you mean?")

#7.3
num = int(input("Please input a number, I will test if it can be divided fully by 10: "))
if num % 10 == 0:
    print(f"{num} can be divided fully by 10")
else:
    print(f"{num} can not be divided fully by 10.")

#7.8
dishes = ["egg", "meat", "milk", "rice"]
finished_dished = []
while dishes:
    for dish in dishes:
        print(f"I made your {dish}")
        finished_dished.append(dish)
        dishes.remove(dish)
print(finished_dished)

#7.9
vestigating = True
vestigate_results = {}
while vestigating:
    name = input("what's your name? ")
    vestigate_results[name] = input("where do you want to have a vacation? ")
    whether_go = input("do you want to continue vestigating?(yes/no) ")
    if whether_go == "no":
        vestigating = False
    elif whether_go == "yes":
        continue
print(f"the result of vestigation is {vestigate_results}")
