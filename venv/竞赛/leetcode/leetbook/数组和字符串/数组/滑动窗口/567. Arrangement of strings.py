# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/27 19:40'

import time


class Solution:
    # 方法一:偷懒滑动窗口,哈希表统计
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import collections
        len_1 = len(s1)
        len_2 = len(s2)
        if len_1 > len_2:
            return False
        else:
            target = collections.Counter(s1)
            for i in range(len_2 - len_1 + 1):
                temp = collections.Counter(s2[i:i + len_1])
                if temp == target:
                    return True
            return False

    # 真滑动窗口
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        m1 = len(s1)
        m2 = len(s2)
        if m1 > m2:
            return False
        dic1 = [0] * 26
        dic2 = [0] * 26
        for i in range(m1):
            dic1[ord(s1[i]) - ord('a')] += 1
            dic2[ord(s2[i]) - ord('a')] += 1
        if dic1 == dic2:
            return True

        for i in range(m1, m2):
            dic2[ord(s2[i - m1]) - ord('a')] -= 1
            dic2[ord(s2[i]) - ord('a')] += 1
            if dic1 == dic2:
                return True
        return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
