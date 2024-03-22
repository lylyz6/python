from pathlib import Path                    
path = Path("abc.txt")                    #使用Path函数寻找文本文件使用
contents = path.read_text()               #使用read_text读取文本文件
print(contents)                       
lines = contents.splitlines()             #将几行字符串的每行切割组成列表
print(lines)  
text = ""
for line in lines:
    text += line
print(text)
writing = "abcdefg\nhijklmn\nopqrst\nuvwxyz\nnow I can say abc "
path.write_text(writing)                  #写入文本
def division(y):
    answer = 10 / int(y)
    return answer
try:                                                                      #try-except处理异常
    a = division(input("input a number that 10 will be divided by it: "))
except ZeroDivisionError:        
    print("you can't divide number with zero!")
else:
    print(a)