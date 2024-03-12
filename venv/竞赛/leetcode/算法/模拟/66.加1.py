# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/16 10:04'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = digits
        for i in range(len(digits) - 1, -1, -1):
            temp = ans[i] + carry
            if temp >= 10:
                carry = temp // 10
                ans[i] = temp % 10
                if i == 0:  # 处理最高位进位情况
                    ans.insert(0, carry)
            else:
                ans[i] = temp  # 剪枝,若无进位说明可以结束了
                break
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
