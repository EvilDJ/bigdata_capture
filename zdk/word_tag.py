#导入需要的模块
import os
import codecs
import pandas
import jieba
import jieba.analyse
#搭建语料库，同类问题放到一起，进行关键词提取，用此关键词和参考答案建立直观链接。
tag = []
j = 0
for dirs ,root ,files in os.walk('./data/0/'):
    for name in files:
        filePath = dirs + '\\' + name
        f = codecs.open(filePath, 'r', encoding="utf-8")
        content = f.read().strip()
        f.close()  # 读取文件内容
        # print(content)
        tags = jieba.analyse.extract_tags(content, topK=8)  # 获取每篇文本词频在前五的关键词
        print(j,':',tags)
        tag.append(tags)
        j += 1

q = 0
with open('./data/tag.txt', 'a+', encoding='utf-8') as f:
    for i in tag:
        f.write(str(q)+','+str(i)+'\n')
        q += 1
