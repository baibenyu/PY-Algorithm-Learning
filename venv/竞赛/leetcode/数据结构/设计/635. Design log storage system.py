# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 15:54'
import collections
import time
from typing import List


class LogSystem:
    # 方法一:直接进行字符串比较即可,根据精度决定取几位进行比较
    def __init__(self):
        self.log_dict = collections.defaultdict(str)
        # 如果对比的是年份，只需要timestamp的前4位，其他同理
        self.granularity_dict = {"Year": 4, "Month": 7, "Day": 10,
                                 "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id: int, timestamp: str) -> None:
        self.log_dict[id] = timestamp

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        check_len = self.granularity_dict.get(granularity)
        res = []
        for key, val in self.log_dict.items():
            if start[:check_len] <= val[:check_len] <= end[:check_len]:
                res.append(key)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
