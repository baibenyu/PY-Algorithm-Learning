# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/31 19:26'

import time
from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    # 方法一:哈希表
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        a = bisect_right(self.dct[key], [timestamp, "z"*101])
        if a-1 == len(self.dct[key]) or a == 0:
            return ""
        return (self.dct[key])[a-1][1]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
