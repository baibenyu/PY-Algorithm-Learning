# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/7 15:37'

import time
from math import comb
from typing import List


class Solution:
    # 方法一:递推
    # 只需前一行即可推出,所以直接覆盖即可
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex + 1):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(ans[j] + ans[j - 1])
            ans = temp
        return ans

    # 方法二:数学
    # 杨辉三角每个数刚好是C(n,i)的组合系数
    def getRow1(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
