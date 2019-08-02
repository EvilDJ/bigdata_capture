import csv
import datetime
import os
import pandas as pd

def _time(sta,end):
    sta = datetime.datetime.strptime(sta,r"%H:%M:%S")
    end = datetime.datetime.strptime(end,r"%H:%M:%S")
    diff_sec = (end - sta).seconds
    m, s = divmod(diff_sec, 60)
    h, m = divmod(m, 60)
    return m

def add_time(sta, mm):
    h,m,s = sta.strip().split(':')
    sta_sec = int(h)*3600+int(m)*60+int(s)
    end_sec = sta_sec + mm
    m, s = divmod(end_sec, 60)
    h, m = divmod(m, 60)
    return ('%02d:%02d:%02d'%(h,m,s))

rare = []
all_cvs = {}
result = {}
csv_dir = r'.\train_csv'
#---------针对01文件-------------
start = '00:00:00'
for l in range(0,11):
    end = add_time(start, 600)
    result[start + '-' + end] = '1'
    start = end
#-------------------------------
cvs_ = pd.read_csv('record_2019-01-01.csv')
ha, li = cvs_.shape
cvs_data = csv.reader(open('record_2019-01-01.csv','r'))
start_time = '02:00:00'
j ,m = 0, 1
for row in cvs_data:
    if row[0] == 'time':
        continue
    use_time = _time(start_time, row[0][11:])
    if use_time < 10:
        rare.append(row)
    if use_time>=10 or m == ha:
        duli = {}
        num = 1
        # ll = 1
        for i in rare:
            # print(ll,i)
            # ll += 1
            station = {}
            if i[2] in duli:
                if i[-3] == '0':
                    if 'ou' in duli[i[2]]:
                        duli[i[2]]['ou'] += 1
                    if 'ou' not in duli[i[2]]:
                        duli[i[2]]['ou'] = num
                if i[-3] == '1':
                    if 'in' in duli[i[2]]:
                        duli[i[2]]['in'] += 1
                    if 'in' not in duli[i[2]]:
                        duli[i[2]]['in'] = num
            if i[2] not in duli:
                if i[-3] == '0':
                    station['ou'] = num
                if i[-3] == '1':
                    station['in'] = num
                duli[i[2]] = station
            # print('\033[31m'+str(duli)+'\033[0m')# "\033[41;36m something here \033[0m" 上色
        # print(j,'\033[35m'+rare[0][0][11:] + '-' + rare[-1][0][11:], str(duli)+'\033[0m')
        # print(j, '\033[35m' + start_time + '-' + add_time(start_time,600) + str(duli) + '\033[0m')
        result[start_time + '-' + add_time(start_time,600)] = duli
        j += 1
        start_time = add_time(start_time, 600)
        rare = []
        rare.append(row)
    m += 1
all_cvs[1] = result

for dir_a, dir_n, file_n in os.walk(csv_dir):
    n = 2
    for i in file_n:
        res = {}
        rare = []
        _csv_read = dir_a + '/' + i
        print(_csv_read)
        cvs_ = pd.read_csv(_csv_read)
        ha, li = cvs_.shape
        cvs_data = csv.reader(open(_csv_read, 'r'))
        start_time = '00:00:00'
        j, m = 0, 1
        for row in cvs_data:
            if row[0] == 'time':
                continue
            use_time = _time(start_time, row[0][11:])
            if use_time < 10:
                rare.append(row)
            if use_time >= 10 or m == ha:
                duli = {}
                num = 1
                # ll = 1
                for i in rare:
                    # print(ll,i)
                    # ll += 1
                    station = {}
                    if i[2] in duli:
                        if i[-3] == '0':
                            if 'ou' in duli[i[2]]:
                                duli[i[2]]['ou'] += 1
                            if 'ou' not in duli[i[2]]:
                                duli[i[2]]['ou'] = num
                        if i[-3] == '1':
                            if 'in' in duli[i[2]]:
                                duli[i[2]]['in'] += 1
                            if 'in' not in duli[i[2]]:
                                duli[i[2]]['in'] = num
                    if i[2] not in duli:
                        if i[-3] == '0':
                            station['ou'] = num
                        if i[-3] == '1':
                            station['in'] = num
                        duli[i[2]] = station
                    # print('\033[31m'+str(duli)+'\033[0m')# "\033[41;36m something here \033[0m" 上色
                # print(j,'\033[35m'+rare[0][0][11:] + '-' + rare[-1][0][11:], str(duli)+'\033[0m')
                # print(j, '\033[35m' + start_time + '-' + add_time(start_time,600) + str(duli) + '\033[0m')
                res[start_time + '-' + add_time(start_time, 600)] = duli
                j += 1
                start_time = add_time(start_time, 600)
                rare = []
                rare.append(row)
            m += 1
        all_cvs[n] = res
        n +=1

for i in all_cvs:
    print(i)