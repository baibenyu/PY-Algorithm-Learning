# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/15 11:14'

import time


class Solution:
    # 方法一:单调栈+贪心--优先移除高位的数字
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
