# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/12 9:34'

import time


class Solution:
    # 方法一:双射--两哈希表确定唯一映射
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            else:
                if dict1[s[i]] != t[i]:
                    return False
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
            else:
                if dict2[t[i]] != s[i]:
                    return False

        return True


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
