from wxpy import Bot
from pyecharts import Map
import webbrowser

bot = Bot()
friends = bot.friends()
attr = []
value = []
dict1 = {}
for friend in friends:

    if friend.province not in dict1:

        dict1[friend.province] = 1

    else:

        dict1[friend.province] += 1

for i in dict1:

    attr.append(i)

    value.append(dict1[i])

map = Map('好友地域分布图')

map.add('地域分布', attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')

map.render('friendsMap.html')

webbrowser.open('friendsMap.html')
