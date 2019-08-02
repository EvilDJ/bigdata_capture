import pandas as pd
import re

def xiu(s):
    cop = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")#用正则化标定指定字符
    s = cop.sub(';', s)#切换所有字符成';'
    _list = list(s)#删除重复出现的';'成单一的';'
    list1 = []
    for i in range(len(_list) - 1):
       if _list[i] != _list[i+1]:
           list1.append(_list[i])
    list1.append(_list[-1])
    s = ''.join(list1)#将list形式转成字符串形式
    return s


qu = []
data = pd.read_csv('./data/0.csv')#读取csv文件并转换成list格式。
for line in data.values:
    qu.append(str(line[3]))#提取csv的第4列数据，及参考答案列
    # f.write((str(line[1])+'\n'))
print(len(qu))
qu = sorted(set(qu), key= qu.index)#整合第四列数据

#将第四列，参考答案列数据 转成txt文件
q = 0
with open('./data/00.txt', 'a+', encoding='utf-8') as f:
    for i in qu:
        f.write(str(q)+','+i+'\n')
        q += 1

#将出现相同参考答案的问题，归为一个txt文档下
#将同一个类问题放一起进行关键词提取，针对参考答案。
j = 0
t = 0
for i in qu:
    path = './data/0/' +  str(j) + '.txt'
    with open(path, 'a+', encoding="utf-8") as f:
        # f.write((str(i) + '\n' + '\n'))
        for line in data.values:
            if i == str(line[3]):
                ll = xiu(line[1])
                print(t, ll)
                f.write((str(ll) + '\n'))
            else:continue
            t += 1
    j += 1
print(t)