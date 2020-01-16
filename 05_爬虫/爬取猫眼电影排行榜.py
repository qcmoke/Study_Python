# 导入我们需要的模块
import re
import requests

# 一、获取网页内容
# （1）声明目标url，就是爬取的网站地址
base_url = "http://maoyan.com/board"

# （2）模仿浏览器
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

# （3）发起请求
response = requests.get(base_url, headers=headers)

# （4）接收响应的数据
html = response.text

# （5）将接收的数据写入
with open("maoyan.html", 'w', encoding='utf-8') as f:
    f.write(html)

# 2.提取数据
# （1）缩小范围（通过正则获取数据）
pattern = re.compile(r'<dd>.*?</dd>',re.S)
movie_list = pattern.findall(html)

# (2) 分别拿取每部电影中的数据
for movie in movie_list:
    # print(movie)
    # 获取排名信息
    pattern = re.compile(r'<i class="board-index board-index-[\d]*">(\d{1,2})</i>')
    index = pattern.findall(movie)[0]
    index = '排名：' + index
    print(index)

    # 获取电影名称信息
    pattern = re.compile(r'title="(.*?)"')
    title = pattern.findall(movie)[0]
    title = '电影名称：' + title
    print(title)

    # 获取图片信息
    pattern = re.compile(r'<img data-src="(.*?)@')
    img = pattern.findall(movie)[0]
    img = '图片：' + img
    print(img)

    # 获取主演信息
    pattern = re.compile(r'<p class="star">([\w\W]*?)</p>')
    star = pattern.findall(movie)[0].strip()
    print(star)

    # 获取上映时间信息
    pattern = re.compile(r'<p class="releasetime">(.*?)</p>')
    releaseTime = pattern.findall(movie)[0]
    print(releaseTime)

    # 获取评分信息
    pattern = re.compile(r'<p class="score"><i class="integer">(\d+\.)</i><i class="fraction">(\d)</i></p> ')
    score = pattern.findall(movie)
    score = '评分：' + score[0][0]+score[0][1]
    print(score)

    # 将所有信息拼接成字符串
    result = index + '\n' + title + '\n' + img + '\n' + star + '\n' + releaseTime + '\n' + score + '\n\n'

    # 将所有信息存入文档
    with open("maoyan.txt", 'a+', encoding='utf-8') as f:
        f.write(result)