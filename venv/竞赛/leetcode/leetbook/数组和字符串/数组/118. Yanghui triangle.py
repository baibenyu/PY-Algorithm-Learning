# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 15:30'

import time
from typing import List


class Solution:
    # 方法一:数学
    # 每一行的数除开头和末尾为1,其它数都等于上一行相同下标和下标-1的和
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(ans[i - 1][j] + ans[i - 1][j - 1])
            ans.append(temp)
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
