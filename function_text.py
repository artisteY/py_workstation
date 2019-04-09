#嵌套循环while 循环的使用

import time
def while_recyle():
    tag = True
    while tag:

        print('111')
        time.sleep(1)
        while tag:

            print('2222')
            time.sleep(13)  #设置时间间隔
            break


# while_recyle()
# for 循环，循环遍历列表
def for_recyle():

    list1 = [1, 3, 5, 6]

    for line in list1:

        print(line)

    for line in range(10): # 数值从0开始，顾头不顾尾

        print(line)

    for line in range(5, 1):
        print(line)


# for_recyle()

#对文件的处理

def use_file():
#     写一个文件
    f = open('file.txt', 'w', encoding='utf-8')

    f.write('你好骚啊')

    f.close()
# 读取文件
    r = open('file.txt', 'r', encoding='utf-8')
    print(r.read())
    r.close()
# 使用with open 自带一个关闭close的功能

    with open('file2.txt', 'w', encoding='utf-8') as f:

        f.write('《围城》')
        r = open('file2.txt', 'r', encoding='utf-8')

        print(r.read())


# use_file()

'''
函数
1.先定义，后调用
2.无参数
3.有参数
'''
def login():

    name = input('name:')
    pwd = input('pwd:')

    if name == 'user' and pwd == '123':
        print('登陆成功！')


# login()

def sum(x, y):
    print(x + y)


    # return x + y

# sum(1,2)

def func():
    # return 'xiaopang'
    # return 1234
    return 'sadf', '2234', 'china'  #return 可以返回多个值
name, pwd, address = func()
# python中return 语句的多个返回值要一一对应
print(name, pwd, address)

# t1=func()  #此时的t1是一个变量
# print(t1)
# print(type(t1))
print('-'*100)

'''
引子：
执行python的文件的过程：
1.加载python解释器 
2.检测文件内的代码的语法
3.执行程序
名称空间和作用域
1.内置名称空间
        关键字,内置模块
2. 全局名称空间
        python文件内，顶着头写，最左边的。
3.局部名称空间
加载顺序：
内置-->全局-->外层局部-->内层局部
执行顺序：与加载顺序刚好相反

'''
num1 = 100
def Foo():
    num1 = 200
    print(id)

# Foo()
# 3.局部名称空间

num = 1
def func1():
    num = 2
    print(num)

    def func2():
        num = 3
        print(num)


    # func2()

# func1()

'''
闭包函数是函数的名称空间和作用域，嵌套函数，函数地址这三者的一个产物
'''

def outer():

    def inner():
        num = 20
        print(num)
        return num

    return inner  #return 函数地址

inner = outer()
inner()
print('-'*100)

# 开发商城时可以定义的函数
def login():
    login_success = 'login is successful.'
    print(login_success.capitalize())
# 注册
def register():
    pass
# 查看余额
def check_balance():
    pass
# 购物车功能
def shop_cart():
    pass
# 支付功能
def pay_money():
    pass

dict1 = {
    '1': login,
    '2': register,
    '3': check_balance,
    '4': shop_cart,
    '5': pay_money,
}

for key in dict1:
    print(key)

# while True:
#     choice = input('请选择你的功能：').strip()
#
#     if choice in dict1:
#         print('在里面！')
#         print(dict1[choice])
#         dict1[choice]()
#     else:
#         print('你输入错误！')

'''
装饰器
指的是装饰的工具，用来给需要添加新功能的函数添加功能，
不修改被装饰器函数的源代码以及调用方式

'''
print('-'*100)
def timmer(func):

    def inner(*args, **kwargs): #args和kwargs可以调用任意数量的变量
        start_time = time.time()
        func(*args, **kwargs) #被装饰的函数
        print(time.time()-start_time)

    return inner #返回地址

@timmer

def foo(x, y):
    # start_time = time.time() 获取程序开始时间戳
    print(x * y)
    time.sleep(3)
    # end_time = time.time() 结束时间戳
#     print(end_time.time() - start_time.time())

foo(3, 4)
'''
函数在定义阶段不会执行函数体代码，也不会产生名称空间
def foo():

    print('from foo ....')


foo()
类会在定义阶段就会执行，产生名称空间
'''
def kanchi(name, sex, number):

    print('%s 上山,性别%s,砍了%s的柴' % (name, sex, number))

kanchi('artiste', 'male', 20)

