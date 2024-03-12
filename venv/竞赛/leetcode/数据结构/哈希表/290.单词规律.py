# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/21 19:55'

import time


class Solution:
    # 方法一:哈希表,双射--元素和元素之间都是唯一的映射
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1 = {}
        string = s.split()
        if len(pattern) != len(string):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                if string[i] in dict1.values():
                    return False
                dict1[pattern[i]] = string[i]
            else:
                if dict1[pattern[i]] != string[i]:
                    return False
        return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
