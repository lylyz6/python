print("每天都爱你:\n\tPiggice\n\tTomoe\n\tBochi the osu\n\tSlay_conceit\n\tEveliya\n\tNaimuTongzi\n\tiz6")#制表符\t 换行符\n
name = " iz6 "
a = "I am"
b = "is me"
print(f"{a}{name}")
print(f"{a}{name.lstrip()}")#删左空白
print(f"{name}{b}")
print(f"{name.rstrip()}{b}")#删右空白
print(f"{a}{name.strip()}, {name.strip()}{b}")#删除两端空白
URL = "http://www.baidu.com"
print(URL.removeprefix("http://www."))#删除前缀
file = "学习资料.txt"
print(file.removesuffix(".txt"))#删除后缀