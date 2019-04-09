'''
# 好友地域分布
from wxpy import Bot
from pyecharts import Map
import webbrowser
bot = Bot()
friends = Bot.friends()

attr = []
value = []
dict = []

for friend in friends:

    if friends.provice not in dict:
        dict[friend.provice] = 1
    else::
        dict[friend.provice] += 1
for i in dict:
    dict.append(i)
    value.append(dict[i])

map = Map('frends_map')

map.add('friends map', attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
map.render('friend.html')
webbrowser.open('friend.html')



'''

# 好友性别分布

'''
from wxpy import Bot
from pyecharts import Pie
import webbrowser

bot = Bot()
friends = bot.friends()

attr = ['male', 'female', 'not in']
value = [0, 0, 0]
for friend in friends:
    if friend.sex == 1:
        value[0] += 1
    elif friend.sex == 2:
        value[1] += 1
    else:
        value[2] += 1


pie = Pie('friends sex pie')
pie.add('', attr, value, is_label_show=True)
pie.render('friends_pie.html')
webbrowser.open('friends_pie.html')

'''

# 给指定好友发消息
'''
from wxpy import *

bot = Bot()

friends = bot.search('老韩')[0]

print(friends)

@bot.register(chats=friends)


def recv_send_msg(recv_msg):
    print('收到消息', recv_msg.text)

    if recv_msg.sender :== friends:
        recv_msg.forward(bot.file_helper, prefix='留言')
        # 留言到微信助手里面
        ms = '行吧'
        print('>>>留言：', ms)
        return ms

embed()

'''
'''
# 给指定群的指定好友发消息
from wxpy import *

bot = Bot()

groups = bot.groups().search('泰州学院')[0]
name = groups.search('韩梓琦')[0]
print(groups, name)
@bot.register(chats=groups)
def recv_send_msg(recv_msg):
    print('收到消息', recv_msg.text)

    if recv_msg.member == name:

        ms = '你好！'
        print('>>>留言：')
        return ms

embed()


'''

'''
# 给所有好友发消息

from wxpy import *

bot = Bot()

friends = bot.friends()
# print(str(friends))
for friend in friends:
    print(str(friend))

    @bot.register(chats=friend)

    def recv_send_msg(recv_msg):

        # if recv_msg.sender == friend:

            print('消息：', recv_msg.text)

            ms = '往后收收吧，小弟弟'

            print('>>>留言：')
            return ms


embed()
'''
# 图灵机器人测试
import json

import requests

from wxpy import *
bot = Bot()
friends = bot.search()
# groups = bot.groups().search('正经群')[0] #指定群发送消息
# name = groups.search('老韩')[0]   #给指定群的人发消息
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "d48264313e7b4d4fbf34eb21e54b21af"
    # text = "你好哇"
    playload = {
        "key": api_key,
        "info": text
    }

    r = requests.post(url, data=json.dumps(playload))
    result = json.loads(r.content)
    print(result)
    return "...."+result['text']

# @bot.register(chats=groups)#设置群的消息
for friend in friends:
    print(friend)
    @bot.register(chats=friend)
    def get_msg(recv_msg):
        # if recv_msg.sender == friends:

            text = recv_msg.text

            # result = auto_reply(text)
            result = auto_reply(text)

            print('图灵返回的内容：', result)
            msg ='[智障机器人：%s]' % result


            # msg = '[图灵机器人测试（请忽略）：%s]' % result

            return msg
embed()
