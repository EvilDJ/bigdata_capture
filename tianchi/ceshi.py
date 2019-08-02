import numpy as np
import datetime
import pandas as pd
import os

csv_dir = r'G:\网络数据集\PEOPLE\Metro_train\Metro_train'
duli = {'37in': 1, '15in': 1, '57in': 5, '37ou': 1, '41in': 1, '77in': 1, '37':0}
# du = []
# for i in duli:
#     if i[:2] not in du:
#         du.append(i[:2])
# du_np = np.ones([len(du),3])
# for i in duli:
#     if i[:2] not in du_np:
#         du_np
# if '15' in duli:
#     print(duli['15'])

# def _time(sta,end):
#     sta = datetime.datetime.strptime(sta,r"%H:%M:%S")
#     end = datetime.datetime.strptime(end,r"%H:%M:%S")
#     diff_sec = (end - sta).seconds
#     print(diff_sec)
#     m, s = divmod(diff_sec, 60)
#     h, m = divmod(m, 60)
#     return h,m,s
# print(_time('00:00:00','00:10:00'))

# mod = [datetime.datetime.strptime(x,r"%H:%M:%S") for x in time[1:]]

# max_time = max(mod)
# min_time = min(mod)
# diff_day = (max_time - min_time).days
# diff_sec = (max_time - min_time).seconds
# m, s = divmod(diff_sec, 60)
# h, m = divmod(m, 60)
#
# print("%d days,%02d hours,%02d minites,%02d seconds" %(diff_day,h, m, s))

# def add_time(sta, mm):
#     h,m,s = sta.strip().split(':')
#     sta_sec = int(h)*3600+int(m)*60+int(s)
#     end_sec = sta_sec + mm
#     m, s = divmod(end_sec, 60)
#     h, m = divmod(m, 60)
#     return ('%02d:%02d:%02d'%(h,m,s))
# print(add_time("00:00:00", 600))

# for dir_a, dir_n, file_n in os.walk(csv_dir):
#     # print(dir_a + '/' + file_n[(num[u])])
#     print(dir_a)
#     # print(file_n)
#     for i in file_n:
#         print(dir_a + '/' + i)

if '37' in duli:
    print(duli['37'])

# for i in duli:
#     print(i)