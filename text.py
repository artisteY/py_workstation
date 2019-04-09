# -*-coding:utf-8 -*-
# str类型转化
i = '34'
i = int(i)
print(type(i))
print(i.bit_length()) # bit_length将数学转换为二进制，并且最少返回二进制的位数
# float类型
j = 332.43
# j = str(j)
print(type(j))
#  bool类型的结果返回值
# None,bool(''),bool([]),bool(0),bool({}),bool(())
# 字符串的操作
# 索引，切片，长度，遍历，删除，分割，清除空白，大小写转换，判断开头
k = 'hahaa2345hahAAAAAhahahahaha'
print(k)
print(k[5]) #从0 开始数
print(k[0:-2]) #切片操作
print(k.index("a", 4))
print(k.find("h", 3)) #获取索引,这里的index和find一样的
print(k.find("c", 1)) #若索引的值不在此字符串里面，find 返回-1,报错
# print(k.index("c", 2))
print(len(k)) #len()同样可以用于其他的数据了类型，比如元组，列表，字典
#   del k 删除语句，
# isalnum(),isalpha()判断是否全为字母,isdigit()
print(k.isdigit()) #判断是否全为数字
# 大小写转化
print(k.capitalize()) #首字母大写
print(k.upper())  #全部大写
print(k.lower())  #全部小写
print(k.title())  #转变为题目
print(k.casefold()) #全部转换为小写
print(k.swapcase()) #大小写互相转换
# 判断以什么开头和结尾，返回值为bool类型
print(k.endswith('4'))
print(k.startswith('h'))
info ="name\tage\temail\nlittlefive\t22\t994263539@qq.com\njames\t33\t66622334@qq.com"
print(info.expandtabs(10))
# 格式化输出的方式： format() ,format_map()
# 第一种方法
info1 = "my name is {name},I'm {age} years old."
print(info1.format(name='xiaofei', age=21))
# 第三种方法看看就行了
# print(info1.format(**{"name": "xiaofei", "age": 33}))
# 第二种方法
info2 = "my name is {0},I'm {1} years old. "
print(info2.format("xiaopang", 13))
info3 = "my name is {name},I'm {age} years old."
print(info3.format_map({"name": "xiaoming", "age": 16}))
# join方法的的使用，将字符串， 元组，列表中的元素以指定的分符（）连接生成的一个新的字符串
print("*".join(info1))
print(type(k))
# 元组
tuple = (34, 42, 1)
print(type(tuple))

list = {1, 2, 34, 5, 6}

print(type(list))

dic = {'name': 'tom', 'age': 18, 'address': 'beijing',
       'name': 'tim', 'age': 19, 'address': 'tianji',
       }
# print(dic.expandtabs())
# 字典类型的数据不能扩展用expandtabs() 表格化输出
print(type(dic))
# 列表中join的使用
l = [1, 2, 3, 4545]
l1 = ["wwee", "ssddd", "ss"]
print("--".join(l1))
print(type(l))