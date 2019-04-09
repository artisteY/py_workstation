'''
理解面象对象的编程技巧
在现实世界中： 先有对象，然后经过人类文明的演变成为类.

在程序中先定义类，然后在创造对象

面向对象的三大基础： 继承，封装，多态


# 类会在定义阶段就会执行，产生名称空间


__init__是一个内置的方法，在特定的条件下才会触发
 在调用类时才会触发
'''
class People:

    print('hello python!')

    def __init__(self, name, age, sex, time_use):

        # print(self,name,age,sex)
        self.name = name
        self.age = age
        self.sex = sex
        self.time_use = time_use
    def learn(self):
            # self.time = time
        print('%s是个%s的%s,每天认真学到%s点' % (
            self.name,
            self.age,
            self.sex,
            self.time_use))

# 调用类的过程称为实例化，得到的man称为一个实例化的一个对象或一个实例
# man = People('artiste', 18, 'male')
# 调用类的过程会将对象当作第一个参数自动传给__init__
# print(man.name, man.age, man.sex)
# People.learn('from PP')
# man.learn() #对象来调用类里面的方法就会把对象作为第一个参数自动传给learn
p3 = People('lechat', 16, 'male', 3)
p3.learn()
print('-'*200)
'''
调用类时会发生的事情：
1.创造一个空对象。
2.会自动触发类内部的__init__函数
3.会自动把对象作为第一个参数传入
'''
class P:
    # 对象共有的属性
    school = 'taizhou'
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def learn(self, time):
        self.time = time
        print('student learning!')

p1 = P('artiste', 16, 'male')

p1.learn('13hours')
# p2 = P()
# print(p2.school)
print('*'*200)
'''
python 中一切都是对象
'''

class Foo:
    pass

f = Foo()

print(type(f))
name1 = 'artiste'
name2 = str('artiste')
age1 = 11
age2 = int(18)
print(type(age1))

print(type([1, 2]))
'''
人狗大战
'''
class Persion:
    def __init__(self, name, aggr, life=100):
        self.name = name
        self.aggr = aggr
        self.life = life

    def bite(self, blood):
        blood.life -= self.aggr
        print('人类："%s"咬了狗"%s",狗还剩余血量为"%s"' % (
            self.name,
            blood.name,
            blood.life
        ))

class Dog:
    def __init__(self, name, aggr, life=200):
        self.name = name
        self.aggr = aggr
        self.life = life
    def bite(self, blood):
        blood.life -= self.life
        print('狗："%s"咬了人类"%s",人还剩余血量为"%s"' % (
            self.name,
            blood.name,
            blood.life
        ))

persion1 =Persion('小胖', 50,3000 )

dog1 = Dog('肥仔', 200, 3500)
persion1.bite(dog1)
dog1.bite(persion1)
print('*'*150)
'''
类：是一系列对象共有的特征与技能的结合体
对象：是特征与技能的结合体
封装
把属性装进对象内，封起来！指的是对内部公开，对外部隐藏
通过__属性，把属性隐藏起来，内部发生变形“__类名__属性”
封装的意义在于把属性隐藏起来，防止外部对内部的属性进行修改，保证数据安全
而且把以对属性封装到对象里，对象就相当于一个容器，需要使用里面的属性时就从容器里直接拿出来使用
'''
class Foo2:
    __number = 100
    # print(__number)
    def __jisuan(self):
        print(self.__number**6)

    def get_number(self):
        return  self.__number

f1 = Foo2()
# print(f1.__number)
# print(self._Foo2__number)
print(f1.get_number())
'''
什么是继承？
继承指的是一种新建的方式，子类可以继承父类的属性，并且可以派生出自己特有的属性。
python中一个子类可以继承多个父类，父类也可以称之为超类和基类
子类（父类）：括号里面写继承的父类
抽象：
抽象类与类相似的部分，抽取他们比较象的特征与技能。
继承最重要的用处是：减少代码的冗余
'''
class Father1:
    pass
class Father2:
    # pass
    name = 'artiste'
class Son1(Father1):
    pass
class Son2(Father2):
    pass
class Son3(Father1, Father2):
    pass

# 查看子类的父类：__bases__
son3 = Son3()

print(son3.name)
print(Son1.__bases__)
print(Son2.__bases__)
print(Son3.__bases__)

print('_'*100)

class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def drink(self):

        print(('drinking water!').capitalize())

    def eat(self):

        print(('eating food.').capitalize())

class Cat(Animal):
    # pass
    print(('this is a sub extend father!').upper())
class Dog(Animal):
    # pass
    print(('this is another sub extend father!').upper())


cat = Cat('小猫', 12, 'female')
cat.drink()
cat.eat()
dog = Dog('小狗', 11, 'male')
dog.drink()
dog.eat()

print('$'*150)

