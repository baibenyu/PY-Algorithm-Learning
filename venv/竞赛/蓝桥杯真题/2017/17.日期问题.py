# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/18 10:10'

import time
import calendar

start = time.clock()

date, res = input().split('/'), []
for u, v, w in [[0, 1, 2], [2, 0, 1], [2, 1, 0]]:  # y/m/d
    for ex in ['19', '20']:
        temp = int(ex + date[u])
        if 1959 < temp < 2060:
            try:
                calendar.weekday(temp, int(date[v]), int(date[w]))  # 利用try和weekday来判断日期是否合法,规避自己判断是否是润年,是否是2月,每个月有几天等问题
                res.append(f"{temp}-{date[v]}-{date[w]}")
            except ValueError:
                pass
res = list(set(res))
res.sort(key = lambda date_: (date_[:4], date_[4:6], date_[6:]))
print(*res, sep = '\n')

end = time.clock()
print(end - start)
