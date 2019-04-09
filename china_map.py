# 城市地域分布图
from pyecharts import Map

import webbrowser

map = Map('城市地域分布图', width=1200, height=600)
# attr 列表里存放各个城市的人数
attr = ['上海', '甘肃', '浙江', '江苏']

# 各个城市对应的各个城市的人数

value = [456, 5789, 5678, 3457]

# 往map对象添加各个城市的名称以及人数,设置国家
map.add('城市分布图', attr, value, maptype="china", is_visualmap=True, visual_text_color='#000')


# 生成城市页面

map.render('cities.html')

# 打开成市页面
webbrowser.open('cities.html')