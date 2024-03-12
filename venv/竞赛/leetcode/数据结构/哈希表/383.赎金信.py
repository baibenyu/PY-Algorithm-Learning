# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 21:16'

import time


class Solution:
    # 方法一:哈希表计数
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        for key in r:
            if key not in m or m[key] < r[key]:
                return False
        return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
