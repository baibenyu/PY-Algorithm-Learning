# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/28 14:49'

import time


class Solution:
    # 方法一:计数,找到不为0的字符
    def findTheDifference(self, s: str, t: str) -> str:
        import collections
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        temp = tc - sc
        for key in temp:
            if temp[key] != 0:
                return key

    # 方法二:求和,对ascii码求和相减即为目标字符的ascii码
    def findTheDifference2(self, s: str, t: str) -> str:
        sum1, sum2 = 0, 0
        for each in s:
            sum1 += ord(each)
        for each in t:
            sum2 += ord(each)
        return chr(sum2 - sum1)


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
