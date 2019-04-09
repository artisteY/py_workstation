import json

import requests

from wxpy import *
bot = Bot(cache_path=True)
# groups = bot.groups
groups = bot.groups().search('泰州学院')[0] #指定群发送消息
name = groups.search('徐鹏')[0]   #给指定群的人发消息
# print('all weChat Groups', groups)

# friend = bot.search('老韩')[0]#给特定的好友发送消息

def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "e71db6a90fce492eaf1ed23df44c67f7"
    # text = "你好哇"
    playload = {
        "key": api_key,
        "info": text
    }

    r = requests.post(url, data=json.dumps(playload))
    result = json.loads(r.content)
    return "...."+result['text']
    # return "[来自机器人]" + result['text']

# @bot.register(chats=friend)
# # @bot.register(chats=groups)#设置群的消息
# def get_msg(recv_msg):
#     # if recv_msg.member == name:
#     if recv_msg.sender == friend:
#
#         text = recv_msg.text
#
#         # result = auto_reply(text)
#         result = auto_reply(text)
#
#         print('图灵返回的内容：', result)
#         msg ='[智障机器人：%s]' % result
#         # msg = '[图灵机器人测试（请忽略）：%s]' % result
#
#         return msg
# embed()
@bot.register(chats=groups)
def forward_message(msg):
    # if msg.sender == 'name':
        return auto_reply(msg.text)

# @bot.register()
def get_msg(recv_msg):

    text = recv_msg.text

    result = auto_reply(text)
    print('图灵返回的内容：', result)

    msg = '[图灵机器人测试（请忽略）：%s]' % result

    return msg
embed()