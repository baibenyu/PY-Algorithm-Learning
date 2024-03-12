# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/31 20:12'

import time
from typing import List


class Solution:
    # 方法一:位运算--异或
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num

        lsb = xorsum & (-xorsum)  # 取出两个剩余数异或后的最低位1,保证两个数&该最低位1的结果不同
        type1 = type2 = 0
        for num in nums:  # 遍历原数组,相同的数&这个最低位1会被归到一组,即有两个的数都会被分到同一组,唯有只有一个的数分到不同组
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num

        return [type1, type2]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
