# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 14:59'

import time
from collections import defaultdict
from math import inf
from typing import List


class WordDistance:
    # 方法一:双指针+哈希表
    def __init__(self, wordsDict: List[str]):
        self.indicesMap = defaultdict(list)
        for i, word in enumerate(wordsDict):  # 将每个单词的下标(不止一个)都计入同一列表中
            self.indicesMap[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        ans = inf
        indices1 = self.indicesMap[word1]
        indices2 = self.indicesMap[word2]
        i, n = 0, len(indices1)
        j, m = 0, len(indices2)
        while i < n and j < m:  # 相互靠近,取距离最小
            index1, index2 = indices1[i], indices2[j]
            ans = min(ans, abs(index1 - index2))
            if index1 < index2:
                i += 1
            else:
                j += 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
