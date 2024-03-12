# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/14 9:04'

import time
from typing import List


class ValidWordAbbr:
    # 方法一:哈希表--以缩写字符为键,以集合为值
    def __init__(self, dictionary: List[str]):
        import collections
        self.dict1 = collections.defaultdict(set)
        for each in dictionary:
            if len(each) > 2:
                abbreviation = each[0] + str(len(each) - 2) + each[-1]
            else:
                abbreviation = each
            self.dict1[abbreviation].add(each)

    def isUnique(self, word: str) -> bool:
        if len(word) > 2:
            abbreviation = word[0] + str(len(word) - 2) + word[-1]
        else:
            abbreviation = word
        if abbreviation in self.dict1:
            if len(self.dict1[abbreviation]) == 1 and word in self.dict1[abbreviation]:
                return True
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
