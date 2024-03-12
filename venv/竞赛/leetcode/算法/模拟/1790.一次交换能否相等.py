# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/24 21:15'

import time


class Solution:
    # 方法一:模拟
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        import collections
        cur1 = collections.Counter(s1)
        cur2 = collections.Counter(s2)
        if cur1 != cur2:  # 首先要字母种类和数目相同才行,即为同一字母序列的不同排列
            return False
        else:
            p1, p2 = 0, 0
            count = 0
            while p1 < len(s1):  # 不同的地方大于2处就不能
                if s1[p1] != s2[p2]:
                    count += 1
                p1 += 1
                p2 += 1
            if count <= 2:
                return True
            else:
                return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
