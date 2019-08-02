from bs4 import BeautifulSoup
import requests
import urllib.request
page = requests.get('https://www.d6080.com/list/1/3.html')#访问网站
bs = BeautifulSoup(page.content,"lxml")#打印出网站
image = bs.find_all('img')#寻找目标位置
# print(image)
data = {}
j = 1
for i in image:
    print(j,':',i.get('src'))#目标位置也是以字典形式保存目标网络，拜访并访问目标网络
    pic_file = open('./images/pic'+str(j)+'.jpg','wb')
    pic_file.write(requests.get(i.get('src')).content)

    # 0urllib.request.urlretrieve(i.get('src'), './images/%s.jpg' % j)
#     data[str(j)] = i.find('a').get('href')
    j+=1
# print(data)
# for i in image:
#     title = i.h2
#     link = i.a
#     print('------',link)
# print(bs.find_all('a'))