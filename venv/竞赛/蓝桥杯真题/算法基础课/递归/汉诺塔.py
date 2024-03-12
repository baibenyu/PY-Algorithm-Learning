# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/15 20:12'

import time

start = time.clock()


# 分解问题,将n-1层移到辅助位置,将第n层移到终点位置,再将n-1层移到终点位置
def hannuota(n, start, end, pas):
    if n == 1:
        print("move" + str(n) + "from" + start + "to" + end)
    else:
        hannuota(n - 1, start, pas, end)
        print("move" + str(n) + "from" + start + "to" + end)
        hannuota(n - 1, pas, end, start)


hannuota(3, "A", "B", "C")
end = time.clock()
print(end - start)
