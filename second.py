# 爬取梨视频的
import requests
import re
import uuid
import os

index_url = 'https://www.pearvideo.com'

headers = {
    'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/65.0.3325.146 Safari/53736'

}

# 定义函数,
def get_page(url):
      # 往url中发送get 请求
    res = requests.get(url, headers=headers)
# print(res,text)
# 返回响应文本
    return res.text

def parse_index(text):
    # 通过正则模块解析所有视频的标签中的相对路径
    a_s = re.findall('<a href="(.*)?" class ="actwapslide-link"', text)
    detail_urls = []
    # 通过循环所有相对路径,拼接视频详情也url
    for line in a_s:
        # 往详情列表追加视频详情页面url
        url = index_url + line
        detail_url.append(url)
    #     返回详情页面列表
    return detail_urls

def parse_detail(text):
    video_urls = re.findall('srcUrl="(.*?)"', text)[0]

    return video_urls


# 保存视频的函数

def save_video(video_url):
    # 往视频链接地址
    res = requests.get(video_url)
    #
    #
    if not os.path.exists("videos"):
        os.mkdir("videos")
    with open(r'videos/%s.mp4' % uuid.uuid4(), 'wb') as f:
        f.write(res.content)

if __name__ == ' __main__ ':
    base_url = 'https://www.pearvideo.com'
    index_page = get_page(index_url)

    detail_urls = parse_index(index_page)

    print(detail_urls)

    for detail_url in detail_urls:
        detail_page = get_page(detail_url)

        video_url = parse_detail(detail_page)

        save_video(video_url)