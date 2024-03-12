# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/30 8:53'

import time
from typing import List


class Solution:
    # 方法一:动态规划
    # 将结果拆成v[i]+i和v[j]-j
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = values[1] + values[0] - 1
        temp = values[0]
        for i in range(1, len(values)):
            ans = max(ans, temp + values[i] - i)
            temp = max(temp, values[i] + i)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
