# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/16 18:47'

import time
from bisect import bisect_right
from typing import List


class Solution:
    # 方法一:线性查找
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return next((letter for letter in letters if letter > target), letters[0])

    # 方法二:二分--因为有序,所以如果最后一个字母大于目标则直接二分,若找不到顺序大于的,就返回循环大于的,即最开头元素
    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target)] if target < letters[-1] else letters[0]


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
