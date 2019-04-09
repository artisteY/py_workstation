from wxpy import Bot

from pyecharts import Pie

import webbrowser

bot = Bot()

friends = bot.friends()

attr = ['男性朋友', '女性朋友', '未知性别']

value = [0, 0, 0]
# 遍历i所有的好友添加到value
for friend in friends:

    if friend.sex == 1:

        value[0] += 1

    elif friend.sex == 2:

        value[1] += 1

    else:

        value[2] += 1
# 生成一个pie对象
pie = Pie('好友性别饼图')
# 把好友数据添加到pie 对象中去
pie.add('', attr, value, is_label_show=True)
# 生成一个好友饼图
pie.render('friends.html')
#
webbrowser.open('friends.html')
