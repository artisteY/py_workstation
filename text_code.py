# from selenium import webdriver
#
# import time
#
#
# driver = webdriver.Chrome()
#
# driver.get('https://www.baidu.com/')
#
# time.sleep(4)
#
# driver.close()
# n = int(input("put your number:"))
# n = 2*n - 1
# for i in range((int(input(""))*2-1)):
#
#     print(i)
'''

打印奇数 2n - 1
和打印偶数 2n

'''
n = int(input("input your number:"))

print(str(n)+'中的奇数是：')


for i in range(1, n):

    if i % 2 == 1:
        l = [i]
        print(l)
print(str(n) + '中的偶数是：')
for i in range(1, n):

    if i % 2 == 0:
        j = i
        l = [j for j in range(j)]
        # l = [i for i in range(1,n)]
        print(l)

print('*'*200)
def d():

    list = [i for i in range(100)]

    print(list)

d()
        # print('*'*i)

    # elif i == 5:
    #     for i in range(1, 2*n - 1):
    #
    #         if i % 2 == 1:
    #             print('*'*i)
    # # else:
    #
    #     for i in range(1, 2*n - 1):
    #
    #         if i % 2 == 1:
    #             print('*'*i)




     # if i % 2 == 0:
    #
    #      print()
    #     # print('偶数是：'+str(i))# 当有str类型和数字类型一起输出时会报错，此时可以把int 强制转换成str
    #
    # else:
    #
    #     print('*'*i)

# n = 2*n - 1
#
# for i in range(1, n):
#
#     if i % 2 == 0:
#         print()
#
#     else:
#         print('*'*i)