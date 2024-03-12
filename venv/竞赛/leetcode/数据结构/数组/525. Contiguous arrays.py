# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/7 20:32'

import time
from typing import List


class Solution:
    # 方法一:前缀和+哈希表
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        hashmap = {0: -1}
        # 当前1的数量和0的数量的差值
        counter = ans = 0
        for i, num in enumerate(nums):
            # 每多一个1，差值+1
            if num:
                counter += 1
            # 每多一个0，差值-1
            else:
                counter -= 1
            # 如果存在1和0的数量差值相等的地方，那么说明后者到前者之前1和0的数量相等！
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
