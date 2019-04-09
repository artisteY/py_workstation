# 
from wxpy import Bot

from wxpy import *
# 导入所有的wxpy里面的
import time
bot = Bot()
# groups = bot.groups()
# print('所有的微信群：', groups)
# friend_group = bot.groups().search('正经群')[0]
# name = friend_group.search('周静根')[0]
# @bot.register(chats='正经群')
#
# def recv_send_msg3(recv_msg):
#
#     print('收到的消息：', recv_msg.text)
#     if recv_msg.member == name:
#         recv_msg.forward(bot.file_helper, prefix='有人留言：')
#
#         ms = '沙雕'
#
#         return ms
# #
# company_group = bot.group().search('群名字')[0]
#
# boss = company_group.search('老板名字')[0]
#
# @bot.register(chat=company_group)
#
# def recv_send_msg2(recv_msg):
#     print('收到的消息：', recv_msg.text)
#
#     if recv_msg.member == boss:
# #         这里不用recv_msg.render 因为reader是群的名字
#             recv_msg.forward(bot.file_helper, prefix = '老板发言：')
# #             return '老板说的好有道理，深受启发'
# # 无限循环给微信助手发送消息
# while True:
#     # 获取微信助手，在微信助手发送消息
#     bot.file_helper.send('hello')
#     time.sleep(3)
# # for line in friend:
#     print(line)
friend = bot.search('颖')[0]
friend1 = bot.search('迷雾')[0]
friend2 = bot.search('夕阳下的过客')[0]
print(friend, friend1, friend2)
@bot.register()
#获得最新的消息
def recv_send_msg(recv_msg):
    print('收到消息：', recv_msg.text) #recv_msg.text取得文本


    if recv_msg.sender == friend:

        recv_msg.forward(bot.file_helper, prefix='留言：')
    #     在文件传输助手里留一份

    # return '自动回复:%s'%recv_msg
        ms = '有人给你留言'
        print('>>>留言：', ms)
        return ms
    elif recv_msg.sender == friend1:

        ms = '帅哥，你好'
        print('>>>留言：', ms)
        return ms
    elif recv_msg.sender == friend2:
        ms = '沙雕'

        print('>>>留言：', ms)

        return ms
# 进入python命令行，让程序持续运行
embed()
