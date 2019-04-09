# 用来驱动浏览器
from selenium import webdriver
# 用来破解滑动验证的时候用的，可以拖动图片
from selenium.webdriver import ActionChains
#按照什么方式查找BY，ID，CSS_SELECTOR
from selenium.webdriver.common.by import By
# 键盘操作
from selenium.webdriver.common.keys import Keys
# 等待页面加载某些元素
from selenium.webdriver.support.wait import WebDriverWait

import time

driver = webdriver.Chrome()

try:

    # 等待标签加载
    driver.implicitly_wait(10)
    # 往京东发送get请求
    driver.get('https://www.jd.com/')

    input_tag = driver.find_element_by_id('key')
    input_tag.send_keys('macbook pro')
    # 控制键盘，按回车键
    input_tag.send_keys(Keys.ENTER)

    # 找到所有商品的div，里面包含所有的li

    goods_div = driver.find_element_by_id('J_goodsList')

    # element：找到第一个  elements:找到所有
    items = goods_div.find_element_by_class_name('gl_item')
    # 循环所有li 标签
    for item in items:
# 商品连接
        good_link = item.find_element_by_css_selector('.p-name a').get_attribute('href')

        # print(good_link)
        good_name = item.find_element_by_css_selector('.p-name em').text
        # print(good_name)
        good_price = item.find_element_by_css_selector('.p-price i').text + '$'
        good_commit = item.find_element_by_css_selector('.p-commit a').text + '条评论'

        print(

            '''
            商品链接：%s
            商品名称：%s
            商品价格：%s
            评价人数：%s
            \n
            ''' % (good_link, good_name, good_price, good_commit) )

        text = '''
            商品链接：%s
            商品名称：%s
            商品价格：%s
            评价人数：%s
            \n
            ''' % (good_link, good_name, good_price, good_commit)

        with open('jd.txt', 'a', encoding='utf-8') as f:

            f.write(text)

    time.sleep(14)

finally:
    driver.close()