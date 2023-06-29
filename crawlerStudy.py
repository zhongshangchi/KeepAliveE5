"""
1. 提取到每一个电影背后的url地址
2. 访问子页面提取到电影的名称以及下载地址
"""
import requests
import re

url = "https://www.dy2018.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"
}
resp = requests.get(url,headers=headers)
resp.encoding = "gbk"

# 1.提取2021必看热片部分的html代码
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<li>.*?)</ul>",re.S)
result1 = obj1.search(resp.text)
lis = result1.group("li")
#提取href
obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title")
result2 = obj2.finditer(lis)

obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名　(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
for item in result2:
    child_url = url.rstrip("/") + item.group("href")
    # print(child_url)
    cresp = requests.get(child_url,headers=headers)
    cresp.encoding = "gbk"

    result3 = obj3.search(cresp.text)
    print(result3.group("download"))

