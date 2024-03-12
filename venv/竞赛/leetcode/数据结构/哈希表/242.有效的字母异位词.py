# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 21:10'

import time


class Solution:
    # 方法一:哈希表统计出现次数
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        if collections.Counter(s) == collections.Counter(t):
            return True
        else:
            return False


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
