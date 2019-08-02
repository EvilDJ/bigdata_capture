import os
# {25天：{144时间段：{个站台：{'0':25,'1':36}}}}
# 站台：  出[天，段] / 进[天，段]
_dir = r'F:\pycharm_代码\tianchi\result'
def read_dit(_dit):
    for num in range(0,80):
        for day in _dit:  # 25天
            mer_day_0 = []
            mer_day_1 = []
            for time in _dir[day]:  # 一天中的144时间段
                mer_time_0 = []
                mer_time_0.append(time)
                mer_time_1 = []
                mer_time_1.append(time)
                if str(num) in _dir[day][time]:
                    mer_time_0.append(_dir[day][time][str(num)]['0'])# 本站台下出去人数
                    mer_day_0.append(mer_time_0)
                    mer_time_1.append(_dir[day][time][str(num)]['1'])# 本站台下进去人数
                    mer_day_1.append(mer_time_1)
                else:
                    mer_time_0.append(0)
                    mer_time_1.append(0)
                    mer_day_1.append(mer_time_1)
                    mer_day_0.append(mer_time_0)