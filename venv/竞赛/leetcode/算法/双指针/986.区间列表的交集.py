# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/18 16:47'

import time
from typing import List


class Solution:
    # 方法一:双指针,让右边界较小的移动
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second = 0, 0
        ans = []
        while first < len(firstList) and second < len(secondList):
            if firstList[first][0] < secondList[second][0]:
                if firstList[first][1] >= secondList[second][0]:
                    if firstList[first][1] < secondList[second][1]:
                        ans.append([secondList[second][0], firstList[first][1]])
                        first += 1
                    else:
                        ans.append([secondList[second][0], secondList[second][1]])
                        second += 1
                else:
                    first += 1
            else:
                if firstList[first][0] <= secondList[second][1]:
                    if firstList[first][1] < secondList[second][1]:
                        ans.append([firstList[first][0], firstList[first][1]])
                        first += 1
                    else:
                        ans.append([firstList[first][0], secondList[second][1]])
                        second += 1
                else:
                    second += 1
        return ans


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
