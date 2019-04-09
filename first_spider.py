# 向百度发送请求,并保存到本地
import requests
base_url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent':'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/65.0.3325.146 Safari/53736'


}


response = requests.get(base_url,headers=headers, params={"wd":"美女"})
# 响应状态码
print(response.status_code)
#响应文本
print(response.text)

with open ("baidu.html",'w',encoding='utf_8') as f:
    f.write(response.text)
