# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/16 9:13'

import time


class Solution:
    # 方法一:KMP算法
    # 可以用该算法是基于s in 2*s(去头去尾),就表明s是由重复子串构成的这条理论
    # 那么问题就转为在2s中找s,若找到则说明存在
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)

    # 方法二:枚举
    # 因为该字符串由子串重复构成,说明从第一个字符就需要满足该条件,所以子串必然包含从开头至当前的所有字符,又因为多次重复,说明只需到原长度一半就可以停止
    def repeatedSubstringPattern2(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length // 2 + 1):
            if s[:i] * (length // i) == s:
                return True
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
