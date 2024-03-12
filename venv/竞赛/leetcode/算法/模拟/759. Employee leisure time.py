# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/6/1 15:08'

import time

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # 扫描线 sweep line == 差分+关键点
        WORK = 0  # 为了排序的时候，同一个位置，先work，后free
        FREE = 1

        rec = []
        for sche in schedule:
            for inter in sche:
                s = inter.start
                e = inter.end
                rec.append((s, WORK))
                rec.append((e, FREE))

        rec.sort()
        res = []
        pre = -1
        cur_worker = 0
        for t, op in rec:
            if cur_worker == 0 and pre != -1:
                res.append(Interval(pre, t))
            if op == WORK:
                cur_worker += 1
            if op == FREE:
                cur_worker -= 1
            pre = t
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
