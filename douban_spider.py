import requests
import re
# import workbook
headers = {

    'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/65.0.3325.146 Safari/53736'

}
# 爬虫三步曲
# 第一步：发送请求
def get_page(url):

    response = requests.get(url,headers=headers)

    print(response.text)

    return  response.text
# 2.解析数据
def parse_page(text):

    list1 = []
#     提取电影连接
    movie_url = re.findall('<div class="item">.*?<a href="(.*?)"', text, re.S)
#     电影名称
    name = re.findall('<div class="item">.*?<span class="title">(.*?)</span>', text, re.S)

#     电影评分
    point = re.findall('<div class="item">.*?<span class = "rating_num".*?>(.*?)</span>', text, re.S)
#     电影评价人数
    number = re.findall('<div class="item">.*?<span>(.*?人评价)</span>', text, re.S)

    # python可以返回多个值，返回到一个数据中
    return movie_url, name, point, number

# 保存数据

def save_data(data):

    with open('douban.txt', 'a', encoding="utf-8") as f:

        f.write('\n' + data)

if __name__ == '__main__':

    base_url = 'https://movie.douban.com/top250?start=%s&filter='

    number = 0
    for line in range(10):

        url = base_url % number

        print(url)
        # 往url地址发送请求
        number += 25

        ret = get_page(url)
        # 解析ret 响应文本
        data = parse_page(ret)
        save_data(str(data))

    # wb = workbook()
    # ws = wb.worksheets[0]
    #
    # for line in result:
    #     line = [movie_url, name, point, number]
    #
    #     ws.append(line)
    # wb.save('douban.xlsx')