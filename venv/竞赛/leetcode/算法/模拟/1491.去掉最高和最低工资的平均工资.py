# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/22 19:43'

import time
from typing import List


class Solution:
    # 模拟
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
