# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 16:51'

import time


class UndergroundSystem:
    # 方法一:模拟+哈希表
    def __init__(self):
        self.startInfo = dict()
        self.table = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startInfo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime = self.startInfo[id][1]
        index = (self.startInfo[id][0], stationName)
        rec = self.table.get(index, (0, 0))
        self.table[index] = (rec[0] + t - startTime, rec[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        index = (startStation, endStation)
        sum, amount = self.table[index]
        return sum / amount


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
