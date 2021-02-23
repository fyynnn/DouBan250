# -*- coding = utf-8 -*-
# @Time :  9:44
# @Author : fyn
# @File : t1.py
# @Software: PyCharm


import urllib.request
# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com") # 对获取的网页源码进行utf-8解码
# print(response.read().decode('utf-8'))

# 获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Server"))


# # 测试
# url = "https://httpbin.org/get"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
# }
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="GET")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
}
req = urllib.request.Request(url=url, headers=headers, method="GET")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))